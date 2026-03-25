from src.quest.generator import QuestGenerator
from src.utils.debug import clear_screen

def quest_menu():
    while True:
        clear_screen()
        print("=" * 60)
        print("    QUEST OPERATIONS")
        print("=" * 60)
        print("\nOPTIONS:")
        print("  1. Generate all quests")
        print("  2. Generate specific quest")
        print("  3. Validate quest definitions")
        print("  4. Back to main menu")
        print("-" * 60)
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            generator = QuestGenerator()
            generator.generate_all()
            input("\nPress Enter to continue...")
        elif choice == "2":
            quest_id = input("Enter quest ID: ").strip()
            generator = QuestGenerator()
            generator.generate_quest_by_id(quest_id)
            input("\nPress Enter to continue...")
        elif choice == "3":
            from src.quest.validator import QuestValidator
            validator = QuestValidator()
            validator.validate_all()
            input("\nPress Enter to continue...")
        elif choice == "4":
            break
        else:
            input("\nInvalid choice. Press Enter to continue...")
