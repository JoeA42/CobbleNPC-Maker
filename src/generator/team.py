# team.py
import random
from config import RANKS, RARITY_WEIGHTS, BAG_ITEMS
from src.api import get_evolved_form, get_moves, get_ability
from src.generator.evolution import get_min_evolution_level, is_valid_for_level
from src.api import get_best_held_item

DEBUG = True

def debug_print(msg, level=0):
    if DEBUG:
        indent = "  " * level
        print(f"{indent}{msg}")

def get_team_size(rank_idx):
    """Get expected team size for a rank"""
    if rank_idx <= 1:
        return 2
    elif rank_idx <= 3:
        return 3
    elif rank_idx <= 5:
        return 4
    elif rank_idx <= 6:
        return 5
    else:
        return 6

# team.py

def select_pokemon_by_rarity(pokemon_pool, rank_idx, level=None):
    """Select a Pokémon based on rank-adjusted rarity weights, optionally filtered by level"""
    rank = min(rank_idx, 8)
    
    common_weight = RARITY_WEIGHTS["common"][rank]
    uncommon_weight = RARITY_WEIGHTS["uncommon"][rank]
    rare_weight = RARITY_WEIGHTS["rare"][rank]
    ultra_weight = RARITY_WEIGHTS["ultra_rare"][rank]
    
    available = []
    weights = []
    
    # Build list with weights, optionally filter by level and rank
    for rarity, weight in [("common", common_weight), ("uncommon", uncommon_weight), ("rare", rare_weight), ("ultra_rare", ultra_weight)]:
        for species in pokemon_pool.get(rarity, []):
            if level is not None and not is_valid_for_level(species, level, rank_idx):
                continue
            available.append(species)
            weights.append(weight)
    
    if not available:
        # Fallback: try without level filter
        if level is not None:
            return select_pokemon_by_rarity(pokemon_pool, rank_idx, None)
        return None
    
    return random.choices(available, weights=weights)[0]


def add_new_pokemon(pokemon_pool, used_species, rank_level, trainer_class, rank_idx):
    """Add a new Pokémon, evolved appropriately for the level"""
    species = select_pokemon_by_rarity(pokemon_pool, rank_idx, rank_level)
    if not species:
        return None
    
    if species in used_species:
        all_pokemon = []
        for rarity in ["common", "uncommon", "rare", "ultra_rare"]:
            all_pokemon.extend(pokemon_pool.get(rarity, []))
        available = [p for p in all_pokemon if p not in used_species]
        if available:
            species = random.choice(available)
    
    evolved = get_evolved_form(species, rank_level, trainer_class)
    
    # Level calculation
    if evolved != species:
        min_evo = get_min_evolution_level(species, evolved, trainer_class)
        if min_evo:
            base_level = min(rank_level, max(min_evo, rank_level - random.randint(0, 3)))
        else:
            base_level = min(rank_level, rank_level - random.randint(0, 2))
    else:
        base_level = min(rank_level, rank_level - random.randint(2, 5))
    
    return {
        "species": evolved,
        "level": max(1, base_level),
        "gender": random.choice(["MALE", "FEMALE"]),
        "nature": random.choice([
            "hardy", "lonely", "brave", "adamant", "naughty",
            "bold", "docile", "relaxed", "impish", "lax",
            "timid", "hasty", "serious", "jolly", "naive",
            "modest", "mild", "quiet", "bashful", "rash",
            "calm", "gentle", "sassy", "careful", "quirky"
        ]),
        "ability": get_ability(evolved),
        "shiny": random.random() < 0.01,
        "moveset": get_moves(evolved, rank_level),
        "ivs": {s: random.randint(10, 31) for s in ["hp", "atk", "def", "spa", "spd", "spe"]},
        "evs": {s: random.randint(0, 85) for s in ["hp", "atk", "def", "spa", "spd", "spe"]},
        "heldItem": get_best_held_item(evolved, rank_idx)
    }