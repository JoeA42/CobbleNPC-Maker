# src/utils/toml_updater.py

"""Update tbcs-server.toml with trainer paths"""
from pathlib import Path
import re

class TOMLUpdater:
    def __init__(self, world_path):
        # The config is in DATA_PATH/config/, not WORLD_PATH.parent.parent
        # world_path: /home/jose/.../world
        # data_path: /home/jose/.../MCData (world.parent)
        # config_path: data_path / "config" / "tbcs-server.toml"
        self.data_path = world_path.parent  # This is MCData
        self.toml_path = self.data_path / "config" / "tbcs-server.toml"
        self.trainer_paths = []
        print(f"Looking for TOML at: {self.toml_path}")  # Debug print
    
    def load_current_paths(self):
        """Load existing trainer paths from TOML file"""
        if not self.toml_path.exists():
            print(f"⚠️ TOML file not found: {self.toml_path}")
            return []
        
        with open(self.toml_path, 'r') as f:
            content = f.read()
        
        # Find trainerPaths section
        pattern = r'trainerPaths\s*=\s*\[([^\]]+)\]'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            paths_str = match.group(1)
            # Parse paths
            paths = re.findall(r'"([^"]+)"', paths_str)
            return paths
        return []
    
    def generate_paths_from_config(self, game_data):
        """Generate trainer paths from game_data"""
        paths = []
        
        # Add regular trainer paths for each folder and subclasses
        for folder, subclasses in game_data.FOLDERS.items():
            # Add the main folder path
            paths.append(f"trainers/regular/{folder}")
            
            # Add individual subclass paths
            for subclass in subclasses:
                paths.append(f"trainers/regular/{folder}/{subclass}")
        
        # Add gym leader paths
        for leader_id in game_data.GYM_LEADERS.keys():
            paths.append(f"trainers/leaders/{leader_id}")
        
        # Add fallback paths
        paths.extend(["trainers", "../trainers", "../../trainers"])
        
        # Remove duplicates while preserving order
        seen = set()
        unique_paths = []
        for path in paths:
            if path not in seen:
                seen.add(path)
                unique_paths.append(path)
        
        return unique_paths
    
    def update_toml(self, game_data):
        """Update the TOML file with current trainer paths"""
        if not self.toml_path.exists():
            print(f"❌ TOML file not found: {self.toml_path}")
            print("   Make sure the server path is correct in export_menu")
            return False
        
        # Load current paths
        current_paths = self.load_current_paths()
        new_paths = self.generate_paths_from_config(game_data)
        
        # Compare
        if set(current_paths) == set(new_paths):
            print("✅ Trainer paths are already up to date")
            return True
        
        print("\n📝 Trainer paths need updating:")
        print("   Current paths:")
        for p in current_paths:
            print(f"     - {p}")
        print("\n   New paths:")
        for p in new_paths:
            print(f"     - {p}")
        
        confirm = input("\nUpdate tbcs-server.toml? (y/n): ").strip().lower()
        if confirm != 'y':
            print("❌ Update cancelled")
            return False
        
        # Read the file
        with open(self.toml_path, 'r') as f:
            content = f.read()
        
        # Create new trainerPaths section
        paths_lines = ['trainerPaths = [']
        for path in new_paths:
            paths_lines.append(f'\t"{path}",')
        paths_lines.append('\t]')
        new_paths_section = '\n'.join(paths_lines)
        
        # Replace the trainerPaths section
        pattern = r'trainerPaths\s*=\s*\[[^\]]+\]'
        new_content = re.sub(pattern, new_paths_section, content, flags=re.DOTALL)
        
        # Write back
        with open(self.toml_path, 'w') as f:
            f.write(new_content)
        
        print(f"\n✅ Updated {self.toml_path}")
        print("   Remember to reload the server or restart for changes to take effect")
        return True
    
    def show_diff(self, game_data):
        """Show differences without updating"""
        current_paths = self.load_current_paths()
        new_paths = self.generate_paths_from_config(game_data)
        
        print("\n📊 Trainer Paths Comparison:")
        print("\nCurrent paths in TOML:")
        if current_paths:
            for p in current_paths:
                print(f"   - {p}")
        else:
            print("   (No paths found - TOML file may be missing or empty)")
        
        print("\nPaths from game_data:")
        for p in new_paths:
            print(f"   - {p}")
        
        missing = set(new_paths) - set(current_paths)
        extra = set(current_paths) - set(new_paths)
        
        if missing:
            print("\n❌ Missing paths (need to add):")
            for p in missing:
                print(f"   - {p}")
        if extra:
            print("\n➕ Extra paths (can be removed):")
            for p in extra:
                print(f"   - {p}")
        if not missing and not extra:
            print("\n✅ Paths are in sync!")