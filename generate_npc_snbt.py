#!/usr/bin/env python3
"""
generate_npc_snbt.py - Generate Easy NPCs .snbt files from existing trainer JSONs
Run this after generating trainers to create corresponding NPC files
"""

import json
import random
import re
from pathlib import Path
from config import RANKS, DIALOGS, get_dialog, get_gym_dialog

# Create RANK_INFO from the ranks in config
RANK_INFO = {rank["name"]: rank for rank in RANKS}

def format_class_name(class_name):
    """
    Convert lowercase class names to display format
    Examples:
        bugcatcher -> "Bug Catcher"
        richboy -> "Rich Boy"
        parkranger -> "Park Ranger"
        scientist -> "Scientist"
        ranger -> "Ranger"
    """
    words = class_name.split('_')
    formatted = ' '.join(word.capitalize() for word in words)
    return formatted

def load_template(template_path):
    """Load the base SNBT template"""
    with open(template_path, "r") as f:
        return f.read()

def generate_uuids():
    """Generate 4 random integers for UUIDs"""
    return [random.randint(-2147483648, 2147483647) for _ in range(4)]

def generate_dialog_dataset(trainer_class, available_ranks):
    """Generate the dialog dataset for the ranks this trainer actually has"""
    dialog_dataset = []
    
    # Add flavor dialog (for right-click) - always first
    flavor_text = get_dialog(trainer_class, "flavor")
    dialog_dataset.append({
        "Buttons": [{
            "Actions": [{"Type": "CLOSE_DIALOG"}],
            "Name": "Goodbye"
        }],
        "Name": "Default",
        "Texts": [{"Text": flavor_text}]
    })
    
    # Sort ranks by badge count
    sorted_ranks = sorted(available_ranks, key=lambda r: RANK_INFO[r]["badges"])
    
    # Add battle start dialogs for each rank
    for rank_name in sorted_ranks:
        dialog_text = get_dialog(trainer_class, "battle_start", rank_name)
        dialog_dataset.append({
            "Buttons": [{
                "Actions": [{"Type": "CLOSE_DIALOG"}],
                "Name": "Close"
            }],
            "Name": f"battle_start_{rank_name}",
            "Texts": [{"Text": dialog_text}]
        })
    
    # Add victory dialog
    dialog_dataset.append({
        "Buttons": [{
            "Actions": [{"Type": "CLOSE_DIALOG"}],
            "Name": "Close"
        }],
        "Name": "victory",
        "Texts": [{"Text": get_dialog(trainer_class, "victory")}]
    })
    
    # Add defeat dialog
    dialog_dataset.append({
        "Buttons": [{
            "Actions": [{"Type": "CLOSE_DIALOG"}],
            "Name": "Close"
        }],
        "Name": "defeat",
        "Texts": [{"Text": get_dialog(trainer_class, "defeat")}]
    })
    
    return dialog_dataset


def format_dialog_dataset(dialog_dataset):
    """Format dialog dataset as SNBT string with proper indentation"""
    lines = ["["]
    for i, dialog in enumerate(dialog_dataset):
        dialog_str = json.dumps(dialog, indent=2)
        dialog_str = "\n  ".join(dialog_str.split("\n"))
        lines.append(f"  {dialog_str}" + ("," if i < len(dialog_dataset) - 1 else ""))
    lines.append("]")
    return "\n".join(lines)

def find_trainer_profiles(base_dir="trainers/regular"):
    """Find all trainer profiles and group them by trainer"""
    base_path = Path(base_dir)
    if not base_path.exists():
        return {}
    
    trainers = {}
    valid_ranks = ["novice", "rookie", "apprentice", "trainer", "challenger", "pro", "ace", "elite", "master"]
    
    for subclass_dir in base_path.iterdir():
        if not subclass_dir.is_dir():
            continue
        
        for json_file in subclass_dir.glob("*.json"):
            filename = json_file.stem
            parts = filename.split('_')
            
            if len(parts) < 3:
                continue
            
            rank = parts[-1]
            name = '_'.join(parts[1:-1])
            trainer_class = parts[0]
            
            if rank not in valid_ranks:
                continue
            
            key = (trainer_class, name)
            if key not in trainers:
                trainers[key] = {"class": trainer_class, "name": name, "ranks": []}
            
            trainers[key]["ranks"].append(rank)
    
    return trainers

def generate_npc_snbt(trainer_info, template_dir="SNBT Templates", output_dir="npcs"):
    """Generate an SNBT file for a trainer"""
    trainer_class = trainer_info["class"]
    name = trainer_info["name"]
    available_ranks = trainer_info["ranks"]
    
    # Format display name
    display_name = f"{format_class_name(trainer_class)} {name.capitalize()}"
    
    # Create trainer ID for battle command
    trainer_id = f"{trainer_class}_{name.lower()}"
    
    # Randomly choose between Alex and Steve models
    is_alex = random.choice([True, False])
    entity_type = "easy_npc:humanoid_slim" if is_alex else "easy_npc:humanoid"
    variant_type = "ALEX" if is_alex else "STEVE"
    
    # Load single template
    template_path = Path(template_dir) / "base_trainer.snbt"
    if not template_path.exists():
        print(f"⚠️ Template not found: {template_path}")
        return None
    
    template = load_template(template_path)
    
    # Generate dialog dataset
    dialog_dataset = generate_dialog_dataset(trainer_class, available_ranks)
    dialog_string = format_dialog_dataset(dialog_dataset)
    
    # Generate UUIDs
    owner_uuid = generate_uuids()
    preset_uuid = generate_uuids()
    entity_uuid = generate_uuids()
    
    # Replace placeholders
    content = template
    content = content.replace("${entity_type}", entity_type)
    content = content.replace("${variant_type}", variant_type)
    content = content.replace("${name}", display_name)
    content = content.replace("${trainer_id}", trainer_id)
    content = content.replace("${dialogs}", dialog_string)
    content = content.replace("${owner_uuid}", ",".join(map(str, owner_uuid)))
    content = content.replace("${preset_uuid}", ",".join(map(str, preset_uuid)))
    content = content.replace("${uuid}", ",".join(map(str, entity_uuid)))
    
    # Save
    output_path = Path(output_dir) / f"{name.lower()}_{trainer_class}.npc.snbt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content)
    
    return output_path

