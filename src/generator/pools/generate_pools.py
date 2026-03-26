#!/usr/bin/env python3
# generate_pools.py - Run this once to generate expanded Pokémon pools

import json
import random
import time
import requests
from pathlib import Path

# Pokémon types that fit each class
CLASS_TYPES = {
    "bug_catcher": ["bug"],
    "bug_maniac": ["bug"],
    "bug_collector": ["bug"],
    "youngster": ["normal"],
    "lass": ["normal", "fairy"],
    "school_kid": ["normal", "psychic"],
    "fisherman": ["water"],
    "fisherwoman": ["water"],
    "hiker": ["rock", "ground"],
    "mountaineer": ["rock", "ground", "ice"],
    "backpacker": ["normal", "rock", "ground"],
    "scientist": ["electric", "steel", "psychic"],
    "researcher": ["psychic", "normal"],
    "engineer": ["electric", "steel"],
    "beauty": ["water", "grass", "fairy"],
    "lady": ["normal", "fairy"],
    "rich_boy": ["normal", "dragon", "psychic"],
    "biker": ["poison", "dark"],
    "roughneck": ["dark", "fighting"],
    "punk": ["dark", "poison"],
    "psychic": ["psychic"],
    "medium": ["ghost", "psychic"],
    "channeler": ["ghost"],
    "black_belt": ["fighting"],
    "battle_girl": ["fighting"],
    "expert": ["fighting", "psychic"],
    "ranger": ["normal", "grass", "flying"],
    "park_ranger": ["grass", "bug"],
    "camper": ["normal", "rock", "ground"],
    "hex_maniac": ["ghost", "dark"],
    "fairy_tale_girl": ["fairy"],
    "dragon_tamer": ["dragon"],
    "firebreather": ["fire"],
    "swimmer_m": ["water"],
    "swimmer_f": ["water"],
    "tuber_m": ["water"],
    "tuber_f": ["water"],
    "bird_keeper": ["flying"],
    "firefighter": ["fire", "water"],  
    "electrician": ["electric", "steel"],
    "miner": ["rock", "ground", "steel"],
    "skier": ["ice", "flying"],  
    "ninja": ["poison", "dark", "fighting"],
    "wanderer": ["fire", "ice", "ground"]
}

# Legendary/mythical Pokémon to exclude
LEGENDARIES = {
    "mew", "mewtwo", "lugia", "ho-oh", "celebi", "kyogre", "groudon", "rayquaza",
    "jirachi", "deoxys", "dialga", "palkia", "giratina", "manaphy", "phione",
    "darkrai", "shaymin", "arceus", "victini", "reshiram", "zekrom", "kyurem",
    "genesect", "xerneas", "yveltal", "zygarde", "diancie", "hoopa", "volcanion",
    "cosmog", "cosmoem", "solgaleo", "lunala", "nihilego", "buzzwole", "pheromosa",
    "xurkitree", "celesteela", "kartana", "guzzlord", "necrozma", "magearna",
    "marshadow", "poipole", "naganadel", "stakataka", "blacephalon", "zacian",
    "zamazenta", "eternatus", "calyrex"
}

def get_pokemon_by_type(pokemon_type):
    """Fetch all Pokémon of a specific type from PokéAPI"""
    url = f"https://pokeapi.co/api/v2/type/{pokemon_type}"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    
    data = response.json()
    pokemon_list = []
    for entry in data["pokemon"]:
        name = entry["pokemon"]["name"]
        # Skip legendaries and forms
        if name not in LEGENDARIES and "-" not in name:
            pokemon_list.append(name)
        time.sleep(0.05)
    
    return list(set(pokemon_list))

def get_pokemon_data(name):
    """Get Pokémon data including catch rate"""
    try:
        url = f"https://pokeapi.co/api/v2/pokemon-species/{name}"
        response = requests.get(url)
        if response.status_code != 200:
            return None
        
        data = response.json()
        return {
            "name": name,
            "catch_rate": data.get("capture_rate", 255),
            "evolution_chain": data.get("evolution_chain", {}).get("url")
        }
    except:
        return None

