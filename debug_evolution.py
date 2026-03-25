# debug_evolution.py
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
    
    def print_raw_evolution_data(self, species_name):
        """Print the raw JSON from the evolution chain"""
        print(f"\n📦 RAW EVOLUTION DATA for {species_name}")
        print("=" * 60)
        
        evo_chain = self.get_evolution_chain(species_name)
        if not evo_chain:
            print("  No evolution chain found")
            return
        
        print(json.dumps(evo_chain, indent=2, default=str))
        print("=" * 60)

api = QuickAPITest()

# Test Pokémon that should evolve
test_species = ["yanma", "scyther", "nincada", "caterpie"]

for species in test_species:
    api.print_raw_evolution_data(species)