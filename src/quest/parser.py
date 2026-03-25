"""Quest Parser - Placeholder"""
import yaml
from pathlib import Path

class QuestParser:
    def __init__(self, quests_dir="config/quests"):
        self.quests_dir = Path(quests_dir)
    
    def parse_all(self):
        quests = []
        if self.quests_dir.exists():
            for yaml_file in self.quests_dir.glob("*.yaml"):
                with open(yaml_file) as f:
                    quests.append(yaml.safe_load(f))
        return quests
    
    def parse_quest(self, quest_id):
        quest_file = self.quests_dir / f"{quest_id}.yaml"
        if quest_file.exists():
            with open(quest_file) as f:
                return yaml.safe_load(f)
        return None
