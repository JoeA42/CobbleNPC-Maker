# src/utils/file_utils.py
import json

def fix_held_items_in_files(filepaths):
    """Remove null heldItem entries from trainer JSON files"""
    for filepath in filepaths:
        try:
            with open(filepath, "r") as f:
                trainer = json.load(f)
            
            modified = False
            for pokemon in trainer.get("team", []):
                if "heldItem" in pokemon and pokemon["heldItem"] is None:
                    del pokemon["heldItem"]
                    modified = True
            
            if modified:
                with open(filepath, "w") as f:
                    json.dump(trainer, f, indent=4)
                print(f"   ✓ Cleaned held items in: {filepath.name}")
        except Exception as e:
            print(f"   ⚠️ Error cleaning {filepath.name}: {e}")