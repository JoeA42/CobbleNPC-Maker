# src/menus/leader_menu.py
from src.trainers.leader_generator import generate_leader_all_ranks
from src.utils.debug import clear_screen

def leader_menu():
    while True:
        clear_screen()
        print("=" * 60)
        print("    GYM LEADER OPERATIONS")
        print("=" * 60)
        print("\nOPTIONS:")
        print("  1. Generate all ranks for a leader")
        print("  2. Back to main menu")
        print("-" * 60)
        
        choice = input("\nEnter choice (1-2): ").strip()
        
        if choice == "1":
            generate_leader_all_ranks()
            input("\nPress Enter to continue...")
        elif choice == "2":
            break
        else:
            input("\nInvalid choice. Press Enter to continue...")