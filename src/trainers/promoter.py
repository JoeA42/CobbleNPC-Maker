# src/trainers/promoter.py
import json
import random
from pathlib import Path
from config import RANKS, POKEMON_POOLS, BAG_ITEMS
from src.api import get_evolved_form, get_moves, get_ability, get_min_evolution_level, get_best_held_item
from src.generator.core import scale_trainer_to_rank
from src.generator.evs import train_evs
from src.utils.file_utils import fix_held_items_in_files
from src.utils.debug import debug_print, clear_screen

def parse_filename(filename):
    """Parse filename to extract subclass, name, and rank"""
    name_parts = filename.replace('.json', '').split('_')
    
    possible_ranks = [r["name"] for r in RANKS]
    
    # Rank is the last part
    rank = name_parts[-1] if name_parts[-1] in possible_ranks else None
    if not rank:
        return None, None, None
    
    # Subclass is the first part
    subclass = name_parts[0] if len(name_parts) >= 2 else None
    
    # Name is everything between subclass and rank
    name = '_'.join(name_parts[1:-1]) if len(name_parts) > 2 else "trainer"
    
    return subclass, name, rank

def scale_leader_team(team, target_rank_idx, leader_class):
    """Scale a leader's team to a higher rank without adding new Pokémon"""
    target_rank = RANKS[target_rank_idx]
    target_level = target_rank["level"]
    rank_name = target_rank["name"]
    
    debug_print(f"\n{'='*50}")
    debug_print(f"SCALING LEADER TEAM to {rank_name} (level {target_level})")
    debug_print(f"{'='*50}")
    
    # Get bag items for target rank
    bag_items = BAG_ITEMS.get(target_rank_idx, [{"item": "cobblemon:potion", "quantity": 1}])
    
    new_team = []
    
    # Process each existing Pokémon
    for i, pokemon in enumerate(team):
        species = pokemon["species"]
        original_level = pokemon["level"]
        
        # Evolve if possible
        evolved = get_evolved_form(species, target_level, leader_class)
        
        # New level: scale to target cap (leaders should be at the cap)
        new_level = target_level
        
        if evolved != species:
            min_evo = get_min_evolution_level(species, evolved, leader_class)
            if min_evo and new_level < min_evo:
                new_level = min_evo
        
        new_moves = get_moves(evolved, target_level)
        new_ability = get_ability(evolved)
        new_held = get_best_held_item(evolved, target_rank_idx)
        
        # Preserve IVs, train EVs (leaders get better EV training)
        ivs = pokemon["ivs"]
        evs = train_evs(pokemon["evs"], evolved, target_rank_idx, is_leader=True)
        
        if evolved != species:
            debug_print(f"  ✨ {species} (lvl {original_level}) → {evolved} (lvl {new_level})")
        else:
            debug_print(f"  📈 {species} (lvl {original_level} → {new_level})")
        
        new_team.append({
            "species": evolved,
            "level": new_level,
            "gender": pokemon["gender"],
            "nature": pokemon["nature"],
            "ability": new_ability,
            "shiny": pokemon["shiny"],
            "moveset": new_moves,
            "ivs": ivs,
            "evs": evs,
            "heldItem": new_held
        })
    
    debug_print(f"\n✓ Scaled Leader Team for {rank_name}:")
    for i, p in enumerate(new_team):
        held = f" [held: {p['heldItem']}]" if p.get('heldItem') else ""
        debug_print(f"  {i+1}. {p['species']} (lvl {p['level']}){held}")
    
    return new_team, bag_items

