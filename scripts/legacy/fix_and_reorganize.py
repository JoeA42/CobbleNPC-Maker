#!/usr/bin/env python3
"""
reorganize_pools_v2.py - Better reorganization preserving evolution lines
"""

import json
import time
import requests
from pathlib import Path
from collections import defaultdict

CACHE_DIR = Path("pokemon_cache")
CACHE_DIR.mkdir(exist_ok=True)

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

def get_evolution_family(species_name):
    """Get the base form and all evolutions in a family"""
    # Get base form
    species_data = get_species_data(species_name)
    if not species_data:
        return [species_name]
    
    # Find base form by traversing backwards
    current = species_name
    while species_data.get("evolves_from_species"):
        prev = species_data["evolves_from_species"]["name"]
        species_data = get_species_data(prev)
        if not species_data:
            break
        current = prev
    
    base_form = current
    
    # Now get evolution chain to find all forms
    evo_chain = get_evolution_chain(base_form)
    if not evo_chain:
        return [base_form]
    
    family = [base_form]
    
    def collect_evolutions(chain):
        for evo in chain.get("evolves_to", []):
            family.append(evo["species"]["name"])
            collect_evolutions(evo)
    
    collect_evolutions(evo_chain["chain"])
    return list(set(family))

def get_evolution_chain(species_name):
    """Get evolution chain data"""
    species_data = get_species_data(species_name)
    if not species_data:
        return None
    
    evo_chain_url = species_data.get("evolution_chain", {}).get("url")
    if not evo_chain_url:
        return None
    
    cache_file = CACHE_DIR / f"evolution_{species_name}.json"
    if cache_file.exists():
        with open(cache_file) as f:
            return json.load(f)
    
    try:
        response = requests.get(evo_chain_url)
        if response.status_code == 200:
            data = response.json()
            with open(cache_file, "w") as f:
                json.dump(data, f)
            time.sleep(0.05)
            return data
    except:
        pass
    return None

def get_evolution_stage(species_name, base_form):
    """Determine evolution stage (0=base, 1=first evo, etc.)"""
    if species_name == base_form:
        return 0
    
    # Count evolutions from base form
    stage = 1
    current = base_form
    max_stage = 5
    
    for _ in range(max_stage):
        # Find next evolution (simplified - in practice we'd traverse the chain)
        # For now, just increment
        stage += 1
        # This is a simplification - in reality we'd follow the evolution chain
    
    return stage

def reorganize_pool(pool_data, class_name):
    """Reorganize preserving evolution lines"""
    # Collect all Pokémon from all tiers
    all_pokemon = set()
    for tier in ["common", "uncommon", "rare", "ultra_rare"]:
        all_pokemon.update(pool_data.get(tier, []))
    
    # Group by evolution family
    families = {}
    for pokemon in all_pokemon:
        base = get_base_form(pokemon)
        if base not in families:
            families[base] = set()
        families[base].add(pokemon)
    
    # For each family, assign members to tiers
    new_common = []
    new_uncommon = []
    new_rare = []
    new_ultra_rare = []
    
    for base, members in families.items():
        # Add base form to common
        new_common.append(base)
        
        # Add evolved forms to appropriate tiers
        evolved = [m for m in members if m != base]
        
        # Distribute evolved forms across tiers
        for i, evo in enumerate(evolved):
            if i == 0:
                new_uncommon.append(evo)
            elif i == 1:
                new_rare.append(evo)
            else:
                new_ultra_rare.append(evo)
    
    # Ensure we have enough variety by adding back any missing Pokémon
    # that might have been removed
    original_common = set(pool_data.get("common", []))
    original_all = set()
    for tier in ["common", "uncommon", "rare", "ultra_rare"]:
        original_all.update(pool_data.get(tier, []))
    
    # Add any missing base forms to common
    for pokemon in original_all:
        base = get_base_form(pokemon)
        if base not in new_common:
            new_common.append(base)
    
    # Add any missing evolved forms to appropriate tiers
    for pokemon in original_all:
        base = get_base_form(pokemon)
        if pokemon == base:
            continue
        if pokemon not in new_uncommon and pokemon not in new_rare and pokemon not in new_ultra_rare:
            # Add to appropriate tier
            new_uncommon.append(pokemon)
    
    # Remove duplicates
    new_common = list(set(new_common))
    new_uncommon = list(set(new_uncommon))
    new_rare = list(set(new_rare))
    new_ultra_rare = list(set(new_ultra_rare))
    
    # Trim to reasonable sizes (keep original counts as guideline)
    orig_sizes = {
        "common": len(pool_data.get("common", [])),
        "uncommon": len(pool_data.get("uncommon", [])),
        "rare": len(pool_data.get("rare", [])),
        "ultra_rare": len(pool_data.get("ultra_rare", []))
    }
    
    # If we have too few, add more
    if len(new_common) < orig_sizes["common"]:
        # Add more base forms from original
        extras = [p for p in original_common if p not in new_common]
        new_common.extend(extras[:orig_sizes["common"] - len(new_common)])
    
    return {
        "common": new_common[:orig_sizes["common"]],
        "uncommon": new_uncommon[:orig_sizes["uncommon"]],
        "rare": new_rare[:orig_sizes["rare"]],
        "ultra_rare": new_ultra_rare[:orig_sizes["ultra_rare"]]
    }

def get_base_form(species_name):
    """Get the base form of a Pokémon"""
    try:
        species_data = get_species_data(species_name)
        if not species_data:
            return species_name
        
        current = species_name
        while species_data.get("evolves_from_species"):
            prev = species_data["evolves_from_species"]["name"]
            species_data = get_species_data(prev)
            if not species_data:
                break
            current = prev
        
        return current
    except:
        return species_name

def main():
    print("=" * 60)
    print("REORGANIZING POKÉMON POOLS (Preserving Evolution Lines)")
    print("=" * 60)
    
    # Load the cleaned pools
    input_file = "cleaned_pools.json"
    with open(input_file, "r") as f:
        pools = json.load(f)
    
    print(f"Loaded {len(pools)} classes")
    
    # Reorganize each class
    reorganized_pools = {}
    
    for class_name, pool_data in pools.items():
        print(f"\nProcessing {class_name}...")
        reorganized_pools[class_name] = reorganize_pool(pool_data, class_name)
        
        print(f"  Common: {len(reorganized_pools[class_name]['common'])}")
        print(f"  Uncommon: {len(reorganized_pools[class_name]['uncommon'])}")
        print(f"  Rare: {len(reorganized_pools[class_name]['rare'])}")
        print(f"  Ultra Rare: {len(reorganized_pools[class_name]['ultra_rare'])}")
    
    # Save
    with open("reorganized_pools_v2.json", "w") as f:
        json.dump(reorganized_pools, f, indent=2)
    
    print(f"\n✅ Saved to reorganized_pools_v2.json")

if __name__ == "__main__":
    main()