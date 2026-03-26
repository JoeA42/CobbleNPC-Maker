from src.utils.debug import clear_screen
import subprocess
import sys
from pathlib import Path

def pool_menu():
    while True:
        clear_screen()
        print("=" * 60)
        print("    POOL GENERATION OPERATIONS")
        print("=" * 60)
        print("\nOPTIONS:")
        print("  1. Generate Pokémon pools (from PokéAPI)")
        print("  2. Fetch evolution items (from PokéAPI)")
        print("  3. Fix held items in trainer files")
        print("  4. Back to main menu")
        print("-" * 60)
        print("📁 Outputs:")
        print("   - Pokémon pools: config/pokemon_pools.json")
        print("   - Evolution items: config/evolution_items_found.json")
        print("-" * 60)
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            print("\n📦 Generating Pokémon pools from PokéAPI...")
            print("   This may take several minutes...")
            try:
                result = subprocess.run(
                    [sys.executable, "src/generator/pools/generate_pools.py"],
                    capture_output=True,
                    text=True
                )
                print(result.stdout)
                if result.stderr:
                    print("Errors:")
                    print(result.stderr)
                print("\n✅ Pokémon pools generated to config/pokemon_pools.json")
            except Exception as e:
                print(f"\n❌ Error: {e}")
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            print("\n📦 Fetching evolution items from PokéAPI...")
            print("   This may take several minutes...")
            try:
                result = subprocess.run(
                    [sys.executable, "src/generator/pools/fetch_all_evolution_items.py"],
                    capture_output=True,
                    text=True
                )
                print(result.stdout)
                if result.stderr:
                    print("Errors:")
                    print(result.stderr)
                print("\n✅ Evolution items fetched to config/evolution_items_found.json")
            except Exception as e:
                print(f"\n❌ Error: {e}")
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            print("\n🔧 Fixing held items in trainer files...")
            try:
                result = subprocess.run(
                    [sys.executable, "src/utils/fix_held_items.py"],
                    capture_output=True,
                    text=True
                )
                print(result.stdout)
                if result.stderr:
                    print("Errors:")
                    print(result.stderr)
                print("\n✅ Held items fixed")
            except Exception as e:
                print(f"\n❌ Error: {e}")
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            break
        else:
            input("\nInvalid choice. Press Enter to continue...")
