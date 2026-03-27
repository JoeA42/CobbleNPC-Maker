"""Mod synchronization between local development instance and server"""
import shutil
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from src.utils.backup import BackupManager

@dataclass
class ModInfo:
    """Information about a mod file"""
    filename: str
    path: Path
    base_name: str
    version: Optional[str]
    size: int
    modified: datetime
    is_newer_than: Optional['ModInfo'] = None

class ModSync:
    """Smart mod synchronization between source and target"""
    
    def __init__(self, source_dir: Path, target_dir: Path, backup_manager: BackupManager):
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.backup = backup_manager
        
    def _extract_mod_info(self, filename: str) -> Tuple[str, Optional[str]]:
        """
        Extract base mod name and version from filename.
        Handles patterns like:
        - cobblemon-fabric-1.5.2+1.20.1.jar -> (cobblemon-fabric, 1.5.2+1.20.1)
        - create-1.20.1-0.5.1.jar -> (create, 1.20.1-0.5.1)
        - jei-1.20.1-forge-15.0.0.30.jar -> (jei, 1.20.1-forge-15.0.0.30)
        """
        # Remove .jar extension
        name = filename.replace('.jar', '')
        
        # Common patterns for version extraction
        # Pattern: modname-version.jar
        match = re.match(r'^(.+?)-(\d[\d\w\.\+\-]+)$', name)
        if match:
            base_name = match.group(1)
            version = match.group(2)
            # Clean up common suffixes
            base_name = re.sub(r'-(fabric|forge|neoforge|bukkit|spigot)$', '', base_name)
            return base_name, version
        
        # If no version pattern found, return full name as base
        return name, None
    
    def _get_mods_dict(self, directory: Path) -> Dict[str, List[ModInfo]]:
        """Get dictionary of mods keyed by base name"""
        mods = {}
        
        if not directory.exists():
            return mods
        
        for file in directory.glob("*.jar"):
            base_name, version = self._extract_mod_info(file.name)
            stat = file.stat()
            
            mod_info = ModInfo(
                filename=file.name,
                path=file,
                base_name=base_name,
                version=version,
                size=stat.st_size,
                modified=datetime.fromtimestamp(stat.st_mtime)
            )
            
            if base_name not in mods:
                mods[base_name] = []
            mods[base_name].append(mod_info)
        
        return mods
    
    def _get_latest_version(self, mod_list: List[ModInfo]) -> ModInfo:
        """Get the latest version from a list of mods (by filename, assumes newer versions have higher numbers)"""
        # Simple approach: sort by filename (usually newer versions come later alphabetically)
        # Could be improved with semantic version parsing if needed
        return sorted(mod_list, key=lambda x: x.filename, reverse=True)[0]
    
    def analyze(self) -> Dict[str, List]:
        """
        Analyze differences between source and target.
        Returns dict with:
            new: List of mods only in source
            missing: List of mods only in target
            update: List of mods where source has newer version
            same: List of mods that match
        """
        result = {
            'new': [],      # In source, not in target
            'missing': [],  # In target, not in source
            'update': [],   # Both exist, source has newer version
            'same': []      # Both exist, versions match
        }
        
        source_mods = self._get_mods_dict(self.source_dir)
        target_mods = self._get_mods_dict(self.target_dir)
        
        # Check source mods
        for base_name, source_list in source_mods.items():
            source_latest = self._get_latest_version(source_list)
            
            if base_name not in target_mods:
                result['new'].append(source_latest)
            else:
                target_latest = self._get_latest_version(target_mods[base_name])
                
                if source_latest.filename != target_latest.filename:
                    # Compare versions - if source has different filename, assume newer
                    source_latest.is_newer_than = target_latest
                    result['update'].append(source_latest)
                else:
                    result['same'].append(source_latest)
        
        # Check for mods only in target
        for base_name, target_list in target_mods.items():
            if base_name not in source_mods:
                for mod in target_list:
                    result['missing'].append(mod)
        
        return result
    
    def show_diff(self, analysis: Dict[str, List]) -> None:
        """Display differences in a formatted way"""
        print("\n" + "=" * 70)
        print("    MOD DIFF ANALYSIS")
        print("=" * 70)
        
        # Summary
        total_source = len(analysis['new']) + len(analysis['update']) + len(analysis['same'])
        total_target = len(analysis['missing']) + len(analysis['update']) + len(analysis['same'])
        
        print(f"\n📊 Summary:")
        print(f"   Source mods: {total_source}")
        print(f"   Target mods: {total_target}")
        
        # New mods
        if analysis['new']:
            print(f"\n📦 NEW MODS (to add to server): {len(analysis['new'])}")
            for mod in sorted(analysis['new'], key=lambda x: x.base_name):
                print(f"   + {mod.filename}")
                print(f"     Size: {mod.size / 1024 / 1024:.1f} MB")
        
        # Missing mods (orphaned)
        if analysis['missing']:
            print(f"\n🗑️  ORPHANED MODS (to possibly remove from server): {len(analysis['missing'])}")
            for mod in sorted(analysis['missing'], key=lambda x: x.base_name):
                print(f"   - {mod.filename}")
                print(f"     Last modified: {mod.modified.strftime('%Y-%m-%d %H:%M')}")
        
        # Updates
        if analysis['update']:
            print(f"\n🔄 UPDATES AVAILABLE: {len(analysis['update'])}")
            for mod in analysis['update']:
                print(f"\n   {mod.base_name}:")
                print(f"     Current: {mod.is_newer_than.filename}")
                print(f"     New:     {mod.filename}")
                print(f"     Size: {mod.is_newer_than.size / 1024 / 1024:.1f} MB → {mod.size / 1024 / 1024:.1f} MB")
        
        # Same mods
        if analysis['same']:
            print(f"\n✅ UP TO DATE: {len(analysis['same'])} mods")
            if len(analysis['same']) <= 10:
                for mod in analysis['same']:
                    print(f"   ✓ {mod.filename}")
            else:
                print(f"   ... and {len(analysis['same'])} more")
        
        if not any([analysis['new'], analysis['missing'], analysis['update']]):
            print("\n✅ All mods are in sync!")
    
    def sync(self, analysis: Dict[str, List], actions: List[str] = None, dry_run: bool = False) -> bool:
        """
        Perform sync based on analysis.
        actions: List of actions to perform: 'new', 'missing', 'update'
        """
        if actions is None:
            actions = ['new', 'missing', 'update']
        
        print("\n" + "=" * 70)
        print(f"{'[DRY RUN] ' if dry_run else ''}MOD SYNC")
        print("=" * 70)
        
        # Create backup if needed and not dry run
        if not dry_run and self.backup and any([analysis['new'], analysis['missing'], analysis['update']]):
            self.backup.create_backup([self.target_dir], "before_mod_sync")
        
        changes_made = False
        
        # Add new mods
        if 'new' in actions and analysis['new']:
            print(f"\n📦 Adding {len(analysis['new'])} new mod(s)...")
            for mod in analysis['new']:
                if dry_run:
                    print(f"   [DRY RUN] Would add: {mod.filename}")
                else:
                    dest = self.target_dir / mod.filename
                    shutil.copy2(mod.path, dest)
                    print(f"   ✓ Added: {mod.filename}")
                    changes_made = True
        
        # Remove orphaned mods
        if 'missing' in actions and analysis['missing']:
            print(f"\n🗑️  Removing {len(analysis['missing'])} orphaned mod(s)...")
            for mod in analysis['missing']:
                if dry_run:
                    print(f"   [DRY RUN] Would remove: {mod.filename}")
                else:
                    mod.path.unlink()
                    print(f"   ✓ Removed: {mod.filename}")
                    changes_made = True
        
        # Update mods
        if 'update' in actions and analysis['update']:
            print(f"\n🔄 Updating {len(analysis['update'])} mod(s)...")
            for mod in analysis['update']:
                if dry_run:
                    print(f"   [DRY RUN] Would update: {mod.base_name}")
                    print(f"     {mod.is_newer_than.filename} → {mod.filename}")
                else:
                    # Remove old version
                    mod.is_newer_than.path.unlink()
                    # Copy new version
                    dest = self.target_dir / mod.filename
                    shutil.copy2(mod.path, dest)
                    print(f"   ✓ Updated: {mod.base_name}")
                    print(f"     {mod.is_newer_than.filename} → {mod.filename}")
                    changes_made = True
        
        if not changes_made:
            print("\n✅ No changes needed")
        elif not dry_run:
            print("\n✅ Mod sync complete!")
        
        return changes_made
    
    def interactive_sync(self, dry_run: bool = False) -> bool:
        """Interactive sync with per-action confirmation"""
        print("\n" + "=" * 70)
        print("    MOD SYNC INTERACTIVE")
        print("=" * 70)
        
        # Analyze
        analysis = self.analyze()
        self.show_diff(analysis)
        
        if not any([analysis['new'], analysis['missing'], analysis['update']]):
            print("\n✅ Already in sync!")
            return True
        
        # Ask what to do
        print("\n" + "=" * 70)
        print("    SELECT ACTIONS")
        print("=" * 70)
        
        actions = []
        
        if analysis['new']:
            print(f"\n📦 New mods: {len(analysis['new'])}")
            choice = input("   Add new mods? (y/n): ").strip().lower()
            if choice == 'y':
                actions.append('new')
        
        if analysis['update']:
            print(f"\n🔄 Updates available: {len(analysis['update'])}")
            choice = input("   Apply updates? (y/n): ").strip().lower()
            if choice == 'y':
                actions.append('update')
        
        if analysis['missing']:
            print(f"\n🗑️  Orphaned mods: {len(analysis['missing'])}")
            choice = input("   Remove orphaned mods? (y/n): ").strip().lower()
            if choice == 'y':
                actions.append('missing')
        
        if not actions:
            print("\n❌ No actions selected. Cancelling.")
            return False
        
        print(f"\nActions to perform: {', '.join(actions)}")
        
        if not dry_run:
            confirm = input("\nProceed with sync? (y/n): ").strip().lower()
            if confirm != 'y':
                print("❌ Cancelled")
                return False
        
        # Perform sync
        return self.sync(analysis, actions, dry_run)