def promote_trainer():
    """Promote an existing trainer to a higher rank"""
    clear_screen()
    print("=" * 60)
    print("    PROMOTE EXISTING TRAINER")
    print("=" * 60)
    
    print("\nSelect source folder:")
    print("  1. Regular trainers (trainers/regular/)")
    print("  2. Gym Leaders (trainers/leaders/)")
    
    source_choice = input("\nChoose (1-2): ").strip()
    
    if source_choice == "1":
        base_dir = Path("trainers/regular")
        is_leader = False
    elif source_choice == "2":
        base_dir = Path("trainers/leaders")
        is_leader = True
    else:
        print("Invalid choice")
        return
    
    if not base_dir.exists():
        print(f"Folder not found: {base_dir}")
        return
    
    # List all available trainer files
    trainer_files = []
    file_display_info = []
    
    if is_leader:
        # Leaders: files directly in folder or in subfolders
        for item in base_dir.iterdir():
            if item.is_dir():
                for file in item.glob("*.json"):
                    trainer_files.append(file)
            elif item.is_file() and item.suffix == ".json":
                trainer_files.append(item)
    else:
        # Regular trainers: subfolders
        for folder in base_dir.iterdir():
            if folder.is_dir():
                for file in folder.glob("*.json"):
                    trainer_files.append(file)
    
    if not trainer_files:
        print("No trainer files found!")
        return
    
    print("\nAvailable trainers:")
    
    for i, file in enumerate(trainer_files[:30]):
        rel_path = file.relative_to(base_dir.parent) if not is_leader else file.relative_to(base_dir.parent)
        filename = file.stem
        
        if is_leader:
            # Leaders: filename format is "leader_rank"
            parts = filename.split('_')
            if len(parts) >= 2 and parts[-1] in [r["name"] for r in RANKS]:
                leader_name = '_'.join(parts[:-1])
                rank = parts[-1]
                display = f"{i+1}. [{leader_name}] {rank}"
            else:
                display = f"{i+1}. {filename}"
        else:
            # Regular trainers
            subclass, name, rank = parse_filename(filename)
            if subclass and name and rank:
                display = f"{i+1}. [{subclass}] {name} ({rank})"
            else:
                display = f"{i+1}. {rel_path}"
        
        file_display_info.append((file, display))
        print(display)
    
    if len(trainer_files) > 30:
        print(f"... and {len(trainer_files)-30} more")
    
    choice = input("\nSelect trainer (number) or enter path: ").strip()
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(trainer_files):
            filepath, _ = file_display_info[idx]
        else:
            print("Invalid selection")
            return
    except ValueError:
        filepath = Path(choice)
        if not filepath.exists():
            print("File not found")
            return
    
    # Load the trainer
    with open(filepath, "r") as f:
        trainer = json.load(f)
    
    # Parse based on source type
    filename = filepath.stem
    
    if not is_leader:
        # Regular trainers - use existing parse logic
        subclass, name, current_rank_name = parse_filename(filename)
        
        if not subclass:
            print(f"\n⚠️ Could not determine subclass from filename: {filename}")
            return
        
        current_rank_idx = None
        if current_rank_name:
            for i, rank in enumerate(RANKS):
                if rank["name"] == current_rank_name:
                    current_rank_idx = i
                    break
        
        if current_rank_idx is None:
            print(f"Invalid rank: {current_rank_name}")
            return
        
        name = name or "trainer"
        subclass = subclass
        
    else:
        # Leaders: filename format is "leader_rank"
        parts = filename.split('_')
        if len(parts) >= 2 and parts[-1] in [r["name"] for r in RANKS]:
            leader_name = '_'.join(parts[:-1])
            current_rank_name = parts[-1]
            name = leader_name
            subclass = leader_name
        else:
            print(f"Could not parse filename: {filename}")
            return
        
        current_rank_idx = None
        for i, rank in enumerate(RANKS):
            if rank["name"] == current_rank_name:
                current_rank_idx = i
                break
        
        if current_rank_idx is None:
            print(f"Invalid rank: {current_rank_name}")
            return
    
    current_rank = RANKS[current_rank_idx]
    print(f"\nCurrent trainer: {name} ({subclass}) - {current_rank['name']} (level cap {current_rank['level']})")
    
    # Determine available next ranks
    next_ranks = []
    for i in range(current_rank_idx + 1, len(RANKS)):
        next_ranks.append(i)
    
    if not next_ranks:
        print("\nAlready at max rank (Master)!")
        return
    
    print("\nPromotion options:")
    print("  1. Random promotion (to a random higher rank)")
    print("  2. Choose specific rank")
    
    promo_choice = input("\nChoose (1-2): ").strip()
    
    if promo_choice == "1":
        target_rank_idx = random.choice(next_ranks)
        print(f"\n🎲 Random promotion to {RANKS[target_rank_idx]['name']}!")
    elif promo_choice == "2":
        print("\nAvailable ranks:")
        for i, rank_idx in enumerate(next_ranks, 1):
            print(f"  {i}. {RANKS[rank_idx]['name']} (level cap {RANKS[rank_idx]['level']})")
        rank_choice = input("\nSelect rank (number): ").strip()
        if not rank_choice.isdigit():
            return
        target_rank_idx = next_ranks[int(rank_choice) - 1]
    else:
        return
    
    target_rank = RANKS[target_rank_idx]
    
    print(f"\n📈 Promoting {name} from {current_rank['name']} to {target_rank['name']}...")
    
    # Scale the trainer using the dedicated function
    if is_leader:
        # For leaders: use scale_leader_team (no new Pokémon, no pools)
        new_team, new_bag = scale_leader_team(trainer["team"], target_rank_idx, subclass)
    else:
        # For regular trainers: use existing scale function
        pokemon_pool = POKEMON_POOLS.get(subclass, {})
        if not pokemon_pool:
            print(f"⚠️ No Pokémon pool found for {subclass}")
            return
        new_team, new_bag = scale_trainer_to_rank(
            trainer["team"], 
            target_rank_idx, 
            subclass, 
            pokemon_pool,
            allow_add_new=False
        )
    
    # Create new trainer
    new_trainer = {
        "name": trainer["name"],
        "ai": trainer["ai"],
        "bag": new_bag,
        "team": new_team
    }
    
    # Save with new rank
    if is_leader:
        # Leaders: save in same folder with format "leader_rank.json"
        leader_folder = filepath.parent
        new_filename = f"{subclass}_{target_rank['name']}.json"
        new_filepath = leader_folder / new_filename
    else:
        # Regular trainers: save in same folder
        new_filename = f"{subclass}_{name.lower()}_{target_rank['name']}.json"
        new_filepath = filepath.parent / new_filename
    
    with open(new_filepath, "w") as f:
        json.dump(new_trainer, f, indent=4)
    
    print(f"\n✅ Saved to {new_filepath}")
    print(f"   Team evolved and leveled up to level {target_rank['level']} cap")
    
    # Show evolution summary
    print("\n📊 Evolution summary:")
    for i, p in enumerate(new_team):
        old_pokemon = trainer["team"][i] if i < len(trainer["team"]) else None
        if old_pokemon and old_pokemon["species"] != p["species"]:
            print(f"   {old_pokemon['species']} → {p['species']} (lvl {old_pokemon['level']} → {p['level']})")
        elif old_pokemon:
            print(f"   {p['species']} leveled up from {old_pokemon['level']} to {p['level']}")
        else:
            print(f"   + {p['species']} (new team member)")