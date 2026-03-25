# src/api.py
import json
import random
import time
import requests
from pathlib import Path

CACHE_DIR = Path("pokemon_cache")
CACHE_DIR.mkdir(exist_ok=True)

class PokeAPICache:
    def __init__(self, cache_dir="pokemon_cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
    
    def get_pokemon(self, name):
        name = name.lower()
        cache_file = self.cache_dir / f"{name}.json"
        if cache_file.exists():
            with open(cache_file) as f:
                return json.load(f)
        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
            if response.status_code == 200:
                data = response.json()
                with open(cache_file, "w") as f:
                    json.dump(data, f)
                time.sleep(0.1)
                return data
        except:
            pass
        return None
    
    def get_species(self, name):
        name = name.lower()
        cache_file = self.cache_dir / f"species_{name}.json"
        if cache_file.exists():
            with open(cache_file) as f:
                return json.load(f)
        url = f"https://pokeapi.co/api/v2/pokemon-species/{name}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                with open(cache_file, "w") as f:
                    json.dump(data, f)
                time.sleep(0.1)
                return data
        except:
            pass
        return None

api = PokeAPICache()

# Branch evolution preferences per trainer class
BRANCH_PREFERENCES = {
    "bugcatcher": {
        "wurmple": {"silcoon": 0.7, "cascoon": 0.3},
        "scyther": {"scizor": 0.8, "kleavor": 0.2},
        "nincada": {"ninjask": 0.9, "shedinja": 0.1},
    },
    "bugmaniac": {
        "wurmple": {"silcoon": 0.3, "cascoon": 0.7},
        "scyther": {"scizor": 0.5, "kleavor": 0.5},
    },
    "youngster": {
        "eevee": {"espeon": 0.4, "umbreon": 0.4, "flareon": 0.2},
    },
    "lass": {
        "eevee": {"espeon": 0.5, "sylveon": 0.4, "umbreon": 0.1},
    },
    "acetrainer": {
        "eevee": {"espeon": 0.3, "umbreon": 0.3, "sylveon": 0.2, "glaceon": 0.1, "leafeon": 0.1},
    },
    "fisher": {
        "eevee": {"vaporeon": 0.9, "umbreon": 0.1},
    },
    "hiker": {
        "eevee": {"flareon": 0.5, "leafeon": 0.5},
    },
    "psychic": {
        "eevee": {"espeon": 0.7, "sylveon": 0.3},
    },
    "blackbelt": {
        "tyrogue": {"hitmonlee": 0.4, "hitmonchan": 0.4, "hitmontop": 0.2},
    },
    "battlegirl": {
        "tyrogue": {"hitmonchan": 0.5, "hitmonlee": 0.3, "hitmontop": 0.2},
    },
}

def get_species_data(name):
    """Fetch species data from PokéAPI with caching"""
    name = name.lower()
    cache_file = CACHE_DIR / f"species_{name}.json"
    
    if cache_file.exists():
        with open(cache_file) as f:
            return json.load(f)
    
    try:
        url = f"https://pokeapi.co/api/v2/pokemon-species/{name}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            with open(cache_file, "w") as f:
                json.dump(data, f)
            time.sleep(0.05)
            return data
    except Exception as e:
        print(f"  Error fetching {name}: {e}")
    return None

def get_min_evolution_level(base_species, evolved_species, trainer_class=None):
    """Find the minimum level at which a Pokémon can evolve into its form"""
    evo_chain = get_evolution_chain(base_species)
    if not evo_chain:
        return None
    
    def find_min_level(chain, current_species, target_species):
        if chain.get("species", {}).get("name") == current_species:
            evolves_to = chain.get("evolves_to", [])
            for evo in evolves_to:
                for detail in evo.get("evolution_details", []):
                    min_level = detail.get("min_level")
                    next_species = evo["species"]["name"]
                    
                    if next_species == target_species:
                        return min_level if min_level else 1
                    
                    if min_level:
                        result = find_min_level(evo, next_species, target_species)
                        if result:
                            return result
            return None
        
        for evo in chain.get("evolves_to", []):
            result = find_min_level(evo, current_species, target_species)
            if result:
                return result
        return None
    
    return find_min_level(evo_chain["chain"], base_species, evolved_species)

def get_evolution_chain(species_name):
    print(f"  📡 Fetching evolution chain for {species_name}")
    species_data = api.get_species(species_name)
    if not species_data:
        print(f"    ❌ No species data for {species_name}")
        return None
    evo_chain_url = species_data.get("evolution_chain", {}).get("url")
    if not evo_chain_url:
        print(f"    ℹ️ {species_name} has no evolution chain URL")
        return None
    print(f"    🔗 URL: {evo_chain_url}")
    
    cache_file = api.cache_dir / f"evolution_{species_name}.json"
    if cache_file.exists():
        with open(cache_file) as f:
            data = json.load(f)
            print(f"    ✅ Loaded from cache")
            return data
    
    try:
        response = requests.get(evo_chain_url)
        if response.status_code == 200:
            data = response.json()
            with open(cache_file, "w") as f:
                json.dump(data, f)
            print(f"    ✅ Fetched and cached")
            time.sleep(0.1)
            return data
        else:
            print(f"    ❌ HTTP {response.status_code}")
    except Exception as e:
        print(f"    ❌ Error: {e}")
    return None

def get_branch_evolution(base_species, possible_evolutions, trainer_class):
    """Select a branch evolution based on trainer class preferences"""
    prefs = BRANCH_PREFERENCES.get(trainer_class, {}).get(base_species, {})
    
    if prefs:
        filtered = {k: v for k, v in prefs.items() if k in possible_evolutions}
        if filtered:
            choices = list(filtered.keys())
            weights = list(filtered.values())
            return random.choices(choices, weights=weights)[0]
    
    return random.choice(possible_evolutions)

def get_pokemon_types(species):
    """Get the types of a Pokémon from API"""
    data = api.get_pokemon(species)
    if not data:
        return ["normal"]
    types = [t["type"]["name"] for t in data.get("types", [])]
    return types

def get_evolved_form(species, level, trainer_class=None):
    """Get the evolved form based on evolution chain from API"""
    evo_chain = get_evolution_chain(species)
    if not evo_chain:
        return species
    
    def find_evolution(chain, current_species, target_level):
        if chain.get("species", {}).get("name") == current_species:
            evolves_to = chain.get("evolves_to", [])
            if not evolves_to:
                return current_species
            
            for evo in evolves_to:
                for detail in evo.get("evolution_details", []):
                    trigger = detail.get("trigger", {}).get("name")
                    min_level = detail.get("min_level")
                    held_item = detail.get("held_item", {}).get("name") if detail.get("held_item") else None
                    item = detail.get("item", {}).get("name") if detail.get("item") else None
                    known_move = detail.get("known_move", {}).get("name") if detail.get("known_move") else None
                    next_species = evo["species"]["name"]
                    
                    should_evolve = False
                    
                    if trigger == "level-up" and min_level and min_level <= target_level:
                        should_evolve = True
                    elif trigger == "trade":
                        should_evolve = True
                    elif trigger == "use-item" and item:
                        if target_level >= 30:
                            should_evolve = True
                    elif trigger == "level-up" and held_item:
                        if target_level >= 30:
                            should_evolve = True
                    elif trigger == "level-up" and known_move:
                        if target_level >= 34:
                            should_evolve = True
                    elif trigger == "shed":
                        if target_level >= 20:
                            should_evolve = True
                    
                    if should_evolve:
                        further = find_evolution(evo, next_species, target_level)
                        if further != next_species:
                            return further
                        return next_species
            
            return current_species
        
        for evo in chain.get("evolves_to", []):
            result = find_evolution(evo, current_species, target_level)
            if result != current_species:
                return result
        return current_species
    
    return find_evolution(evo_chain["chain"], species, level)

def get_moves(species, level):
    data = api.get_pokemon(species)
    if not data:
        return ["tackle"]
    moves = []
    for m in data.get("moves", []):
        for v in m.get("version_group_details", []):
            if v.get("level_learned_at", 0) <= level and v.get("move_learn_method", {}).get("name") == "level-up":
                move_name = m["move"]["name"].replace("-", "").replace("_", "")
                moves.append(move_name)
    return list(dict.fromkeys(moves))[-4:] or ["tackle"]

def get_ability(species):
    data = api.get_pokemon(species)
    if not data:
        return "normal"
    abilities = [a["ability"]["name"].replace("-", "").replace("_", "") for a in data.get("abilities", [])]
    return random.choice(abilities) if abilities else "normal"

def get_evolution_method(species):
    """Get the evolution method for a Pokémon (level, item, trade, etc.)"""
    evo_chain = get_evolution_chain(species)
    if not evo_chain:
        return None
    
    def find_evolution_step(chain, target):
        if chain.get("species", {}).get("name") == target:
            return None  # Base form
        evolves_to = chain.get("evolves_to", [])
        for evo in evolves_to:
            next_species = evo["species"]["name"]
            if next_species == target:
                return evo.get("evolution_details", [{}])[0] if evo.get("evolution_details") else None
            result = find_evolution_step(evo, target)
            if result:
                return result
        return None
    
    return find_evolution_step(evo_chain["chain"], species)

def get_best_held_item(species, rank_idx):
    """Choose a held item based on Pokémon type and rank"""
    from config import TYPE_ITEMS, UTILITY_ITEMS
    
    types = get_pokemon_types(species)
    primary_type = types[0] if types else "normal"
    
    # Type-specific items (Challenger+)
    type_data = TYPE_ITEMS.get(primary_type)
    if type_data and rank_idx >= type_data["min_rank"]:
        if random.random() < 0.6:
            return random.choice(type_data["items"])
    
    # Berries (Apprentice+)
    if rank_idx >= UTILITY_ITEMS["berries"]["min_rank"]:
        if random.random() < 0.4:
            return random.choice(UTILITY_ITEMS["berries"]["items"])
    
    # Utility items by rank
    if rank_idx >= UTILITY_ITEMS["ultra_rare"]["min_rank"]:
        if random.random() < 0.5:
            return random.choice(UTILITY_ITEMS["ultra_rare"]["items"])
    elif rank_idx >= UTILITY_ITEMS["rare"]["min_rank"]:
        if random.random() < 0.4:
            return random.choice(UTILITY_ITEMS["rare"]["items"])
    elif rank_idx >= UTILITY_ITEMS["common"]["min_rank"]:
        if random.random() < 0.3:
            return random.choice(UTILITY_ITEMS["common"]["items"])
    
    return None