# fix_held_items.py
import json
from pathlib import Path

# Base trainers directory
trainers_base = Path("trainers")

print("=" * 60)
print("FIXING HELD ITEMS IN ALL TRAINER FILES")
print("=" * 60)

# Find all JSON files in trainers folder recursively
trainer_files = list(trainers_base.rglob("*.json"))

if not trainer_files:
    print("No trainer files found!")
    exit()

print(f"Found {len(trainer_files)} trainer files\n")

fixed_count = 0

for file in trainer_files:
    try:
        with open(file, "r") as f:
            trainer = json.load(f)
        
        modified = False
        for pokemon in trainer.get("team", []):
            if "heldItem" in pokemon and pokemon["heldItem"] is None:
                del pokemon["heldItem"]
                modified = True
                print(f"  Removed null held item from {file.relative_to(trainers_base)}")
        
        if modified:
            with open(file, "w") as f:
                json.dump(trainer, f, indent=4)
            fixed_count += 1
    except Exception as e:
        print(f"✗ Error processing {file.name}: {e}")

print(f"\n✅ Done! Fixed {fixed_count} files.")