def generate_all_npcs(trainers_dir="trainers/regular", template_dir="SNBT Templates", output_dir="npcs"):
    """Generate NPC files for all trainers found in the trainers directory"""
    trainers = find_trainer_profiles(trainers_dir)
    
    if not trainers:
        print(f"No trainer profiles found in {trainers_dir}")
        return 0
    
    print(f"\n📝 Found {len(trainers)} trainers to process:")
    for (trainer_class, name), info in trainers.items():
        rank_count = len(info["ranks"])
        display_class = format_class_name(trainer_class)
        print(f"   - {name} ({display_class}) - {rank_count} ranks")
    
    print(f"\n🎲 Generating NPC SNBT files...")
    
    generated = 0
    for trainer_info in trainers.values():
        output_path = generate_npc_snbt(trainer_info, template_dir, output_dir)
        if output_path:
            print(f"✓ Generated: {output_path}")
            generated += 1
    
    print(f"\n✅ Generated {generated} NPC files in {output_dir}/")
    return generated

def generate_for_trainer(trainer_class, trainer_name, trainers_dir="trainers/regular", template_dir="SNBT Templates", output_dir="npcs"):
    """Generate NPC file for a specific trainer"""
    trainers = find_trainer_profiles(trainers_dir)
    
    key = (trainer_class, trainer_name)
    if key not in trainers:
        print(f"Trainer not found: {trainer_name} ({trainer_class})")
        print("\nAvailable trainers:")
        for (cls, name), info in trainers.items():
            display_class = format_class_name(cls)
            print(f"  - {name} ({display_class})")
        return None
    
    output_path = generate_npc_snbt(trainers[key], template_dir, output_dir)
    if output_path:
        print(f"✓ Generated: {output_path}")
    return output_path

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 2:
        trainer_class = sys.argv[1]
        trainer_name = sys.argv[2]
        generate_for_trainer(trainer_class, trainer_name)
    else:
        generate_all_npcs()


# Add this to generate_npc_snbt.py

def generate_gym_leader_snbt(leader_info, template_dir="SNBT Templates", output_dir="npcs/gym_leaders"):
    """Generate an SNBT file for a gym leader"""
    leader_id = leader_info["id"]
    name = leader_info["name"]
    badge = leader_info["badge"]
    skin_url = leader_info.get("skin_url", "")
    
    # Format display name
    display_name = name
    
    # Randomly choose between Alex and Steve models
    is_alex = random.choice([True, False])
    entity_type = "easy_npc:humanoid_slim" if is_alex else "easy_npc:humanoid"
    variant_type = "ALEX" if is_alex else "STEVE"
    
    # Load gym leader template
    template_path = Path(template_dir) / "base_gym_leader.snbt"
    if not template_path.exists():
        print(f"⚠️ Template not found: {template_path}")
        return None
    
    template = load_template(template_path)
    
    # Get dialog lines from config
    flavor_text = get_gym_dialog(leader_id, "flavor")
    challenge_text = get_gym_dialog(leader_id, "challenge")
    victory_first_text = get_gym_dialog(leader_id, "victory_first")
    victory_rematch_text = get_gym_dialog(leader_id, "victory_rematch")
    defeat_text = get_gym_dialog(leader_id, "defeat")
    rematch_cooldown_text = get_gym_dialog(leader_id, "rematch_cooldown")
    
    # Generate UUIDs
    owner_uuid = generate_uuids()
    preset_uuid = generate_uuids()
    entity_uuid = generate_uuids()
    
    # Replace placeholders
    content = template
    content = content.replace("${entity_type}", entity_type)
    content = content.replace("${variant_type}", variant_type)
    content = content.replace("${name}", display_name)
    content = content.replace("${leader_id}", leader_id)
    content = content.replace("${flavor_dialog}", flavor_text)
    content = content.replace("${challenge_dialog}", challenge_text)
    content = content.replace("${victory_first_dialog}", victory_first_text)
    content = content.replace("${victory_rematch_dialog}", victory_rematch_text)
    content = content.replace("${defeat_dialog}", defeat_text)
    content = content.replace("${rematch_cooldown_dialog}", rematch_cooldown_text)
    content = content.replace("${skin_url}", skin_url)
    content = content.replace("${owner_uuid}", ",".join(map(str, owner_uuid)))
    content = content.replace("${preset_uuid}", ",".join(map(str, preset_uuid)))
    content = content.replace("${uuid}", ",".join(map(str, entity_uuid)))
    
    # Save
    output_path = Path(output_dir) / f"{leader_id}.npc.snbt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content)
    
    return output_path