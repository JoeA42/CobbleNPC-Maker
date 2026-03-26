#!/usr/bin/env python3
"""
complete_evolution_lines.py - Add missing evolution stages to pools
"""

import json
import time
import requests
from pathlib import Path
from collections import defaultdict

CACHE_DIR = Path("pokemon_cache")
CACHE_DIR.mkdir(exist_ok=True)

def get_evolution_chain(species_name):
    """Get the full evolution chain for a Pokémon"""
    try:
        # Get species data first
        species_data = get_species_data(species_name)
        if not species_data:
            return None
        
        # Get evolution chain URL
        evo_chain_url = species_data.get("evolution_chain", {}).get("url")
        if not evo_chain_url:
            return None
        
        # Check cache
        cache_file = CACHE_DIR / f"evolution_{species_name}.json"
        if cache_file.exists():
            with open(cache_file) as f:
                return json.load(f)
        
        # Fetch evolution chain
        response = requests.get(evo_chain_url)
        if response.status_code == 200:
            data = response.json()
            with open(cache_file, "w") as f:
                json.dump(data, f)
            time.sleep(0.05)
            return data
    except Exception as e:
        print(f"  Error fetching evolution chain for {species_name}: {e}")
    return None

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

def get_all_evolution_stages(species_name):
    """Get all stages in an evolution line (base, stage1, stage2, etc.)"""
    evo_chain = get_evolution_chain(species_name)
    if not evo_chain:
        return [species_name]
    
    stages = []
    
    def traverse(chain, current_stage=0):
        species = chain.get("species", {}).get("name")
        if species:
            stages.append((species, current_stage))
        
        for evo in chain.get("evolves_to", []):
            traverse(evo, current_stage + 1)
    
    traverse(evo_chain["chain"])
    
    # If we got multiple stages, return them, otherwise just the original
    if len(stages) > 1:
        return [s[0] for s in stages]
    return [species_name]

def get_evolution_stage(species_name, base_form=None):
    """Determine evolution stage (0=base, 1=stage1, etc.)"""
    if not base_form:
        base_form = get_base_form(species_name)
    
    if species_name == base_form:
        return 0
    
    # Count stages by getting full evolution line
    all_stages = get_all_evolution_stages(base_form)
    for i, stage in enumerate(all_stages):
        if stage == species_name:
            return i
    return 1  # Default

def get_base_form(species_name):
    """Get the base form of a Pokémon"""
    try:
        species_data = get_species_data(species_name)
        if not species_data:
            return species_name
        
        current = species_name
        max_depth = 10
        depth = 0
        while species_data.get("evolves_from_species") and depth < max_depth:
            prev = species_data["evolves_from_species"]["name"]
            species_data = get_species_data(prev)
            if not species_data:
                break
            current = prev
            depth += 1
        
        return current
    except:
        return species_name

def get_tier_for_stage(stage, original_tier_of_base=None):
    """Determine which tier a stage should go into"""
    # Stage 0 (base) - goes to common or uncommon based on original base tier
    if stage == 0:
        if original_tier_of_base in ["common", "uncommon"]:
            return "common"
        elif original_tier_of_base in ["rare", "ultra_rare"]:
            return "uncommon"
        return "common"
    # Stage 1 - goes to uncommon or rare
    elif stage == 1:
        return "uncommon"
    # Stage 2 - goes to rare or ultra rare
    elif stage == 2:
        return "rare"
    # Stage 3+ - goes to ultra rare
    else:
        return "ultra_rare"

def complete_class_pools(pool_data, class_name):
    """Add missing evolution stages to a class's pools"""
    
    # Collect all Pokémon in the class
    all_pokemon = set()
    for tier in ["common", "uncommon", "rare", "ultra_rare"]:
        all_pokemon.update(pool_data.get(tier, []))
    
    # Group by evolution family
    families = defaultdict(set)
    base_tiers = {}
    
    for pokemon in all_pokemon:
        base = get_base_form(pokemon)
        families[base].add(pokemon)
        
        # Track the original tier of base forms
        if pokemon == base:
            for tier in ["common", "uncommon", "rare", "ultra_rare"]:
                if pokemon in pool_data.get(tier, []):
                    base_tiers[base] = tier
                    break
    
    # For each family, ensure all stages are present
    new_pools = {
        "common": list(pool_data.get("common", [])),
        "uncommon": list(pool_data.get("uncommon", [])),
        "rare": list(pool_data.get("rare", [])),
        "ultra_rare": list(pool_data.get("ultra_rare", []))
    }
    
    for base, members in families.items():
        # Get all stages for this evolution line
        all_stages = get_all_evolution_stages(base)
        
        # Check which stages are missing
        for stage_name in all_stages:
            if stage_name not in members:
                # This stage is missing - add it
                stage = get_evolution_stage(stage_name, base)
                base_tier = base_tiers.get(base, "common")
                target_tier = get_tier_for_stage(stage, base_tier)
                
                if stage_name not in new_pools[target_tier]:
                    new_pools[target_tier].append(stage_name)
                    print(f"    Added missing {stage_name} (stage {stage}) to {target_tier}")
    
    # Remove duplicates and sort for consistency
    for tier in new_pools:
        new_pools[tier] = sorted(list(set(new_pools[tier])))
    
    return new_pools

def main():
    print("=" * 60)
    print("ADDING MISSING EVOLUTION STAGES TO POKÉMON POOLS")
    print("=" * 60)
    
    # Load the adjusted pools
    input_file = "adjusted_pools_original.json"
    if not Path(input_file).exists():
        print(f"Error: {input_file} not found!")
        print("Running with expanded_pools.json instead?")
        input_file = "expanded_pools.json"
    
    print(f"Loading {input_file}...")
    with open(input_file, "r") as f:
        pools = json.load(f)
    
    print(f"Loaded {len(pools)} classes")
    
    # Complete each class
    completed_pools = {}
    
    for class_name, pool_data in pools.items():
        print(f"\nProcessing {class_name}...")
        print(f"  Before: common={len(pool_data.get('common', []))}, "
              f"uncommon={len(pool_data.get('uncommon', []))}, "
              f"rare={len(pool_data.get('rare', []))}, "
              f"ultra_rare={len(pool_data.get('ultra_rare', []))}")
        
        completed_pools[class_name] = complete_class_pools(pool_data, class_name)
        
        print(f"  After: common={len(completed_pools[class_name]['common'])}, "
              f"uncommon={len(completed_pools[class_name]['uncommon'])}, "
              f"rare={len(completed_pools[class_name]['rare'])}, "
              f"ultra_rare={len(completed_pools[class_name]['ultra_rare'])}")
    
    # Save
    output_file = "completed_pools.json"
    with open(output_file, "w") as f:
        json.dump(completed_pools, f, indent=2)
    
    print(f"\n✅ Saved to {output_file}")

if __name__ == "__main__":
    main()