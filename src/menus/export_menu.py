"""Export generated files to server directories"""
import shutil
import os
from pathlib import Path
from datetime import datetime
from src.utils.debug import clear_screen
from src.utils.toml_updater import TOMLUpdater
from src.utils.backup import BackupManager
from src.utils.config import Config
import importlib
import json

class Exporter:
    def __init__(self):
        self.config = Config
        self.output_dir = self.config.OUTPUT_DIR
        self.backup = BackupManager(self.config.SERVER_ROOT)
        
        # Map output folders to server destinations
        self.destinations = {
            # Trainer JSONs
            "trainers/regular": self.config.TRAINERS_REGULAR,
            "trainers/leaders": self.config.TRAINERS_LEADERS,
            
            # NPC SNBTs
            "npcs/regular": self.config.NPCS_PATH,
            "npcs/gym_leaders": self.config.NPCS_PATH,
            "npcs/quests": self.config.NPCS_PATH,
            
            # KubeJS files
            "kubejs/data/trainer_config.json": self.config.KUBEJS_DATA / "trainer_config.json",
            "quests/kubejs/quests": self.config.KUBEJS_SCRIPTS / "quests",
        }
    
    def _get_trainer_base_name(self, filename):
        """Extract base trainer name without rank suffix (for display)"""
        name = filename.stem.replace('_', ' ').title()
        rank_suffixes = ['Pro', 'Elite', 'Master', 'Challenger', 'Ace', 
                        'Trainer', 'Novice', 'Rookie', 'Apprentice',
                        'Masterstar1', 'Masterstar2', 'Masterstar3']
        for suffix in rank_suffixes:
            if name.endswith(f' {suffix}'):
                return name[:-len(suffix)-1]
        return name

    def _get_trainer_raw_base_name(self, filename):
        """Extract raw base trainer name (lowercase, underscores) without rank suffix"""
        name = filename.stem  # Keep original case and underscores
        
        # Remove rank suffix
        rank_suffixes = ['_novice', '_rookie', '_apprentice', '_trainer', '_challenger', 
                        '_pro', '_ace', '_elite', '_master', '_masterstar1', 
                        '_masterstar2', '_masterstar3']
        for suffix in rank_suffixes:
            if name.endswith(suffix):
                return name[:-len(suffix)]
        return name
    
    def _check_mount(self):
        """Check if the server directory is mounted"""
        return self.config.check_mount()
    
    def _show_diff(self, source_dir, target_dir, prefix=""):
        """Show differences between source and target directories (recursive)"""
        source_files = set()
        target_files = set()
        
        if source_dir.exists():
            # Get all files recursively with relative paths
            for file in source_dir.rglob("*"):
                if file.is_file():
                    rel_path = file.relative_to(source_dir)
                    source_files.add(str(rel_path))
        
        if target_dir.exists():
            # Get all files recursively with relative paths
            for file in target_dir.rglob("*"):
                if file.is_file():
                    rel_path = file.relative_to(target_dir)
                    target_files.add(str(rel_path))
        
        new_files = source_files - target_files
        missing_files = target_files - source_files
        common_files = source_files & target_files
        
        if prefix:
            print(f"\n{prefix}:")
        
        if new_files:
            print(f"  📦 New files to add ({len(new_files)}):")
            for f in sorted(new_files):
                print(f"     + {f}")
        
        if missing_files:
            print(f"  🗑️  Orphaned files to possibly delete ({len(missing_files)}):")
            for f in sorted(missing_files):
                # Try to get file info if it exists
                if target_dir.exists():
                    file_path = target_dir / f
                    if file_path.exists():
                        mtime = datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d')
                        size = file_path.stat().st_size / 1024
                        print(f"     - {f} (last modified: {mtime}, {size:.1f} KB)")
                    else:
                        print(f"     - {f}")
        
        if not new_files and not missing_files:
            print(f"  ✅ No changes (already in sync)")
        
        return new_files, missing_files, common_files
    
    def _sync_folder(self, source_dir, target_dir, description, dry_run=False, confirm_deletions=True, protect_patterns=None):
        """Sync a folder: add new files, create missing folders, optionally delete orphans"""
        print(f"\n{'[DRY RUN] ' if dry_run else ''}{description}")
        print(f"  Source: {source_dir}")
        print(f"  Target: {target_dir}")
        
        # Default protect patterns for gym leaders (novice rank files)
        if protect_patterns is None:
            protect_patterns = []
        
        # Check source exists
        if not source_dir.exists():
            print(f"  ⚠️ Source folder not found: {source_dir}")
            return False
        
        # Show diff recursively
        new_files, missing_files, common_files = self._show_diff(source_dir, target_dir, "Changes detected")
        
        # Filter out protected files from deletion candidates
        protected_files = []
        if protect_patterns:
            filtered_missing = []
            for rel_path in missing_files:
                is_protected = False
                for pattern in protect_patterns:
                    if pattern in rel_path:
                        is_protected = True
                        protected_files.append(rel_path)
                        break
                if not is_protected:
                    filtered_missing.append(rel_path)
            missing_files = filtered_missing
            
            if protected_files:
                print(f"\n  🛡️ Protected files (will NOT be deleted):")
                for f in protected_files:
                    print(f"     🛡️ {f}")
        
        # Also find new folders (directories that exist in source but not in target)
        new_folders = set()
        if source_dir.exists():
            for item in source_dir.rglob("*"):
                if item.is_dir():
                    rel_path = item.relative_to(source_dir)
                    target_folder = target_dir / rel_path
                    if not target_folder.exists():
                        new_folders.add(str(rel_path))
        
        if new_folders:
            print(f"\n  📁 New folders to create ({len(new_folders)}):")
            for folder in sorted(new_folders):
                print(f"     + {folder}/")
        
        if not new_files and not missing_files and not new_folders:
            print("  ✅ Already in sync")
            return True
        
        # Create new folders
        if new_folders and not dry_run:
            print(f"\n  📁 Creating {len(new_folders)} new folder(s)...")
            for rel_path in new_folders:
                target_folder = target_dir / rel_path
                target_folder.mkdir(parents=True, exist_ok=True)
                print(f"     ✓ Created {rel_path}/")
        
        # Handle new files
        if new_files:
            print(f"\n  📦 Adding {len(new_files)} new file(s)...")
            if not dry_run:
                for rel_path in new_files:
                    src_file = source_dir / rel_path
                    dst_file = target_dir / rel_path
                    dst_file.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src_file, dst_file)
                    print(f"     ✓ Added {rel_path}")
        
        # Handle orphaned files (with confirmation) - only those not protected
        if missing_files and confirm_deletions:
            print(f"\n  🗑️  Found {len(missing_files)} orphaned file(s) on server:")
            
            # List files with info
            for i, rel_path in enumerate(sorted(missing_files), 1):
                file_path = target_dir / rel_path
                if file_path.exists():
                    mtime = datetime.fromtimestamp(file_path.stat().st_mtime).strftime('%Y-%m-%d %H:%M')
                    print(f"     {i}. {rel_path} (last modified: {mtime})")
                else:
                    print(f"     {i}. {rel_path}")
            
            print("\n  Options:")
            print("     y - delete this file")
            print("     n - keep this file")
            print("     a - delete all remaining")
            print("     q - quit deletion (keep remaining)")
            
            files_to_delete = []
            delete_all = False
            
            for rel_path in sorted(missing_files):
                if delete_all:
                    files_to_delete.append(rel_path)
                    continue
                
                file_path = target_dir / rel_path
                if not file_path.exists():
                    continue
                
                choice = input(f"  Delete '{rel_path}'? (y/n/a/q): ").strip().lower()
                
                if choice == 'y':
                    files_to_delete.append(rel_path)
                elif choice == 'a':
                    delete_all = True
                    files_to_delete.append(rel_path)
                elif choice == 'q':
                    print("  Quitting deletion, keeping remaining files")
                    break
                # 'n' does nothing
            
            # Perform deletions
            if files_to_delete and not dry_run:
                for rel_path in files_to_delete:
                    file_path = target_dir / rel_path
                    if file_path.exists():
                        file_path.unlink()
                        print(f"     ✓ Deleted {rel_path}")
                        
                        # Remove empty parent directories
                        parent = file_path.parent
                        while parent != target_dir and not any(parent.iterdir()):
                            parent.rmdir()
                            print(f"     ✓ Removed empty folder: {parent.relative_to(target_dir)}")
                            parent = parent.parent
                            
            elif files_to_delete and dry_run:
                print(f"  [DRY RUN] Would delete: {', '.join(files_to_delete)}")
        
        # Return new folders for TOML update
        return new_folders

    def sync_trainers(self, dry_run=False):
        """Sync trainers folder with two-step process"""
        print("\n" + "=" * 60)
        print(f"{'[DRY RUN] ' if dry_run else ''}SYNC TRAINERS")
        print("=" * 60)
        
        # Check mount
        if not self._check_mount():
            print("\n⚠️ Server not mounted!")
            print(f"   Mount with: {self.config.get_mount_command()}")
            return False
        
        new_folders = set()
        
        # Collect info for messages
        new_trainer_files = []
        trainer_groups = {}  # Group trainers by base name for display
        new_folders_list = []
        
        # Sync regular trainers
        source_regular = self.output_dir / "trainers/regular"
        target_regular = self.config.TRAINERS_REGULAR
        
        # Collect regular trainer info BEFORE sync
        if source_regular.exists():
            for f in source_regular.rglob("*.json"):
                rel_path = f.relative_to(source_regular)
                new_trainer_files.append(str(rel_path))
                
                # Group by base name (without rank)
                base_name = self._get_trainer_base_name(f)
                if base_name not in trainer_groups:
                    trainer_groups[base_name] = []
                trainer_groups[base_name].append(f.stem)
        
        # Sync gym leaders with protection for novice files
        source_leaders = self.output_dir / "trainers/leaders"
        target_leaders = self.config.TRAINERS_LEADERS
        
        # Protect files that contain "_novice" in the path (gym leader base templates)
        protect_patterns = ["_novice."]
        
        # Collect gym leader info
        if source_leaders.exists():
            for f in source_leaders.rglob("*.json"):
                if "_novice" in f.name:
                    continue
                rel_path = f.relative_to(source_leaders)
                new_trainer_files.append(str(rel_path))
                # Gym leaders are grouped differently
                base_name = f.stem.split('_')[0].replace('_', ' ').title()
                if base_name not in trainer_groups:
                    trainer_groups[base_name] = []
                trainer_groups[base_name].append(f"{base_name} (Gym Leader)")
        
        # PHASE 1: Add new trainer files - SEND GROUPED MESSAGES
        if trainer_groups:
            self._send_rcon_message(f"§6[EXPORT {'SIMULATION' if dry_run else 'START'}] Phase 1: Adding trainer files...", dry_run=dry_run)
            for base_name, ranks in sorted(trainer_groups.items())[:5]:
                rank_count = len(ranks)
                self._send_rcon_message(f"§e  • {base_name} ({rank_count} rank{'s' if rank_count > 1 else ''})", dry_run=dry_run)
            if len(trainer_groups) > 5:
                self._send_rcon_message(f"§e  • ... and {len(trainer_groups)-5} more", dry_run=dry_run)
        
        # Actually perform the sync
        result = self._sync_folder(source_regular, target_regular, "Regular Trainers", dry_run, confirm_deletions=True, protect_patterns=None)
        if isinstance(result, set):
            new_folders.update(result)
            new_folders_list = list(result)
        
        result = self._sync_folder(source_leaders, target_leaders, "Gym Leaders", dry_run, confirm_deletions=True, protect_patterns=protect_patterns)
        if isinstance(result, set):
            new_folders.update(result)
            if result:
                new_folders_list.extend(list(result))
        
        # PHASE 2: Folder creation message
        if new_folders_list:
            self._send_rcon_message(f"§6[EXPORT {'SIMULATION' if dry_run else 'START'}] Creating new trainer folders...", dry_run=dry_run)
            for folder in new_folders_list[:5]:
                self._send_rcon_message(f"§e  • {folder}", dry_run=dry_run)
            if len(new_folders_list) > 5:
                self._send_rcon_message(f"§e  • ... and {len(new_folders_list)-5} more", dry_run=dry_run)
        
        # Send completion message for this phase
        total_trainers = len(new_trainer_files)
        total_folders = len(new_folders_list)
        if total_trainers > 0 or total_folders > 0:
            self._send_rcon_message(f"§a[EXPORT {'SIMULATION' if dry_run else 'START'}] Phase 1 complete: {total_trainers} files added, {total_folders} folders created", dry_run=dry_run)
        
        # If new folders were added, offer to update TOML (only for real export)
        if new_folders and not dry_run:
            print("\n" + "=" * 60)
            print("📁 NEW TRAINER FOLDERS DETECTED")
            print("=" * 60)
            print("\nThe following new folders were created:")
            for folder in sorted(new_folders):
                print(f"  - {folder}")
            
            print("\nThese should be added to tbcs-server.toml to make trainers accessible.")
            choice = input("\nUpdate TOML config now? (y/n): ").strip().lower()
            
            if choice == 'y':
                # Load game_data
                try:
                    import source.game_data as game_data
                    importlib.reload(game_data)
                except ImportError:
                    print("\n❌ Could not load source.game_data")
                    return True
                
                updater = TOMLUpdater(self.config.WORLD_PATH)
                updater.update_toml(game_data)
        
        return True

    def _send_rcon_message(self, message, dry_run=False, ops_only=True):
        """Send a message to Minecraft via RCON directly"""
        prefix = "[SIMULATION] " if dry_run else ""
        full_message = f"{prefix}{message}"
        
        try:
            from mcrcon import MCRcon
            
            host = self.config.SERVER_HOST
            port = 25575
            password = "backup123"
            
            if dry_run:
                print(f"  📡 Sending to Minecraft: {full_message}")
            
            with MCRcon(host, password, port=port) as mcr:
                if ops_only:
                    # Send as a tellraw to ops only (shows in console and to ops)
                    response = mcr.command(f"tellraw @a[level=1..] {{\"text\":\"{full_message}\",\"color\":\"gold\"}}")
                else:
                    response = mcr.command(f"say {full_message}")
                if dry_run:
                    print(f"  ✅ Message sent!")
                    
        except Exception as e:
            if dry_run:
                print(f"  ⚠️ RCON error: {e}")

    def replace_npcs(self, dry_run=False, clear_first=True):
        """Replace NPCs folder - copies to both humanoid and humanoid_slim folders"""
        print("\n" + "=" * 60)
        print(f"{'[DRY RUN] ' if dry_run else ''}REPLACE NPCS")
        print("=" * 60)
        
        if not self._check_mount():
            print("\n⚠️ Server not mounted!")
            return False
        
        source_npcs = self.output_dir / "npcs"
        
        # Easy NPCs preset locations
        easy_npc_base = self.config.DATA_PATH / "config/easy_npc/preset"
        humanoid_path = easy_npc_base / "humanoid"
        humanoid_slim_path = easy_npc_base / "humanoid_slim"
        
        if not source_npcs.exists():
            print(f"⚠️ Source NPC folder not found: {source_npcs}")
            return False
        
        print(f"  Source: {source_npcs}")
        print(f"  Target (humanoid): {humanoid_path}")
        print(f"  Target (slim): {humanoid_slim_path}")
        
        # Skip quest NPCs for now
        skip_quests = True
        
        # Collect NPC counts for messages
        regular_count = 0
        gym_count = 0
        quest_count = 0
        
        src_regular = source_npcs / "regular"
        src_gym = source_npcs / "gym_leaders"
        src_quests = source_npcs / "quests"
        
        if src_regular.exists():
            regular_count = len(list(src_regular.glob("*.snbt")) + list(src_regular.glob("*.npc")))
        if src_gym.exists():
            gym_count = len(list(src_gym.glob("*.snbt")) + list(src_gym.glob("*.npc")))
        if src_quests.exists() and not skip_quests:
            quest_count = len(list(src_quests.glob("*.snbt")) + list(src_quests.glob("*.npc")))
        
        total_npcs = regular_count + gym_count
        
        # Send phase message
        self._send_rcon_message(f"§6[EXPORT {'SIMULATION' if dry_run else 'START'}] Phase 2: Replacing NPCs...", dry_run=dry_run)
        self._send_rcon_message(f"§e  • Clearing existing NPCs", dry_run=dry_run)
        self._send_rcon_message(f"§e  • Deploying {total_npcs} new NPCs to both humanoid and humanoid_slim", dry_run=dry_run)
        
        # Show NPC files to deploy
        print("\n  NPC files to deploy:")
        if src_regular.exists():
            files = list(src_regular.glob("*.snbt")) + list(src_regular.glob("*.npc"))
            if files:
                print(f"    regular/: {len(files)} file(s)")
                for f in files[:5]:
                    print(f"      - {f.name}")
                if len(files) > 5:
                    print(f"      ... and {len(files)-5} more")
        
        if src_gym.exists():
            files = list(src_gym.glob("*.snbt")) + list(src_gym.glob("*.npc"))
            if files:
                print(f"    gym_leaders/: {len(files)} file(s)")
                for f in files:
                    print(f"      - {f.name}")
        
        if src_quests.exists() and skip_quests:
            files = list(src_quests.glob("*.snbt")) + list(src_quests.glob("*.npc"))
            if files:
                print(f"    quests/: {len(files)} file(s) - SKIPPED (not developed)")
        
        print("\n  ⚠️ This will CLEAR existing NPCs from both folders and replace with new ones!")
        print("     (NPC templates will be available for both Steve and Alex models)")
        
        if not dry_run:
            confirm = input("\nContinue? (y/n): ").strip().lower()
            if confirm != 'y':
                self._send_rcon_message(f"§c[EXPORT START] Phase 2 cancelled by user", dry_run=dry_run)
                print("❌ Cancelled")
                return False
        
        if not dry_run:
            # Create backup if enabled
            if self.config.BACKUP_ENABLED:
                self.backup.create_backup([humanoid_path, humanoid_slim_path], "before_npc_replace")
            
            # Clear target folders
            print("\n  Clearing existing NPCs...")
            if humanoid_path.exists():
                shutil.rmtree(humanoid_path)
            if humanoid_slim_path.exists():
                shutil.rmtree(humanoid_slim_path)
            
            humanoid_path.mkdir(parents=True, exist_ok=True)
            humanoid_slim_path.mkdir(parents=True, exist_ok=True)
            
            # Copy regular NPCs to both folders
            if src_regular.exists():
                print("\n  Copying regular NPCs...")
                for item in src_regular.glob("*"):
                    if item.is_file():
                        # Copy to humanoid
                        shutil.copy2(item, humanoid_path / item.name)
                        # Copy to humanoid_slim
                        shutil.copy2(item, humanoid_slim_path / item.name)
                        print(f"     ✓ {item.name} -> both folders")
            
            # Copy gym leader NPCs to both folders
            if src_gym.exists():
                print("\n  Copying gym leader NPCs...")
                for item in src_gym.glob("*"):
                    if item.is_file():
                        shutil.copy2(item, humanoid_path / item.name)
                        shutil.copy2(item, humanoid_slim_path / item.name)
                        print(f"     ✓ {item.name} -> both folders")
            
            # Quest NPCs are skipped
            if skip_quests and src_quests.exists():
                print("\n  ⚠️ Quest NPCs skipped (not developed yet)")
            
            print("\n✅ NPCs replaced successfully")
            self._send_rcon_message(f"§a[EXPORT START] Phase 2 complete: {total_npcs} NPCs deployed to both humanoid and humanoid_slim", dry_run=dry_run)
        else:
            print("\n[DRY RUN] Would replace NPCs")
            self._send_rcon_message(f"§a[EXPORT SIMULATION] Phase 2 would deploy {total_npcs} NPCs to both folders", dry_run=dry_run)
        
        return True

    def sync_trainer_config(self, dry_run=False):
        """Validate trainer_config.json matches actual trainer files, then copy to server"""
        print("\n" + "=" * 60)
        print(f"{'[DRY RUN] ' if dry_run else ''}SYNC TRAINER CONFIG")
        print("=" * 60)
        
        if not self._check_mount():
            print("\n⚠️ Server not mounted!")
            return False
        
        source_config = self.output_dir / "kubejs/data/trainer_config.json"
        target_config = self.config.TRAINER_CONFIG
        
        # STEP 1: Check if source config exists
        if not source_config.exists():
            print("\n❌ ERROR: trainer_config.json not found in outputs/")
            print("   Generate it using: NPC Operations -> Option 4")
            return False
        
        # STEP 2: Load config
        import json
        with open(source_config, 'r') as f:
            config_data = json.load(f)
        
        # STEP 3: Find all trainer base names from actual files in outputs
        trainer_base_names = set()
        trainers_regular = self.output_dir / "trainers/regular"
        trainers_leaders = self.output_dir / "trainers/leaders"

        if trainers_regular.exists():
            for f in trainers_regular.rglob("*.json"):
                base_name = self._get_trainer_raw_base_name(f)  # Use raw version
                trainer_base_names.add(base_name)

        if trainers_leaders.exists():
            for f in trainers_leaders.rglob("*.json"):
                if "_novice" in f.name:
                    continue
                base_name = f.stem.split('_')[0]  # Already raw
                trainer_base_names.add(base_name)

        config_trainers = set(config_data.keys())

        # Find mismatches
        missing_in_config = trainer_base_names - config_trainers
        extra_in_config = config_trainers - trainer_base_names
        
        if missing_in_config or extra_in_config:
            print("\n❌ ERROR: Trainer config does not match actual trainer files!")
            if missing_in_config:
                print(f"\n   Missing in config ({len(missing_in_config)}):")
                for t in sorted(missing_in_config):
                    print(f"      - {t}")
                print("\n   These trainers have JSON files but no entry in trainer_config.json")
            if extra_in_config:
                print(f"\n   Extra in config ({len(extra_in_config)}):")
                for t in sorted(extra_in_config):
                    print(f"      - {t}")
                print("\n   These entries have no matching JSON files")
            
            print("\n   Please regenerate trainer_config.json using:")
            print("      NPC Operations -> Option 4 (Generate Trainer Config)")
            return False
        
        # STEP 5: Config is valid - show what will change on server
        if target_config.exists():
            with open(target_config, 'r') as f:
                server_config = json.load(f)
            
            to_add = config_trainers - set(server_config.keys())
            to_remove = set(server_config.keys()) - config_trainers
            
            if to_add or to_remove:
                print("\n📊 Changes to server:")
                if to_add:
                    print(f"  ➕ Will add {len(to_add)} trainer(s)")
                if to_remove:
                    print(f"  ➖ Will remove {len(to_remove)} orphaned trainer(s)")
            else:
                print("\n  ✅ Config already matches server")
                return True
        else:
            print("\n  📦 Server config doesn't exist - will create new one")
        
        # Send phase message
        self._send_rcon_message(f"§6[EXPORT {'SIMULATION' if dry_run else 'START'}] Phase 3: Syncing trainer_config.json...", dry_run=dry_run)
        if to_add:
            self._send_rcon_message(f"§e  • Adding {len(to_add)} trainers", dry_run=dry_run)
        if to_remove:
            self._send_rcon_message(f"§e  • Removing {len(to_remove)} orphaned trainers", dry_run=dry_run)
        
        if dry_run:
            print("\n[DRY RUN] Would copy trainer_config.json to server")
            self._send_rcon_message(f"§a[EXPORT SIMULATION] Phase 3 would update trainer_config.json", dry_run=dry_run)
            return True
        
        # Real sync
        confirm = input("\nCopy trainer_config.json to server? (y/n): ").strip().lower()
        if confirm != 'y':
            print("❌ Cancelled")
            return False
        
        # Create backup
        if self.config.BACKUP_ENABLED:
            self.backup.create_backup([target_config], "before_trainer_config_sync")
        
        # Copy the file
        target_config.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_config, target_config)
        
        print(f"\n✅ Copied trainer_config.json to server")
        self._send_rcon_message(f"§a[EXPORT START] Phase 3 complete: trainer_config.json updated", dry_run=dry_run)
        
        return True

    def update_toml(self, dry_run=False):
        """Update TOML config with current trainer paths"""
        print("\n" + "=" * 60)
        print(f"{'[DRY RUN] ' if dry_run else ''}UPDATE TOML CONFIG")
        print("=" * 60)
        
        if not self._check_mount():
            print("\n⚠️ Server not mounted.")
            return False
        
        if not self.config.WORLD_PATH.exists():
            print(f"\n⚠️ World path not found: {self.config.WORLD_PATH}")
            return False
        
        # Load game_data
        try:
            import source.game_data as game_data
            importlib.reload(game_data)
        except ImportError:
            print("\n❌ Could not load source.game_data")
            return False
        
        updater = TOMLUpdater(self.config.WORLD_PATH)
        
        # Get current and new paths for messages
        current_paths = updater.load_current_paths()
        new_paths = updater.generate_paths_from_config(game_data)
        missing = set(new_paths) - set(current_paths)
        extra = set(current_paths) - set(new_paths)
        
        # Send phase message
        self._send_rcon_message(f"§6[EXPORT {'SIMULATION' if dry_run else 'START'}] Phase 4: Updating TOML paths...", dry_run=dry_run)
        
        if missing:
            self._send_rcon_message(f"§e  • Adding {len(missing)} new trainer paths", dry_run=dry_run)
            for p in sorted(missing)[:3]:
                self._send_rcon_message(f"§e    - {p}", dry_run=dry_run)
            if len(missing) > 3:
                self._send_rcon_message(f"§e    - ... and {len(missing)-3} more", dry_run=dry_run)
        
        if extra:
            self._send_rcon_message(f"§e  • Removing {len(extra)} obsolete paths", dry_run=dry_run)
        
        if not missing and not extra:
            self._send_rcon_message(f"§a[EXPORT {'SIMULATION' if dry_run else 'START'}] Phase 4: Already up to date", dry_run=dry_run)
        
        if dry_run:
            updater.show_diff(game_data)
            self._send_rcon_message(f"§a[EXPORT SIMULATION] Phase 4 would add {len(missing)} paths, remove {len(extra)} paths", dry_run=dry_run)
            return True
        
        # Real sync
        updater.update_toml(game_data)
        self._send_rcon_message(f"§a[EXPORT START] Phase 4 complete: Added {len(missing)} paths, removed {len(extra)} paths", dry_run=dry_run)
        
        return True

    def export_all(self, dry_run=False):
        """Export all generated files with per-phase confirmation"""
        print("\n" + "=" * 60)
        print(f"{'[DRY RUN] ' if dry_run else ''}EXPORT ALL")
        print("=" * 60)
        
        # Check mount
        if not self._check_mount():
            print("\n⚠️ Server not mounted!")
            return False
        
        # Phase 1: Sync trainers
        if dry_run:
            self.sync_trainers(dry_run=True)
        else:
            self.sync_trainers(dry_run=False)
            print("\n" + "-" * 60)
            confirm = input("Phase 1 complete. Continue to Phase 2 (NPCs)? (y/n): ").strip().lower()
            if confirm != 'y':
                print("❌ Export cancelled")
                return False
        
        # Phase 2: Replace NPCs
        if dry_run:
            self.replace_npcs(dry_run=True, clear_first=True)
        else:
            self.replace_npcs(dry_run=False, clear_first=True)
            print("\n" + "-" * 60)
            confirm = input("Phase 2 complete. Continue to Phase 3 (Trainer Config)? (y/n): ").strip().lower()
            if confirm != 'y':
                print("❌ Export cancelled")
                return False
        
        # Phase 3: Sync trainer config
        if dry_run:
            self.sync_trainer_config(dry_run=True)
        else:
            self.sync_trainer_config(dry_run=False)
            print("\n" + "-" * 60)
            confirm = input("Phase 3 complete. Continue to Phase 4 (TOML paths)? (y/n): ").strip().lower()
            if confirm != 'y':
                print("❌ Export cancelled")
                return False
        
        # Phase 4: Update TOML paths
        if dry_run:
            self.update_toml(dry_run=True)
        else:
            self.update_toml(dry_run=False)
        
        # Final completion message
        if not dry_run:
            self._send_rcon_message(f"§a[EXPORT COMPLETE] All phases finished! Run §6/reload §ato activate changes.", dry_run=False)
            print("\n✅ Export complete! Run '/reload' on the server to activate changes.")
        
        return True

    def dry_run(self):
        """Show what would change without making changes"""
        self.export_all(dry_run=True)
        input("\n[DRY RUN COMPLETE] Press Enter to continue...")
    
    def show_status(self):
        """Show current status of all folders"""
        clear_screen()
        print("=" * 60)
        print("    EXPORT STATUS")
        print("=" * 60)
        
        if not self._check_mount():
            print("⚠️ Server mount: NOT CONNECTED")
            print(f"   Mount with: {self.config.get_mount_command()}")
            return
        
        print("✅ Server mount: Connected")
        print(f"\n📁 Server root: {self.config.SERVER_ROOT}")
        print(f"📁 World path: {self.config.WORLD_PATH}\n")
        
        # Check each destination
        for name, dest in self.destinations.items():
            status = "✅" if dest.exists() else "❌"
            print(f"  {status} {name}: {dest}")
        
        # Check config
        if self.config.TBCS_CONFIG.exists():
            print(f"  ✅ TBCS config: {self.config.TBCS_CONFIG}")
        else:
            print(f"  ❌ TBCS config: {self.config.TBCS_CONFIG}")
        
        input("\nPress Enter to continue...")

