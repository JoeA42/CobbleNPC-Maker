"""Parse YAML quest definitions"""
import yaml
from pathlib import Path

class QuestParser:
    def __init__(self, quests_dir="config/quests"):
        self.quests_dir = Path(quests_dir)
    
    def parse_all(self):
        """Parse all quest YAML files"""
        quests = []
        if not self.quests_dir.exists():
            return quests
        
        for yaml_file in self.quests_dir.glob("*.yaml"):
            try:
                with open(yaml_file, 'r', encoding='utf-8') as f:
                    quest = yaml.safe_load(f)
                    if quest:
                        quests.append(quest)
                        print(f"  ✓ Loaded quest: {quest.get('id', 'unknown')}")
            except Exception as e:
                print(f"  ✗ Error loading {yaml_file}: {e}")
        
        return quests
    
    def parse_quest(self, quest_id):
        """Parse a single quest by ID"""
        quest_file = self.quests_dir / f"{quest_id}.yaml"
        if quest_file.exists():
            try:
                with open(quest_file, 'r', encoding='utf-8') as f:
                    return yaml.safe_load(f)
            except Exception as e:
                print(f"Error loading {quest_file}: {e}")
        return None
