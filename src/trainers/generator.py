# src/trainers/generator.py
import json
import random
from pathlib import Path
from config import RANKS, FOLDERS, NAMES, POKEMON_POOLS, BAG_ITEMS
from src.generator.core import generate_team, generate_progression, scale_trainer_to_rank
from src.utils.file_utils import fix_held_items_in_files
from src.utils.debug import debug_print, clear_screen

def generate_single_trainer(folder, subclass, name, base_rank):
    """Generate a single trainer with all 3 ranks"""
    pokemon_pool = POKEMON_POOLS.get(subclass, {})
    if not pokemon_pool:
        print(f"⚠️ No Pokémon pool found for {subclass}")
        return
    
    progression = generate_progression(base_rank)
    
    output_dir = Path(f"trainers/regular/{folder}")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    team = None
    generated_files = []
    
    for rank_idx in progression:
        rank_name = RANKS[rank_idx]["name"]
        team, bag_items = generate_team(pokemon_pool, rank_idx, subclass, team, is_leader=False)
        
        trainer = {
            "name": name,
            "ai": {"type": "rct", "data": {"maxSelectMargin": 0.5}},
            "bag": bag_items,
            "team": team
        }
        
        filename = f"{subclass}_{name.lower()}_{rank_name}.json"
        filepath = output_dir / filename
        
        with open(filepath, "w") as f:
            json.dump(trainer, f, indent=4)
        
        print(f"✓ Generated: {filename}")
        generated_files.append(filepath)
    
    # Clean up held items
    fix_held_items_in_files(generated_files)
    
    print(f"\n✅ Generated {name} ({subclass}) with {len(progression)} ranks in {output_dir}/")

def generate_single_trainer_interactive():
    """Interactive single trainer generation"""
    clear_screen()
    print("=" * 60)
    print("    GENERATE SINGLE TRAINER")
    print("=" * 60)
    
    # Show folders
    folders = list(FOLDERS.keys())
    for i, f in enumerate(folders, 1):
        print(f"{i}. {f}")
    
    folder_choice = input("\nSelect folder (number): ").strip()
    if not folder_choice.isdigit():
        return
    
    folder = folders[int(folder_choice) - 1]
    subclasses = FOLDERS[folder]
    
    print(f"\nSubclasses in {folder}:")
    for i, s in enumerate(subclasses, 1):
        print(f"{i}. {s}")
    
    sub_choice = input("\nSelect subclass (number): ").strip()
    if not sub_choice.isdigit():
        return
    
    subclass = subclasses[int(sub_choice) - 1]
    
    # Get name
    name_pool = NAMES.get(subclass, [f"{subclass}_{i}" for i in range(1, 6)])
    print(f"\nAvailable names: {', '.join(name_pool)}")
    name = input("Enter name (or press Enter for random): ").strip()
    if not name:
        name = random.choice(name_pool)
    
    # Get base rank
    print("\nBase ranks (0=novice to 6=ace):")
    for i in range(7):
        print(f"{i}. {RANKS[i]['name']} (level {RANKS[i]['level']})")
    rank_choice = input("Enter base rank (0-6, or Enter for random): ").strip()
    base_rank = random.randint(0, 6) if not rank_choice else int(rank_choice)
    
    generate_single_trainer(folder, subclass, name, base_rank)

def generate_multiple_trainers(count, folder=None, subclass=None):
    """Generate multiple trainers"""
    # Determine which subclasses to use
    if folder and subclass:
        subclasses_to_use = [(folder, subclass)]
    elif folder:
        subclasses_to_use = [(folder, s) for s in FOLDERS.get(folder, [])]
    else:
        subclasses_to_use = []
        for f, subs in FOLDERS.items():
            for s in subs:
                subclasses_to_use.append((f, s))
    
    # Track used names to avoid duplicates
    used_names = set()
    generated = 0
    
    # Shuffle to randomize which subclasses get trainers
    random.shuffle(subclasses_to_use)
    
    for folder_name, subclass_name in subclasses_to_use:
        if generated >= count:
            break
        
        # Get name pool for this subclass
        name_pool = NAMES.get(subclass_name, [f"{subclass_name}_{i}" for i in range(1, 10)])
        
        # Filter out used names
        available_names = [n for n in name_pool if n not in used_names]
        if not available_names:
            # If all names used, generate a unique name
            available_names = [f"{subclass_name}_{len(used_names)+1}"]
        
        # Pick a random name
        name = random.choice(available_names)
        used_names.add(name)
        
        # Random base rank between 0 and 6
        base_rank = random.randint(0, 6)
        
        print(f"\n🎲 Generating {subclass_name} trainer: {name}")
        generate_single_trainer(folder_name, subclass_name, name, base_rank)
        generated += 1
    
    print(f"\n✅ Generated {generated} trainers")

def generate_trainers_by_class():
    """Generate trainers by class menu option"""
    clear_screen()
    print("=" * 60)
    print("    GENERATE TRAINERS BY CLASS")
    print("=" * 60)
    
    folders = list(FOLDERS.keys())
    for i, f in enumerate(folders, 1):
        print(f"{i}. {f}")
    
    folder_choice = input("\nSelect folder (number): ").strip()
    if not folder_choice.isdigit():
        return
    
    folder = folders[int(folder_choice) - 1]
    subclasses = FOLDERS[folder]
    
    print(f"\nSubclasses in {folder}:")
    for i, s in enumerate(subclasses, 1):
        print(f"{i}. {s}")
    print(f"{len(subclasses)+1}. All subclasses in {folder}")
    
    sub_choice = input("\nSelect subclass (number): ").strip()
    if not sub_choice.isdigit():
        return
    
    sub_idx = int(sub_choice) - 1
    if sub_idx == len(subclasses):
        count_input = input("How many trainers to generate? (default: 3): ").strip()
        count = int(count_input) if count_input else 3
        generate_multiple_trainers(count, folder=folder)
    else:
        subclass = subclasses[sub_idx]
        count_input = input("How many trainers to generate? (default: 3): ").strip()
        count = int(count_input) if count_input else 3
        generate_multiple_trainers(count, folder=folder, subclass=subclass)

def generate_random_trainers():
    """Generate random trainers menu option"""
    clear_screen()
    print("=" * 60)
    print("    GENERATE RANDOM TRAINERS")
    print("=" * 60)
    
    count_input = input("How many trainers to generate? (default: 10): ").strip()
    count = int(count_input) if count_input else 10
    
    generate_multiple_trainers(count)

def generate_all_trainers():
    """Generate all trainers (one per subclass) menu option"""
    clear_screen()
    print("=" * 60)
    print("    GENERATE ALL TRAINERS")
    print("=" * 60)
    
    confirm = input("This will generate one trainer for every subclass. Continue? (y/n): ").strip().lower()
    if confirm == 'y':
        total_subclasses = sum(len(subs) for subs in FOLDERS.values())
        generate_multiple_trainers(total_subclasses)