def get_base_evolution(name):
    """Get the base form of a Pokémon"""
    try:
        url = f"https://pokeapi.co/api/v2/pokemon-species/{name}"
        response = requests.get(url)
        if response.status_code != 200:
            return name
        
        data = response.json()
        chain_url = data.get("evolution_chain", {}).get("url")
        if not chain_url:
            return name
        
        response = requests.get(chain_url)
        if response.status_code != 200:
            return name
        
        chain = response.json()
        
        def find_base(chain_data):
            if not chain_data.get("evolves_to"):
                return chain_data["species"]["name"]
            return find_base(chain_data["evolves_to"][0])
        
        base = find_base(chain["chain"])
        return base
    except:
        return name

def generate_pool(class_name, types):
    """Generate a Pokémon pool for a class with rarity based on catch rate"""
    all_pokemon = []
    
    for t in types:
        if t == "any":
            # For "any", get from multiple types
            any_types = ["normal", "fire", "water", "grass", "electric", "psychic", "fighting", "dark", "dragon"]
            for any_type in any_types:
                pokemon = get_pokemon_by_type(any_type)
                all_pokemon.extend(pokemon)
        else:
            pokemon = get_pokemon_by_type(t)
            all_pokemon.extend(pokemon)
    
    # Remove duplicates
    all_pokemon = list(set(all_pokemon))
    
    # Get base forms with catch rates
    pokemon_data = []
    print(f"  Fetching catch rates for {class_name}...")
    for pokemon in all_pokemon:
        base = get_base_evolution(pokemon)
        if base not in [p["name"] for p in pokemon_data]:
            data = get_pokemon_data(base)
            if data:
                pokemon_data.append(data)
        time.sleep(0.05)
    
    # Sort by catch rate (higher catch rate = easier to catch = more common)
    # Catch rates: 255 (very common) to 3 (very rare)
    pokemon_data.sort(key=lambda x: x["catch_rate"], reverse=True)
    
    # Split into rarity tiers based on catch rate
    total = len(pokemon_data)
    common_cutoff = total // 2
    uncommon_cutoff = total * 3 // 4
    rare_cutoff = total * 7 // 8
    
    common = [p["name"] for p in pokemon_data[:common_cutoff]]
    uncommon = [p["name"] for p in pokemon_data[common_cutoff:uncommon_cutoff]]
    rare = [p["name"] for p in pokemon_data[uncommon_cutoff:rare_cutoff]]
    ultra_rare = [p["name"] for p in pokemon_data[rare_cutoff:]]
    
    # Ensure each tier has at least some Pokémon
    if len(rare) < 3:
        rare.extend(uncommon[-3:])
        uncommon = uncommon[:-3]
    if len(ultra_rare) < 2:
        ultra_rare.extend(rare[-2:])
        rare = rare[:-2]
    
    return {
        "common": common,
        "uncommon": uncommon,
        "rare": rare,
        "ultra_rare": ultra_rare
    }

def main():
    print("=" * 60)
    print("GENERATING EXPANDED POKÉMON POOLS (by catch rate)")
    print("=" * 60)
    print("This will take a few minutes...\n")
    
    expanded_pools = {}
    
    for class_name, types in CLASS_TYPES.items():
        print(f"Generating pool for {class_name}...")
        expanded_pools[class_name] = generate_pool(class_name, types)
        print(f"  ✓ {len(expanded_pools[class_name]['common'])} common, "
              f"{len(expanded_pools[class_name]['uncommon'])} uncommon, "
              f"{len(expanded_pools[class_name]['rare'])} rare, "
              f"{len(expanded_pools[class_name]['ultra_rare'])} ultra-rare")
        
        # Save after each class (in case of interruption)
        with open("expanded_pools_progress.json", "w") as f:
            json.dump(expanded_pools, f, indent=2)
        print(f"  💾 Saved progress to expanded_pools_progress.json")
    
    # Final save
    output_file = "config/pokemon_pools.json"
    with open(output_file, "w") as f:
        json.dump(expanded_pools, f, indent=2)
    
    print(f"\n✅ Done! Saved to {output_file}")
    print(f"\nCopy the POKEMON_POOLS dictionary from this file into your config.py")

if __name__ == "__main__":
    main()