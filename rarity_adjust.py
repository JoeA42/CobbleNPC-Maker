#!/usr/bin/env python3
"""
rarity_adjust_original.py - Adjust tiers based on evolution stage
- Base forms stay in their original tier (preserves catch rate rarity)
- Evolved forms move UP one tier
- Adds missing base forms if needed
- Does NOT preserve original tier counts
"""

import json
import time
import requests
from pathlib import Path
from collections import defaultdict

CACHE_DIR = Path("pokemon_cache")
CACHE_DIR.mkdir(exist_ok=True)

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

def adjust_pool(pool_data):
    """Adjust tiers: base forms stay, evolved forms move up one tier"""
    
    # Tier order for moving up
    tier_order = ["common", "uncommon", "rare", "ultra_rare"]
    tier_index = {tier: i for i, tier in enumerate(tier_order)}
    
    # New pools
    new_pools = {
        "common": [],
        "uncommon": [],
        "rare": [],
        "ultra_rare": []
    }
    
    # Track all Pokémon we've processed
    processed = set()
    
    # Process each tier from highest to lowest
    for tier in reversed(tier_order):
        for pokemon in pool_data.get(tier, []):
            if pokemon in processed:
                continue
            
            base = get_base_form(pokemon)
            
            if base == pokemon:
                # Base form - keep in same tier
                new_pools[tier].append(pokemon)
                processed.add(pokemon)
            else:
                # Evolved form - move up one tier
                current_idx = tier_index[tier]
                new_idx = min(3, current_idx + 1)
                new_tier = tier_order[new_idx]
                new_pools[new_tier].append(pokemon)
                processed.add(pokemon)
                
                # Also ensure the base form exists somewhere
                if base not in processed:
                    # Add base form to one tier lower than the evolved form
                    base_idx = max(0, new_idx - 1)
                    base_tier = tier_order[base_idx]
                    if base not in new_pools[base_tier]:
                        new_pools[base_tier].append(base)
                        processed.add(base)
    
    # Remove duplicates
    for tier in new_pools:
        new_pools[tier] = list(set(new_pools[tier]))
    
    return new_pools

def main():
    print("=" * 60)
    print("ADJUSTING POKÉMON TIERS (Base forms stay, evolved forms move up)")
    print("=" * 60)
    
    # Load original pools
    input_file = "expanded_pools.json"
    if not Path(input_file).exists():
        print(f"Error: {input_file} not found!")
        return
    
    print(f"Loading {input_file}...")
    with open(input_file, "r") as f:
        pools = json.load(f)
    
    print(f"Loaded {len(pools)} classes")
    
    # Adjust each class
    adjusted_pools = {}
    
    for class_name, pool_data in pools.items():
        print(f"\nProcessing {class_name}...")
        print(f"  Original sizes: common={len(pool_data.get('common', []))}, "
              f"uncommon={len(pool_data.get('uncommon', []))}, "
              f"rare={len(pool_data.get('rare', []))}, "
              f"ultra_rare={len(pool_data.get('ultra_rare', []))}")
        
        adjusted_pools[class_name] = adjust_pool(pool_data)
        
        print(f"  New sizes: common={len(adjusted_pools[class_name]['common'])}, "
              f"uncommon={len(adjusted_pools[class_name]['uncommon'])}, "
              f"rare={len(adjusted_pools[class_name]['rare'])}, "
              f"ultra_rare={len(adjusted_pools[class_name]['ultra_rare'])}")
    
    # Save
    output_file = "adjusted_pools_original.json"
    with open(output_file, "w") as f:
        json.dump(adjusted_pools, f, indent=2)
    
    print(f"\n✅ Saved to {output_file}")

if __name__ == "__main__":
    main()