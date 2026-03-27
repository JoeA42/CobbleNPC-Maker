from src.menus.trainer_menu import trainer_menu
from src.menus.leader_menu import leader_menu
from src.menus.npc_menu import npc_menu
from src.menus.quest_menu import quest_menu
from src.menus.pool_menu import pool_menu
from src.menus.export_menu import export_menu
from src.menus.mod_sync_menu import mod_sync_menu  # New import
from src.utils.debug import clear_screen

def main_menu():
    while True:
        clear_screen()
        print("=" * 60)
        print("    COBBLE NPC MAKER")
        print("=" * 60)
        print("\nOPTIONS:")
        print("  1. Trainer Operations")
        print("  2. Gym Leader Operations")
        print("  3. NPC Operations")
        print("  4. Quest Operations")
        print("  5. Pool Generation Operations")
        print("  6. Export to Server")
        print("  7. Mod Sync Operations")  # New option
        print("  8. Exit")
        print("-" * 60)
        
        choice = input("\nEnter choice (1-8): ").strip()
        
        if choice == "1":
            trainer_menu()
        elif choice == "2":
            leader_menu()
        elif choice == "3":
            npc_menu()
        elif choice == "4":
            quest_menu()
        elif choice == "5":
            pool_menu()
        elif choice == "6":
            export_menu()
        elif choice == "7":
            mod_sync_menu()  # New menu
        elif choice == "8":
            print("\nGoodbye!")
            break
        else:
            input("\nInvalid choice. Press Enter to continue...")