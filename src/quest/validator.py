"""Validate quest definitions"""
from .parser import QuestParser

class QuestValidator:
    def __init__(self):
        self.parser = QuestParser()
        self.errors = []
        self.warnings = []
    
    def validate_all(self):
        """Validate all quest definitions"""
        quests = self.parser.parse_all()
        
        if not quests:
            print("No quests found to validate")
            return False
        
        print(f"\n📋 Validating {len(quests)} quests...")
        
        for quest in quests:
            self.validate_quest(quest)
        
        print(f"\n✅ Validation complete: {len(self.errors)} errors, {len(self.warnings)} warnings")
        
        for error in self.errors:
            print(f"  ✗ {error}")
        for warning in self.warnings:
            print(f"  ⚠ {warning}")
        
        return len(self.errors) == 0
    
    def validate_quest(self, quest):
        """Validate a single quest"""
        quest_id = quest.get('id')
        if not quest_id:
            self.errors.append("Quest missing 'id' field")
            return
        
        # Check required fields
        if not quest.get('name'):
            self.errors.append(f"Quest {quest_id} missing 'name'")
        
        if not quest.get('stages'):
            self.errors.append(f"Quest {quest_id} has no stages")
            return
        
        # Validate stages
        stages = quest['stages']
        for stage_num, stage in stages.items():
            if not stage.get('name'):
                self.warnings.append(f"Quest {quest_id}, stage {stage_num} missing 'name'")
            
            if stage.get('condition') and stage.get('dialog'):
                self.warnings.append(f"Quest {quest_id}, stage {stage_num} has both condition and dialog")
        
        print(f"  ✓ {quest_id}: {quest['name']}")
