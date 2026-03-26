# src/trainers/leader_generator.py
import json
from pathlib import Path
from source.game_data import RANKS, BAG_ITEMS
from src.trainers.promoter import scale_leader_team
from src.utils.file_utils import fix_held_items_in_files
from src.utils.debug import clear_screen

def generate_leader_all_ranks():
    """Generate all ranks for a leader starting from a chosen base rank"""
    clear_screen()
    print("=" * 60)
    print("    GENERATE LEADER ALL RANKS")
    print("=" * 60)
    
    # Get leaders source folder (where seed files are stored)
    source_dir = Path("source/leaders")
    if not source_dir.exists():
        print(f"Source folder not found: {source_dir}")
        print("Create source/leaders/ and add your base leader JSON files")
        return
    
    # List all leader source files
    leader_files = []
    for folder in source_dir.iterdir():
        if folder.is_dir():
            for file in folder.glob("*.json"):
                leader_files.append(file)
        elif folder.is_file() and folder.suffix == ".json":
            leader_files.append(folder)
    
    if not leader_files:
        print("No leader source files found in source/leaders/")
        return
    
    print("\nAvailable leader source files:")
    for i, file in enumerate(leader_files):
        rel_path = file.relative_to(source_dir.parent)
        print(f"{i+1}. {rel_path}")
    
    choice = input("\nSelect leader file (number): ").strip()
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(leader_files):
            filepath = leader_files[idx]
        else:
            print("Invalid selection")
            return
    except:
        print("Invalid input")
        return
    
    # Parse filename to get leader name and current rank
    filename = filepath.stem
    parts = filename.split('_')
    
    # Find the rank at the end
    possible_ranks = [r["name"] for r in RANKS]
    current_rank_name = None
    leader_name = None
    
    for i in range(len(parts)-1, -1, -1):
        if parts[i] in possible_ranks:
            current_rank_name = parts[i]
            leader_name = '_'.join(parts[:i])
            break
    
    if not current_rank_name or not leader_name:
        print(f"Could not parse filename: {filename}")
        print("Expected format: leader_rank.json (e.g., ikuma_novice.json)")
        return
    
    # Find current rank index
    current_rank_idx = None
    for i, rank in enumerate(RANKS):
        if rank["name"] == current_rank_name:
            current_rank_idx = i
            break
    
    if current_rank_idx is None:
        print(f"Invalid rank: {current_rank_name}")
        return
    
    print(f"\n📁 Selected: {leader_name} - {current_rank_name}")
    
    # Load the base trainer
    with open(filepath, "r") as f:
        trainer = json.load(f)
    
    print(f"   Team size: {len(trainer['team'])} Pokémon")
    
    # Show available ranks to generate from
    next_ranks = []
    for i in range(current_rank_idx + 1, len(RANKS)):
        next_ranks.append(i)
    
    if not next_ranks:
        print("\nAlready at max rank (Master)!")
        return
    
    print("\nRanks to generate:")
    for i, rank_idx in enumerate(next_ranks):
        print(f"  {i+1}. {RANKS[rank_idx]['name']} (level {RANKS[rank_idx]['level']})")
    
    # Ask which ranks to generate
    gen_choice = input("\nGenerate all higher ranks? (y/n, default: y): ").strip().lower()
    if gen_choice == 'n':
        rank_choice = input("Enter rank numbers to generate (comma separated, e.g., 1,3,5): ").strip()
        try:
            selected = [int(x.strip()) - 1 for x in rank_choice.split(',')]
            ranks_to_generate = [next_ranks[i] for i in selected if 0 <= i < len(next_ranks)]
        except:
            print("Invalid selection")
            return
    else:
        ranks_to_generate = next_ranks
    
    if not ranks_to_generate:
        print("No ranks selected")
        return
    
    # Create output directory
    output_dir = Path(f"outputs/trainers/leaders/{leader_name}")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate selected ranks
    generated = []
    current_team = trainer["team"]
    current_bag = trainer["bag"]
    generated_files = []
    
    for target_rank_idx in ranks_to_generate:
        target_rank = RANKS[target_rank_idx]
        print(f"\n📈 Generating {leader_name}_{target_rank['name']}.json...")
        
        # Scale the team
        new_team, new_bag = scale_leader_team(current_team, target_rank_idx, leader_name)
        
        # Save the new rank
        new_filename = f"{leader_name}_{target_rank['name']}.json"
        new_filepath = output_dir / new_filename
        
        new_trainer = {
            "name": trainer["name"],
            "ai": trainer["ai"],
            "bag": new_bag,
            "team": new_team
        }
        
        with open(new_filepath, "w") as f:
            json.dump(new_trainer, f, indent=4)
        
        generated.append(new_filename)
        generated_files.append(new_filepath)
        print(f"   ✓ Saved to: {new_filepath}")
        
        # Update for next iteration (if generating sequentially)
        current_team = new_team
        current_bag = new_bag
    
    # Clean up held items
    fix_held_items_in_files(generated_files)
    
    print(f"\n✅ Generated {len(generated)} files in {output_dir}/")
    for f in generated:
        print(f"   - {f}")
