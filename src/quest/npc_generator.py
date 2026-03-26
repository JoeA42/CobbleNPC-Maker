"""Generate SNBT files for quest NPCs"""
import json
import random
from pathlib import Path
from src.npc.template import load_template, generate_uuids

class QuestNPCGenerator:
    def __init__(self, output_dir="outputs/npcs/quests"):
        self.output_dir = Path(output_dir)
        self.template_path = Path("templates/base_quest_npc.snbt")
    
    def generate_npc(self, npc_config, quest_id):
        """Generate SNBT for a quest NPC"""
        if not self.template_path.exists():
            print(f"⚠️ Template not found: {self.template_path}")
            return None
        
        template = load_template(self.template_path)
        
        npc_id = npc_config.get('id')
        npc_name = npc_config.get('name', npc_id.capitalize())
        npc_role = npc_config.get('role', 'generic')
        
        # Generate UUIDs
        owner_uuid = generate_uuids()
        preset_uuid = generate_uuids()
        entity_uuid = generate_uuids()
        
        # Random model choice
        is_alex = random.choice([True, False])
        entity_type = "easy_npc:humanoid_slim" if is_alex else "easy_npc:humanoid"
        variant_type = "ALEX" if is_alex else "STEVE"
        
        # Build dialog dataset for this quest NPC
        dialogs = self.build_dialogs(npc_config, quest_id)
        
        # Replace placeholders
        content = template
        content = content.replace("${entity_type}", entity_type)
        content = content.replace("${variant_type}", variant_type)
        content = content.replace("${name}", npc_name)
        content = content.replace("${npc_id}", npc_id)
        content = content.replace("${quest_id}", quest_id)
        content = content.replace("${dialogs}", json.dumps(dialogs, indent=2))
        content = content.replace("${owner_uuid}", ",".join(map(str, owner_uuid)))
        content = content.replace("${preset_uuid}", ",".join(map(str, preset_uuid)))
        content = content.replace("${uuid}", ",".join(map(str, entity_uuid)))
        
        # Save
        output_path = self.output_dir / f"{quest_id}_{npc_id}.npc.snbt"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content)
        
        return output_path
    
    def build_dialogs(self, npc_config, quest_id):
        """Build dialog dataset for this NPC"""
        # This will be expanded later
        return [
            {
                "Buttons": [{
                    "Actions": [{"Type": "CLOSE_DIALOG"}],
                    "Name": "Close"
                }],
                "Name": "default",
                "Texts": [{"Text": "Hello!"}]
            }
        ]
    
    def generate_all_npcs(self, quest):
        """Generate all NPCs for a quest"""
        generated = []
        for npc_config in quest.get('npcs', []):
            output = self.generate_npc(npc_config, quest['id'])
            if output:
                generated.append(output)
                print(f"  ✓ Generated NPC: {npc_config.get('id')}")
        return generated
