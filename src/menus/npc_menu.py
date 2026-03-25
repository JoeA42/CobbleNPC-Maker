# src/menus/npc_menu.py
from src.npc.trainer_npc import generate_all_npcs, generate_for_trainer
from src.npc.gym_leader_npc import generate_all_gym_leaders
from src.utils.config_generator import generate_trainer_config
from src.utils.debug import clear_screen
from config import FOLDERS

def npc_menu():
    while True:
        clear_screen()
        print("=" * 60)
        print("    NPC OPERATIONS")
        print("=" * 60)
        print("\nOPTIONS:")
        print("  1. Generate NPCs for all trainers")
        print("  2. Generate NPC for a specific trainer")
        print("  3. Generate Gym Leader NPCs")
        print("  4. Generate Trainer Config (for KubeJS)")
        print("  5. Back to main menu")
        print("-" * 60)
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == "1":
            generate_all_npcs()
            input("\nPress Enter to continue...")
        elif choice == "2":
            print("\nAvailable classes:")
            for folder, subclasses in FOLDERS.items():
                print(f"\n{folder}:")
                for sub in subclasses:
                    print(f"  - {sub}")
            
            trainer_class = input("\nEnter trainer class: ").strip().lower()
            trainer_name = input("Enter trainer name: ").strip()
            
            generate_for_trainer(trainer_class, trainer_name)
            input("\nPress Enter to continue...")
        elif choice == "3":
            generate_all_gym_leaders()
            input("\nPress Enter to continue...")
        elif choice == "4":
            generate_trainer_config()
            input("\nPress Enter to continue...")
        elif choice == "5":
            break
        else:
            input("\nInvalid choice. Press Enter to continue...")