def export_menu():
    exporter = Exporter()
    
    while True:
        clear_screen()
        print("=" * 60)
        print("    EXPORT OPERATIONS")
        print("=" * 60)
        
        # Show mount status
        if exporter._check_mount():
            print("✅ Server mount: Connected")
        else:
            print("⚠️ Server mount: NOT CONNECTED")
            print(f"   Mount: {exporter.config.get_mount_command()}")
        
        print("\nOPTIONS:")
        print("  🏃 DRY RUN (preview - safe):")
        print("    1. Dry run (preview all changes)")
        print("\n  TRAINERS (Critical - needs confirmation):")
        print("    2. Sync trainers (add new + confirm deletions)")
        print("\n  NPCS (Template files - safe to replace):")
        print("    3. Replace NPCs (clear and copy fresh)")
        print("\n  CONFIG:")
        print("    4. Sync trainer_config.json (add/remove entries)")
        print("    5. Update TOML paths (based on game_data)")
        print("    6. Show TOML diff")
        print("\n  ALL:")
        print("    7. Export ALL (trainers + NPCs + config)")
        print("\n  UTILITIES:")
        print("    8. Show status (check folders)")
        print("    9. Configure server path")
        print("    10. Back to main menu")
        print("-" * 60)
        print(f"📁 Server root: {exporter.config.SERVER_ROOT}")
        print(f"📁 Output dir: {exporter.output_dir}")
        print("-" * 60)
        
        choice = input("\nEnter choice (1-10): ").strip()
        
        if choice == "1":
            exporter.dry_run()
        elif choice == "2":
            exporter.sync_trainers(dry_run=False)
            input("\nPress Enter to continue...")
        elif choice == "3":
            exporter.replace_npcs(dry_run=False, clear_first=True)
            input("\nPress Enter to continue...")
        elif choice == "4":
            exporter.sync_trainer_config(dry_run=False)
            input("\nPress Enter to continue...")
        elif choice == "5":
            exporter.update_toml(dry_run=False)
            input("\nPress Enter to continue...")
        elif choice == "6":
            exporter.update_toml(dry_run=True)
            input("\nPress Enter to continue...")
        elif choice == "7":
            exporter.export_all(dry_run=False)
            input("\nPress Enter to continue...")
        elif choice == "8":
            exporter.show_status()
        elif choice == "9":
            new_path = input("Enter server root path (e.g., ~/MCServer-local): ").strip()
            if new_path:
                print(f"\n⚠️ To update permanently, edit .env file")
                print(f"   SERVER_ROOT={new_path}")
            input("\nPress Enter to continue...")
        elif choice == "10":
            break
        else:
            input("\nInvalid choice. Press Enter to continue...")
    exporter = Exporter()
    
    while True:
        clear_screen()
        print("=" * 60)
        print("    EXPORT OPERATIONS")
        print("=" * 60)
        
        # Show mount status
        if exporter._check_mount():
            print("✅ Server mount: Connected")
        else:
            print("⚠️ Server mount: NOT CONNECTED")
            print(f"   Mount: {exporter.config.get_mount_command()}")
        
        print("\nOPTIONS:")
        print("  TRAINERS (Critical - needs confirmation):")
        print("    1. Sync trainers (add new + confirm deletions)")
        print("    2. Dry run (preview all changes)")
        print("\n  NPCS (Template files - safe to replace):")
        print("    3. Replace NPCs (clear and copy fresh)")
        print("\n  CONFIG:")
        print("    4. Sync trainer_config.json (add/remove entries)")
        print("    5. Update TOML paths (based on game_data)")
        print("    6. Show TOML diff")
        print("\n  ALL:")
        print("    7. Export ALL (trainers + NPCs + config)")
        print("\n  UTILITIES:")
        print("    8. Show status (check folders)")
        print("    9. Configure server path")
        print("    10. Back to main menu")
        print("-" * 60)
        print(f"📁 Server root: {exporter.config.SERVER_ROOT}")
        print(f"📁 Output dir: {exporter.output_dir}")
        print("-" * 60)
        
        choice = input("\nEnter choice (1-10): ").strip()
        
        if choice == "1":
            exporter.sync_trainers(dry_run=False)
            input("\nPress Enter to continue...")
        elif choice == "2":
            exporter.dry_run()
        elif choice == "3":
            exporter.replace_npcs(dry_run=False, clear_first=True)
            input("\nPress Enter to continue...")
        elif choice == "4":
            exporter.sync_trainer_config(dry_run=False)
            input("\nPress Enter to continue...")
        elif choice == "5":
            exporter.update_toml(dry_run=False)
            input("\nPress Enter to continue...")
        elif choice == "6":
            exporter.update_toml(dry_run=True)
            input("\nPress Enter to continue...")
        elif choice == "7":
            exporter.export_all(dry_run=False)
            input("\nPress Enter to continue...")
        elif choice == "8":
            exporter.show_status()
        elif choice == "9":
            new_path = input("Enter server root path (e.g., ~/MCServer-local): ").strip()
            if new_path:
                # Update would need to modify .env file
                print(f"\n⚠️ To update permanently, edit .env file")
                print(f"   SERVER_ROOT={new_path}")
            input("\nPress Enter to continue...")
        elif choice == "10":
            break
        else:
            input("\nInvalid choice. Press Enter to continue...")