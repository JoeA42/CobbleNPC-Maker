# src/menus/trainer_menu.py
from src.trainers.generator import generate_single_trainer_interactive, generate_trainers_by_class, generate_random_trainers, generate_all_trainers
from src.trainers.promoter import promote_trainer
from src.utils.debug import clear_screen

def trainer_menu():
    while True:
        clear_screen()
        print("=" * 60)
        print("    TRAINER OPERATIONS")
        print("=" * 60)
        print("\nOPTIONS:")
        print("  1. Generate a single trainer (interactive)")
        print("  2. Generate trainers by class")
        print("  3. Generate random trainers (specify count)")
        print("  4. Generate all trainers (one per subclass)")
        print("  5. Promote existing trainer")
        print("  6. Back to main menu")
        print("-" * 60)
        
        choice = input("\nEnter choice (1-6): ").strip()
        
        if choice == "1":
            generate_single_trainer_interactive()
            input("\nPress Enter to continue...")
        elif choice == "2":
            generate_trainers_by_class()
            input("\nPress Enter to continue...")
        elif choice == "3":
            generate_random_trainers()
            input("\nPress Enter to continue...")
        elif choice == "4":
            generate_all_trainers()
            input("\nPress Enter to continue...")
        elif choice == "5":
            promote_trainer()
            input("\nPress Enter to continue...")
        elif choice == "6":
            break
        else:
            input("\nInvalid choice. Press Enter to continue...")