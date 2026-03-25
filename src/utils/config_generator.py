# src/utils/config_generator.py
#!/usr/bin/env python3
"""
generate_trainer_config.py - Generate/Update trainer_config.json from existing trainer profiles
Run this after generating new trainers to update the config
"""

import json
from pathlib import Path

# Rank order and their badge count thresholds
RANK_BADGE_COUNTS = {
    "novice": 0,
    "rookie": 1,
    "apprentice": 2,
    "trainer": 3,
    "challenger": 4,
    "pro": 5,
    "ace": 6,
    "elite": 7,
    "master": 8,
    "masterstar1": 9,
    "masterstar2": 10,
    "masterstar3": 11
}

def load_existing_config(config_path):
    """Load existing config if it exists"""
    if config_path.exists():
        try:
            with open(config_path, "r") as f:
                return json.load(f)
        except:
            print(f"⚠️ Could not load existing config, creating new one")
    return {}

def scan_trainer_profiles(base_dir="trainers/regular"):
    """Scan the trainers/regular folder and return all trainers found"""
    base_path = Path(base_dir)
    if not base_path.exists():
        print(f"Error: {base_dir} not found!")
        return {}
    
    trainers = {}
    
    for class_dir in base_path.iterdir():
        if not class_dir.is_dir():
            continue
        
        for json_file in class_dir.glob("*.json"):
            filename = json_file.stem
            parts = filename.split('_')
            
            if len(parts) < 3:
                continue
            
            rank = parts[-1]
            name = '_'.join(parts[1:-1])
            trainer_class = parts[0]
            
            if rank not in RANK_BADGE_COUNTS:
                continue
            
            trainer_id = f"{trainer_class}_{name}"
            
            if trainer_id not in trainers:
                trainers[trainer_id] = {
                    "class": trainer_class,
                    "name": name,
                    "ranks": {}
                }
            
            trainers[trainer_id]["ranks"][rank] = RANK_BADGE_COUNTS[rank]
    
    return trainers

def scan_gym_leader_profiles(base_dir="trainers/leaders"):
    """Scan the trainers/leaders folder and return all gym leaders found"""
    base_path = Path(base_dir)
    if not base_path.exists():
        return {}
    
    gym_leaders = {}
    valid_ranks = ["novice", "rookie", "apprentice", "trainer", "challenger", "pro", "ace", "elite", "master", "masterstar1", "masterstar2", "masterstar3"]
    
    for leader_dir in base_path.iterdir():
        if not leader_dir.is_dir():
            continue
        
        for json_file in leader_dir.glob("*.json"):
            filename = json_file.stem
            parts = filename.split('_')
            
            if len(parts) < 2:
                continue
            
            rank = parts[-1]
            leader_id = '_'.join(parts[:-1])
            
            if rank not in valid_ranks:
                continue
            
            if leader_id not in gym_leaders:
                gym_leaders[leader_id] = {
                    "id": leader_id,
                    "ranks": {}
                }
            
            gym_leaders[leader_id]["ranks"][rank] = RANK_BADGE_COUNTS[rank]
    
    return gym_leaders

def update_config(existing_config, found_trainers):
    """Update existing config with newly found trainers"""
    updated_config = existing_config.copy()
    added = 0
    updated = 0
    
    for trainer_id, info in found_trainers.items():
        if trainer_id not in updated_config:
            updated_config[trainer_id] = {"ranks": info["ranks"]}
            added += 1
            print(f"  ➕ Added: {trainer_id} - ranks: {', '.join(info['ranks'].keys())}")
        else:
            existing_ranks = set(updated_config[trainer_id]["ranks"].keys())
            new_ranks = set(info["ranks"].keys())
            
            if existing_ranks != new_ranks:
                updated_config[trainer_id]["ranks"] = info["ranks"]
                updated += 1
                print(f"  🔄 Updated: {trainer_id} - ranks: {', '.join(new_ranks)}")
    
    return updated_config, added, updated

def update_gym_config(existing_config, found_gym_leaders):
    """Update existing gym leader config"""
    updated_config = existing_config.copy()
    added = 0
    updated = 0
    
    for leader_id, info in found_gym_leaders.items():
        if leader_id not in updated_config:
            updated_config[leader_id] = {"ranks": info["ranks"]}
            added += 1
            print(f"  ➕ Added gym leader: {leader_id} - ranks: {', '.join(info['ranks'].keys())}")
        else:
            existing_ranks = set(updated_config[leader_id].get("ranks", {}).keys())
            new_ranks = set(info["ranks"].keys())
            
            if existing_ranks != new_ranks:
                updated_config[leader_id]["ranks"] = info["ranks"]
                updated += 1
                print(f"  🔄 Updated gym leader: {leader_id} - ranks: {', '.join(new_ranks)}")
    
    return updated_config, added, updated

def save_config(config, output_path):
    """Save config to file"""
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, "w") as f:
        json.dump(config, f, indent=2)
    
    print(f"\n💾 Saved to: {output_file}")

def generate_trainer_config(output_path="kubejs/data/trainer_config.json"):
    """Generate/Update the trainer_config.json file"""
    print("=" * 60)
    print("GENERATING TRAINER CONFIG")
    print("=" * 60)
    
    print("\n📂 Scanning regular trainer profiles...")
    found_trainers = scan_trainer_profiles()
    
    if not found_trainers:
        print("No trainer profiles found!")
    else:
        print(f"   Found {len(found_trainers)} trainers")
    
    print("\n📂 Scanning gym leader profiles...")
    found_gym_leaders = scan_gym_leader_profiles()
    
    if not found_gym_leaders:
        print("No gym leader profiles found!")
    else:
        print(f"   Found {len(found_gym_leaders)} gym leaders")
    
    if not found_trainers and not found_gym_leaders:
        print("No profiles found!")
        return False
    
    print("\n📖 Loading existing config...")
    existing_config = load_existing_config(Path(output_path))
    print(f"   Existing config has {len(existing_config)} entries")
    
    print("\n🔄 Updating regular trainers...")
    updated_config, added, updated = update_config(existing_config, found_trainers)
    
    print("\n🔄 Updating gym leaders...")
    updated_config, gym_added, gym_updated = update_gym_config(updated_config, found_gym_leaders)
    
    total_added = added + gym_added
    total_updated = updated + gym_updated
    
    if total_added == 0 and total_updated == 0:
        print("\n   No changes detected")
    else:
        print(f"\n📊 Summary:")
        print(f"   Regular trainers added: {added}, updated: {updated}")
        print(f"   Gym leaders added: {gym_added}, updated: {gym_updated}")
        print(f"   Total entries: {len(updated_config)}")
        
        save_config(updated_config, output_path)
    
    return True

if __name__ == "__main__":
    generate_trainer_config()