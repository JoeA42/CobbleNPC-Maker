# evs.py
import random
from src.api import api

def generate_ivs(is_leader):
    if is_leader:
        return {s: random.randint(20, 31) for s in ["hp", "atk", "def", "spa", "spd", "spe"]}
    else:
        return {s: random.randint(10, 31) for s in ["hp", "atk", "def", "spa", "spd", "spe"]}

def generate_initial_evs(species, rank_idx, is_leader):
    """Generate initial EVs for a new Pokémon (respect 252 per stat, 510 total)"""
    evs = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
    
    if rank_idx == 0:
        return evs
    
    data = api.get_pokemon(species)
    if data:
        stat_map = {
            "hp": "hp",
            "attack": "atk",
            "defense": "def",
            "special-attack": "spa",
            "special-defense": "spd",
            "speed": "spe"
        }
        
        stats = {}
        for stat in data["stats"]:
            stat_name = stat["stat"]["name"]
            if stat_name in stat_map:
                stats[stat_map[stat_name]] = stat["base_stat"]
        
        prioritized = sorted(stats.items(), key=lambda x: x[1], reverse=True)
        primary = prioritized[0][0]
        secondary = prioritized[1][0]
    else:
        primary = "atk"
        secondary = "spe"
    
    if is_leader:
        total_evs = min(100 + (rank_idx * 20), 510)
    else:
        total_evs = min(50 + (rank_idx * 10), 510)
    
    # Distribute EVs - max 252 per stat
    evs[primary] = min(total_evs // 2, 252)
    remaining = total_evs - evs[primary]
    evs[secondary] = min(remaining, 252)
    
    return evs

def train_evs(current_evs, species, rank_idx, is_leader):
    """Train EVs for existing Pokémon (only increase, respect 252 per stat, 510 total)"""
    data = api.get_pokemon(species)
    if data:
        stat_map = {
            "hp": "hp",
            "attack": "atk",
            "defense": "def",
            "special-attack": "spa",
            "special-defense": "spd",
            "speed": "spe"
        }
        
        stats = {}
        for stat in data["stats"]:
            stat_name = stat["stat"]["name"]
            if stat_name in stat_map:
                stats[stat_map[stat_name]] = stat["base_stat"]
        
        # Get top 2 highest stats
        sorted_stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)
        primary = sorted_stats[0][0]
        secondary = sorted_stats[1][0]
    else:
        primary = "atk"
        secondary = "spe"
    
    if is_leader:
        gain = 40 + (rank_idx * 15)
    else:
        gain = 20 + (rank_idx * 8)
    
    new_evs = current_evs.copy()
    
    # Ensure all EV keys exist
    for key in ["hp", "atk", "def", "spa", "spd", "spe"]:
        if key not in new_evs:
            new_evs[key] = 0
    
    # Calculate current total EVs
    total_evs = sum(new_evs.values())
    max_total = 510
    
    # Add to primary stat until 252 or total limit
    if new_evs[primary] < 252 and total_evs < max_total:
        add = min(gain, 252 - new_evs[primary], max_total - total_evs)
        new_evs[primary] += add
        gain -= add
        total_evs += add
    
    # Add remaining to secondary stat
    if gain > 0 and new_evs[secondary] < 252 and total_evs < max_total:
        add = min(gain, 252 - new_evs[secondary], max_total - total_evs)
        new_evs[secondary] += add
    
    # Zero out any EVs in non-priority stats
    priority_stats = [primary, secondary]
    for stat in ["hp", "atk", "def", "spa", "spd", "spe"]:
        if stat not in priority_stats and new_evs[stat] > 0:
            excess = new_evs[stat]
            new_evs[stat] = 0
            total_evs -= excess
            
            if new_evs[primary] < 252:
                add = min(excess, 252 - new_evs[primary])
                new_evs[primary] += add
                excess -= add
            if excess > 0 and new_evs[secondary] < 252:
                add = min(excess, 252 - new_evs[secondary])
                new_evs[secondary] += add
    
    return new_evs