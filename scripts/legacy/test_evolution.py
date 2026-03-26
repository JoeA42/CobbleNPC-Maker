# test_evolution.py
import json
import time
import requests
from pathlib import Path

class QuickAPITest:
    def __init__(self):
        self.cache_dir = Path("pokemon_cache")
        self.cache_dir.mkdir(exist_ok=True)
    
    def get_species(self, name):
        name = name.lower()
        cache_file = self.cache_dir / f"species_{name}.json"
        if cache_file.exists():
            with open(cache_file) as f:
                return json.load(f)
        url = f"https://pokeapi.co/api/v2/pokemon-species/{name}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            with open(cache_file, "w") as f:
                json.dump(data, f)
            time.sleep(0.1)
            return data
        return None
    
    def get_evolution_chain(self, species_name):
        species_data = self.get_species(species_name)
        if not species_data:
            print(f"  ❌ Could not get species data for {species_name}")
            return None
        evo_chain_url = species_data.get("evolution_chain", {}).get("url")
        if not evo_chain_url:
            print(f"  ℹ️ {species_name} has no evolution chain")
            return None
        cache_file = self.cache_dir / f"evolution_{species_name}.json"
        if cache_file.exists():
            with open(cache_file) as f:
                return json.load(f)
        response = requests.get(evo_chain_url)
        if response.status_code == 200:
            data = response.json()
            with open(cache_file, "w") as f:
                json.dump(data, f)
            time.sleep(0.1)
            return data
        return None
    
    def print_evolution_path(self, species, target_level):
        print(f"\n📊 Analyzing {species} at level {target_level}")
        print("-" * 40)
        
        evo_chain = self.get_evolution_chain(species)
        if not evo_chain:
            print(f"  {species} does not evolve")
            return
        
        def find_evolutions(chain, current_species, target_level, depth=0):
            indent = "  " * depth
            if chain.get("species", {}).get("name") == current_species:
                evolves_to = chain.get("evolves_to", [])
                if not evolves_to:
                    print(f"{indent}✓ {current_species} (final form)")
                    return current_species
                
                print(f"{indent}🔍 {current_species} can evolve into:")
                valid = []
                for evo in evolves_to:
                    for detail in evo.get("evolution_details", []):
                        min_level = detail.get("min_level")
                        item = detail.get("item")
                        trade = detail.get("trade_species")
                        happiness = detail.get("min_happiness")
                        
                        condition = []
                        if min_level:
                            condition.append(f"Level {min_level}")
                        if item:
                            condition.append(f"Item {item['name']}")
                        if trade:
                            condition.append("Trade")
                        if happiness:
                            condition.append(f"Happiness {happiness}")
                        
                        condition_str = " + ".join(condition) if condition else "Other condition"
                        next_species = evo["species"]["name"]
                        
                        can_evolve = False
                        if min_level and min_level <= target_level:
                            can_evolve = True
                        elif item and target_level >= 30:
                            can_evolve = True
                        elif trade and target_level >= 30:
                            can_evolve = True
                        elif happiness and target_level >= 20:
                            can_evolve = True
                        
                        status = "✅" if can_evolve else "⏳"
                        print(f"{indent}  {status} {next_species} ({condition_str})")
                        
                        if can_evolve:
                            valid.append((evo, next_species))
                
                if valid:
                    print(f"{indent}➡️ Will evolve at this level")
                    for evo, next_species in valid:
                        find_evolutions(evo, next_species, target_level, depth + 1)
                else:
                    print(f"{indent}⏳ Will not evolve yet (needs higher level)")
                return
            
            for evo in chain.get("evolves_to", []):
                find_evolutions(evo, current_species, target_level, depth)
        
        find_evolutions(evo_chain, species, target_level)

# Test specific Pokémon
api = QuickAPITest()

print("\n" + "=" * 60)
print("TESTING EVOLUTION PATHS")
print("=" * 60)

# Test Pokémon with different evolution types
test_pokemon = [
    ("caterpie", 12),
    ("caterpie", 30),
    ("nincada", 25),
    ("nincada", 45),
    ("scyther", 35),
    ("scyther", 50),
    ("yanma", 35),
    ("wurmple", 10),
    ("eevee", 25),
    ("eevee", 40),
]

for species, level in test_pokemon:
    api.print_evolution_path(species, level)

print("\n" + "=" * 60)
print("Test complete!")