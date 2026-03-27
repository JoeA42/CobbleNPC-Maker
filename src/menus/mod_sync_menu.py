"""Mod synchronization menu"""
from src.utils.mod_sync import ModSync
from src.utils.backup import BackupManager
from src.utils.config import Config
from src.utils.debug import clear_screen

def mod_sync_menu():
    """Mod synchronization menu"""
    config = Config
    backup = BackupManager(config.SERVER_ROOT)
    mod_sync = ModSync(config.MOD_SOURCE, config.MOD_TARGET, backup)
    
    while True:
        clear_screen()
        print("=" * 60)
        print("    MOD SYNC OPERATIONS")
        print("=" * 60)
        
        # Show paths
        print(f"\nSource (local dev): {config.MOD_SOURCE}")
        print(f"Target (server):    {config.MOD_TARGET}")
        
        # Check source exists
        if not config.MOD_SOURCE.exists():
            print("\n⚠️ WARNING: Source mod directory not found!")
            print(f"   Please check MOD_SOURCE in .env file")
            print(f"   Current path: {config.MOD_SOURCE}")
        
        # Check mount
        if not config.check_mount():
            print("\n⚠️ WARNING: Server not mounted!")
            print(f"   Mount with: {config.get_mount_command()}")
        
        # Analyze to show status
        print("\n" + "-" * 60)
        print("ANALYZING MOD DIFFERENCES...")
        analysis = mod_sync.analyze()
        
        # Show quick status
        print("\nSTATUS:")
        if analysis['new']:
            print(f"  📦 New mods to add: {len(analysis['new'])}")
        if analysis['update']:
            print(f"  🔄 Updates available: {len(analysis['update'])}")
        if analysis['missing']:
            print(f"  🗑️  Orphaned mods to remove: {len(analysis['missing'])}")
        if analysis['same']:
            print(f"  ✅ Up to date: {len(analysis['same'])}")
        
        if not any([analysis['new'], analysis['update'], analysis['missing']]):
            print("  ✅ All mods are in sync!")
        
        print("-" * 60)
        
        print("\nOPTIONS:")
        print("  1. Show detailed diff")
        print("  2. Interactive sync (recommended)")
        print("  3. Add new mods only")
        print("  4. Apply updates only")
        print("  5. Remove orphaned mods only")
        print("  6. Dry run (preview changes)")
        print("  7. Back to main menu")
        print("-" * 60)
        
        choice = input("\nEnter choice (1-7): ").strip()
        
        if choice == "1":
            # Show detailed diff
            mod_sync.show_diff(analysis)
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            # Interactive sync with confirmation
            if any([analysis['new'], analysis['update'], analysis['missing']]):
                mod_sync.interactive_sync(dry_run=False)
            else:
                print("\n✅ No changes needed - mods are already in sync!")
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            # Add new mods only
            if analysis['new']:
                print("\n" + "=" * 60)
                print("ADD NEW MODS ONLY")
                print("=" * 60)
                # Show only new mods
                mod_sync.show_diff({
                    'new': analysis['new'],
                    'missing': [],
                    'update': [],
                    'same': []
                })
                confirm = input("\nAdd these new mods to server? (y/n): ").strip().lower()
                if confirm == 'y':
                    mod_sync.sync(analysis, ['new'], dry_run=False)
                else:
                    print("❌ Cancelled")
            else:
                print("\n✅ No new mods to add")
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            # Apply updates only
            if analysis['update']:
                print("\n" + "=" * 60)
                print("APPLY UPDATES ONLY")
                print("=" * 60)
                # Show only updates
                mod_sync.show_diff({
                    'new': [],
                    'missing': [],
                    'update': analysis['update'],
                    'same': []
                })
                confirm = input("\nApply these updates to server? (y/n): ").strip().lower()
                if confirm == 'y':
                    mod_sync.sync(analysis, ['update'], dry_run=False)
                else:
                    print("❌ Cancelled")
            else:
                print("\n✅ No updates available")
            input("\nPress Enter to continue...")
        
        elif choice == "5":
            # Remove orphaned mods only
            if analysis['missing']:
                print("\n" + "=" * 60)
                print("REMOVE ORPHANED MODS ONLY")
                print("=" * 60)
                print("⚠️  WARNING: These mods exist on the server but not in your source folder.")
                print("   Removing them will delete them from the server.")
                print()
                # Show only orphaned mods
                mod_sync.show_diff({
                    'new': [],
                    'missing': analysis['missing'],
                    'update': [],
                    'same': []
                })
                confirm = input("\nRemove these orphaned mods from server? (y/n): ").strip().lower()
                if confirm == 'y':
                    mod_sync.sync(analysis, ['missing'], dry_run=False)
                else:
                    print("❌ Cancelled")
            else:
                print("\n✅ No orphaned mods to remove")
            input("\nPress Enter to continue...")
        
        elif choice == "6":
            # Dry run - preview all changes
            print("\n" + "=" * 60)
            print("DRY RUN - PREVIEW CHANGES ONLY")
            print("=" * 60)
            print("No changes will be made to the server.\n")
            mod_sync.interactive_sync(dry_run=True)
            input("\n[DRY RUN COMPLETE] Press Enter to continue...")
        
        elif choice == "7":
            break
        
        else:
            input("\nInvalid choice. Press Enter to continue...")