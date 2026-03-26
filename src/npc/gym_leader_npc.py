# src/npc/gym_leader_npc.py
import random
from pathlib import Path
from config import GYM_LEADERS, get_gym_dialog
from src.npc.trainer_npc import generate_uuids
from src.npc.template import load_template

def generate_gym_leader_snbt(leader_id, leader_info, template_dir="source/templates", output_dir="outputs/npcs/gym_leaders"):
    """Generate an SNBT file for a gym leader"""
    name = leader_info["name"]
    skin_url = leader_info.get("skin_url", "")
    badge_id = leader_info.get("badge", "unknown")
    
    # Get teleport coordinates (battle arena positions)
    npc_x = leader_info.get("battle_position", {}).get("npc_x", 585)
    npc_y = leader_info.get("battle_position", {}).get("npc_y", 78)
    npc_z = leader_info.get("battle_position", {}).get("npc_z", 402)
    player_x = leader_info.get("battle_position", {}).get("player_x", 610)
    player_y = leader_info.get("battle_position", {}).get("player_y", 78)
    player_z = leader_info.get("battle_position", {}).get("player_z", 402)
    
    # Randomly choose between Alex and Steve models
    is_alex = random.choice([True, False])
    entity_type = "easy_npc:humanoid_slim" if is_alex else "easy_npc:humanoid"
    variant_type = "ALEX" if is_alex else "STEVE"
    
    template_path = Path(template_dir) / "base_gym_leader.snbt"
    if not template_path.exists():
        print(f"⚠️ Template not found: {template_path}")
        return None
    
    # Load template FIRST
    template = load_template(template_path)
    
    # Get dialog lines
    flavor_text = get_gym_dialog(leader_id, "flavor")
    challenge_text = get_gym_dialog(leader_id, "challenge")
    rematch_challenge_text = get_gym_dialog(leader_id, "rematch_challenge")
    
    # First badge ever flow
    victory_first_novice_1 = get_gym_dialog(leader_id, "victory_first_novice_1")
    victory_first_novice_2 = get_gym_dialog(leader_id, "victory_first_novice_2")
    
    # Rank-specific victory dialogs
    victory_first_rookie = get_gym_dialog(leader_id, "victory_first_rookie")
    victory_first_apprentice = get_gym_dialog(leader_id, "victory_first_apprentice")
    victory_first_trainer = get_gym_dialog(leader_id, "victory_first_trainer")
    victory_first_challenger = get_gym_dialog(leader_id, "victory_first_challenger")
    victory_first_pro = get_gym_dialog(leader_id, "victory_first_pro")
    victory_first_ace = get_gym_dialog(leader_id, "victory_first_ace")
    victory_first_elite = get_gym_dialog(leader_id, "victory_first_elite")
    victory_first_master = get_gym_dialog(leader_id, "victory_first_master")
    victory_first_masterstar1 = get_gym_dialog(leader_id, "victory_first_masterstar1")
    victory_first_masterstar2 = get_gym_dialog(leader_id, "victory_first_masterstar2")
    victory_first_masterstar3 = get_gym_dialog(leader_id, "victory_first_masterstar3")
    
    # Common ending
    victory_first_end = get_gym_dialog(leader_id, "victory_first_end")
    
    # Rematch and other dialogs
    victory_rematch_text = get_gym_dialog(leader_id, "victory_rematch")
    defeat_text = get_gym_dialog(leader_id, "defeat")
    rematch_cooldown_text = get_gym_dialog(leader_id, "rematch_cooldown")
    
    # Generate UUIDs
    owner_uuid = generate_uuids()
    preset_uuid = generate_uuids()
    entity_uuid = generate_uuids()
    
    # Start with template content
    content = template
    
    # Replace placeholders
    content = content.replace("${entity_type}", entity_type)
    content = content.replace("${variant_type}", variant_type)
    content = content.replace("${name}", name)
    content = content.replace("${leader_id}", leader_id)
    content = content.replace("${badge_id}", badge_id)
    
    # Basic dialogs
    content = content.replace("${flavor_dialog}", flavor_text)
    content = content.replace("${challenge_dialog}", challenge_text)
    content = content.replace("${rematch_challenge_dialog}", rematch_challenge_text)
    
    # First badge ever flow
    content = content.replace("${victory_first_novice_1}", victory_first_novice_1)
    content = content.replace("${victory_first_novice_2}", victory_first_novice_2)
    
    # Rank-specific victory dialogs
    content = content.replace("${victory_first_rookie}", victory_first_rookie)
    content = content.replace("${victory_first_apprentice}", victory_first_apprentice)
    content = content.replace("${victory_first_trainer}", victory_first_trainer)
    content = content.replace("${victory_first_challenger}", victory_first_challenger)
    content = content.replace("${victory_first_pro}", victory_first_pro)
    content = content.replace("${victory_first_ace}", victory_first_ace)
    content = content.replace("${victory_first_elite}", victory_first_elite)
    content = content.replace("${victory_first_master}", victory_first_master)
    content = content.replace("${victory_first_masterstar1}", victory_first_masterstar1)
    content = content.replace("${victory_first_masterstar2}", victory_first_masterstar2)
    content = content.replace("${victory_first_masterstar3}", victory_first_masterstar3)
    
    # Common ending
    content = content.replace("${victory_first_end}", victory_first_end)
    
    # Rematch and other dialogs
    content = content.replace("${victory_rematch_dialog}", victory_rematch_text)
    content = content.replace("${defeat_dialog}", defeat_text)
    content = content.replace("${rematch_cooldown_dialog}", rematch_cooldown_text)
    
    # Position and UUIDs
    content = content.replace("${skin_url}", skin_url)
    content = content.replace("${npc_x}", str(npc_x))
    content = content.replace("${npc_y}", str(npc_y))
    content = content.replace("${npc_z}", str(npc_z))
    content = content.replace("${player_x}", str(player_x))
    content = content.replace("${player_y}", str(player_y))
    content = content.replace("${player_z}", str(player_z))
    content = content.replace("${owner_uuid}", ",".join(map(str, owner_uuid)))
    content = content.replace("${preset_uuid}", ",".join(map(str, preset_uuid)))
    content = content.replace("${uuid}", ",".join(map(str, entity_uuid)))
    
    output_path = Path(output_dir) / f"{leader_id}.npc.snbt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content)
    
    return output_path

def generate_all_gym_leaders(template_dir="source/templates", output_dir="outputs/npcs/gym_leaders"):
    """Generate NPC files for all gym leaders"""
    from config import GYM_LEADERS
    
    print(f"\n📝 Found {len(GYM_LEADERS)} gym leaders:")
    for leader_id, info in GYM_LEADERS.items():
        print(f"   - {info['name']} ({leader_id}) - {info['badge']} badge")
    
    print(f"\n🎲 Generating Gym Leader SNBT files...")
    
    generated = 0
    for leader_id, info in GYM_LEADERS.items():
        output_path = generate_gym_leader_snbt(leader_id, info, template_dir, output_dir)
        if output_path:
            print(f"✓ Generated: {output_path}")
            generated += 1
    
    print(f"\n✅ Generated {generated} gym leader files in {output_dir}/")
    return generated