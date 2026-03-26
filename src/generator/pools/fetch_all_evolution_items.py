#!/usr/bin/env python3
# fetch_all_evolution_items.py - Fetch all evolution items and their details

import json
import requests
import time
from pathlib import Path

def fetch_all_items():
    """Fetch all items from PokéAPI"""
    all_items = []
    url = "https://pokeapi.co/api/v2/item?limit=1000"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch items list")
        return []
    
    data = response.json()
    items = data["results"]
    
    print(f"Found {len(items)} total items, filtering evolution items...")
    
    for item in items:
        item_name = item["name"]
        # Fetch item details
        item_url = item["url"]
        response = requests.get(item_url)
        if response.status_code == 200:
            item_data = response.json()
            # Check if this item is used in evolution
            # Look for evolution-related categories or attributes
            category = item_data.get("category", {}).get("name", "")
            attributes = [attr["name"] for attr in item_data.get("attributes", [])]
            
            # Evolution items typically have categories like "evolution", "held-items"
            if "evolution" in category or "held" in category or "stone" in item_name:
                all_items.append({
                    "name": item_name,
                    "category": category,
                    "attributes": attributes,
                    "cost": item_data.get("cost", 0)
                })
                print(f"  Found: {item_name} (category: {category})")
        
        time.sleep(0.05)
    
    return all_items

def assign_tiers(items):
    """Assign tiers to evolution items based on their properties"""
    basic_items = []
    rare_items = []
    master_items = []
    
    for item in items:
        name = item["name"]
        
        # Stone evolutions - basic tier
        if "stone" in name:
            basic_items.append(name)
        # Trade items - rare tier
        elif any(trade_item in name for trade_item in ["metal", "scale", "coat", "cable", "protector", 
                                                        "electirizer", "magmarizer", "reaper", "razor"]):
            rare_items.append(name)
        # Special items - master tier
        elif any(master_item in name for master_item in ["dubious", "prism", "sweet", "tart", "pot", "galarica"]):
            master_items.append(name)
        # Default to rare for other evolution items
        elif "held" in item["category"]:
            rare_items.append(name)
        else:
            basic_items.append(name)
    
    return {
        "basic": {
            "min_rank": 3,
            "min_level": 20,
            "items": basic_items
        },
        "rare": {
            "min_rank": 4,
            "min_level": 25,
            "items": rare_items
        },
        "master": {
            "min_rank": 6,
            "min_level": 30,
            "items": master_items
        }
    }

def main():
    print("=" * 60)
    print("FETCHING ALL EVOLUTION ITEMS FROM POKÉAPI")
    print("=" * 60)
    
    items = fetch_all_items()
    print(f"\nFound {len(items)} evolution items")
    
    tiers = assign_tiers(items)
    
    # Save to file
    output_file = "evolution_tiers.json"
    with open(output_file, "w") as f:
        json.dump(tiers, f, indent=2)
    
    print(f"\n✅ Saved to {output_file}")
    print("\nTiers:")
    for tier, config in tiers.items():
        print(f"  {tier}: rank {config['min_rank']}+, level {config['min_level']}+, {len(config['items'])} items")
        print(f"    Items: {', '.join(config['items'][:10])}" + ("..." if len(config['items']) > 10 else ""))
    
    # Also generate a Python version for config.py
    print("\n\nCopy this into config.py:")
    print("EVOLUTION_TIERS = {")
    for tier, config in tiers.items():
        print(f'    "{tier}": {{')
        print(f'        "min_rank": {config["min_rank"]},')
        print(f'        "min_level": {config["min_level"]},')
        print(f'        "items": {json.dumps(config["items"], indent=12)}')
        print(f"    }},")
    print("}")

if __name__ == "__main__":
    main()