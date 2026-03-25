# src/generator/core.py
import random
from config import RANKS, BAG_ITEMS
from src.api import get_evolved_form, get_moves, get_ability
from src.generator.evolution import get_min_evolution_level
from src.api import get_best_held_item
from src.generator.evs import generate_ivs, generate_initial_evs, train_evs
from src.generator.team import select_pokemon_by_rarity, get_team_size, add_new_pokemon
from src.utils.debug import debug_print

def scale_trainer_to_rank(team, target_rank_idx, trainer_class, pokemon_pool, allow_add_new=True):
    """Scale an existing team to a higher rank"""
    target_rank = RANKS[target_rank_idx]
    target_level = target_rank["level"]
    rank_name = target_rank["name"]
    
    debug_print(f"\n{'='*50}")
    debug_print(f"SCALING TEAM to {rank_name} (level {target_level})")
    debug_print(f"{'='*50}")
    
    # Get bag items for target rank
    bag_items = BAG_ITEMS.get(target_rank_idx, [{"item": "cobblemon:potion", "quantity": 1}])
    
    new_team = []
    
    # Process each existing Pokémon
    for i, pokemon in enumerate(team):
        species = pokemon["species"]
        original_level = pokemon["level"]
        
        # Evolve if possible
        evolved = get_evolved_form(species, target_level, trainer_class)
        
        # New level: at least original, at most target cap
        new_level = max(original_level, min(target_level, original_level + random.randint(5, 12)))
        
        # Ensure evolved Pokémon meet evolution level
        if evolved != species:
            min_evo = get_min_evolution_level(species, evolved, trainer_class)
            if min_evo and new_level < min_evo:
                new_level = min_evo
        
        # Get new moves and ability
        new_moves = get_moves(evolved, target_level)
        new_ability = get_ability(evolved)
        
        # Get new held item
        new_held = get_best_held_item(evolved, target_rank_idx)
        
        if evolved != species:
            debug_print(f"  ✨ {species} (lvl {original_level}) → {evolved} (lvl {new_level})")
        else:
            debug_print(f"  📈 {species} (lvl {original_level} → {new_level})")
        
        new_team.append({
            "species": evolved,
            "level": new_level,
            "gender": pokemon["gender"],
            "nature": pokemon["nature"],
            "ability": new_ability,
            "shiny": pokemon["shiny"],
            "moveset": new_moves,
            "ivs": pokemon["ivs"],
            "evs": pokemon["evs"],
            "heldItem": new_held
        })
    
    # Determine target team size based on rank
    target_team_size = get_team_size(target_rank_idx)
    
    # Add new Pokémon if allowed and needed
    if allow_add_new:
        used_species = [p["species"] for p in new_team]
        while len(new_team) < target_team_size:
            new_pokemon = add_new_pokemon(pokemon_pool, used_species, target_level, trainer_class, target_rank_idx)
            if new_pokemon:
                used_species.append(new_pokemon["species"])
                new_team.append(new_pokemon)
                debug_print(f"  + Added {new_pokemon['species']} (lvl {new_pokemon['level']})")
            else:
                break
    
    # Final team summary
    debug_print(f"\n✓ Scaled Team for {rank_name}:")
    for i, p in enumerate(new_team):
        held = f" [held: {p['heldItem']}]" if p.get('heldItem') else ""
        debug_print(f"  {i+1}. {p['species']} (lvl {p['level']}){held}")
    
    return new_team, bag_items

def generate_team(pokemon_list, rank_idx, trainer_class, previous_team=None, is_leader=False):
    rank = RANKS[rank_idx]
    rank_level = rank["level"]
    rank_name = rank["name"]
    team_size = get_team_size(rank_idx)
    
    debug_print(f"\n{'='*50}")
    debug_print(f"⚡ {rank_name.upper()} (Level Cap: {rank_level}, Team Size: {team_size})")
    debug_print(f"{'='*50}")
    
    team = []
    bag_items = BAG_ITEMS.get(rank_idx, [{"item": "cobblemon:potion", "quantity": 1}])
    
    if previous_team:
        debug_print(f"📈 Training to {rank_name}:")
        for i, pokemon in enumerate(previous_team):
            species = pokemon["species"]
            original_level = pokemon["level"]
            original_ability = pokemon.get("ability", "unknown")
            original_moveset = pokemon.get("moveset", [])
            
            evolved = get_evolved_form(species, rank_level, trainer_class)
            
            target = int(rank_level * random.uniform(0.85, 0.95))
            new_level = max(original_level, target)
            new_level = min(rank_level, new_level)
            
            if evolved != species:
                min_evo = get_min_evolution_level(species, evolved, trainer_class)
                if min_evo and new_level < min_evo:
                    new_level = min_evo
            
            new_ability = get_ability(evolved)
            new_moveset = get_moves(evolved, rank_level)
            
            ivs = pokemon["ivs"]
            evs = train_evs(pokemon["evs"], evolved, rank_idx, is_leader)
            
            if evolved != species:
                debug_print(f"  ✨ {species} (lvl {original_level}) → {evolved} (lvl {new_level})", level=1)
                if original_ability != new_ability:
                    debug_print(f"     Ability: {original_ability} → {new_ability}", level=2)
                if original_moveset != new_moveset:
                    debug_print(f"     Moveset: {', '.join(original_moveset)} → {', '.join(new_moveset)}", level=2)
            else:
                debug_print(f"  📈 {species} (lvl {original_level} → {new_level})", level=1)
                if new_level > original_level:
                    debug_print(f"     New level! Learning new moves...", level=2)
                    if original_moveset != new_moveset:
                        debug_print(f"     Moveset: {', '.join(original_moveset)} → {', '.join(new_moveset)}", level=2)
            
            # Nincada evolution bonus
            if species == "nincada" and evolved == "ninjask":
                shedinja_exists = any(p["species"] == "shedinja" for p in team)
                if not shedinja_exists and len(team) < team_size:
                    shedinja_level = max(20, new_level - random.randint(1, 3))
                    shedinja_ability = get_ability("shedinja")
                    shedinja_moveset = get_moves("shedinja", rank_level)
                    shedinja = {
                        "species": "shedinja",
                        "level": shedinja_level,
                        "gender": "GENDERLESS",
                        "nature": pokemon.get("nature", random.choice(["hardy", "lonely", "brave", "adamant", "naughty", "bold", "docile", "relaxed", "impish", "lax", "timid", "hasty", "serious", "jolly", "naive", "modest", "mild", "quiet", "bashful", "rash", "calm", "gentle", "sassy", "careful", "quirky"])),
                        "ability": shedinja_ability,
                        "shiny": pokemon.get("shiny", random.random() < 0.01),
                        "moveset": shedinja_moveset,
                        "ivs": generate_ivs(is_leader),
                        "evs": generate_initial_evs("shedinja", rank_idx, is_leader),
                        "heldItem": get_best_held_item("shedinja", rank_idx)
                    }
                    team.append(shedinja)
                    debug_print(f"     ✨ Bonus Shedinja appears! (lvl {shedinja_level})", level=2)
            
            team.append({
                "species": evolved,
                "level": new_level,
                "gender": pokemon["gender"],
                "nature": pokemon["nature"],
                "ability": new_ability,
                "shiny": pokemon["shiny"],
                "moveset": new_moveset,
                "ivs": ivs,
                "evs": evs,
                "heldItem": get_best_held_item(evolved, rank_idx) if random.random() < 0.5 else None
            })
    else:
        debug_print(f"🌟 Creating initial team at {rank_name} rank (Level Cap: {rank_level}):")
        for i in range(team_size):
            species = select_pokemon_by_rarity(pokemon_list, rank_idx, rank_level)
            evolved = get_evolved_form(species, rank_level, trainer_class)
            
            if rank_idx >= 6:
                base_level = max(1, int(rank_level * random.uniform(0.85, 0.95)))
            elif rank_idx >= 4:
                base_level = max(1, int(rank_level * random.uniform(0.8, 0.9)))
            else:
                base_level = max(1, int(rank_level * random.uniform(0.7, 0.85)))
            
            if evolved != species:
                min_evo = get_min_evolution_level(species, evolved, trainer_class)
                if min_evo and base_level < min_evo:
                    base_level = min_evo
                debug_print(f"  ✨ {species} → {evolved} (lvl {base_level})", level=1)
            else:
                debug_print(f"  + {species} (lvl {base_level})", level=1)
            
            # Nincada evolution bonus
            if species == "nincada" and evolved == "ninjask":
                if len(team) < team_size:
                    shedinja_level = max(20, base_level - random.randint(1, 3))
                    shedinja_ability = get_ability("shedinja")
                    shedinja_moveset = get_moves("shedinja", rank_level)
                    shedinja = {
                        "species": "shedinja",
                        "level": shedinja_level,
                        "gender": "GENDERLESS",
                        "nature": random.choice(["hardy", "lonely", "brave", "adamant", "naughty", "bold", "docile", "relaxed", "impish", "lax", "timid", "hasty", "serious", "jolly", "naive", "modest", "mild", "quiet", "bashful", "rash", "calm", "gentle", "sassy", "careful", "quirky"]),
                        "ability": shedinja_ability,
                        "shiny": random.random() < 0.01,
                        "moveset": shedinja_moveset,
                        "ivs": generate_ivs(is_leader),
                        "evs": generate_initial_evs("shedinja", rank_idx, is_leader),
                        "heldItem": get_best_held_item("shedinja", rank_idx)
                    }
                    team.append(shedinja)
                    debug_print(f"     ✨ Bonus Shedinja appears! (lvl {shedinja_level})", level=2)
            
            team.append({
                "species": evolved,
                "level": base_level,
                "gender": random.choice(["MALE", "FEMALE"]),
                "nature": random.choice(["hardy", "lonely", "brave", "adamant", "naughty", "bold", "docile", "relaxed", "impish", "lax", "timid", "hasty", "serious", "jolly", "naive", "modest", "mild", "quiet", "bashful", "rash", "calm", "gentle", "sassy", "careful", "quirky"]),
                "ability": get_ability(evolved),
                "shiny": random.random() < 0.01,
                "moveset": get_moves(evolved, rank_level),
                "ivs": generate_ivs(is_leader),
                "evs": generate_initial_evs(evolved, rank_idx, is_leader),
                "heldItem": get_best_held_item(evolved, rank_idx) if random.random() < 0.3 else None
            })
    
    if len(team) < team_size:
        debug_print(f"\n📦 Adding new team members:")
    used_species = [p["species"] for p in team]
    while len(team) < team_size:
        new_pokemon = add_new_pokemon(pokemon_list, used_species, rank_level, trainer_class, rank_idx)
        if new_pokemon:
            used_species.append(new_pokemon["species"])
            team.append(new_pokemon)
            debug_print(f"  + {new_pokemon['species']} (lvl {new_pokemon['level']})", level=1)
        else:
            break
    
    debug_print(f"\n✓ {rank_name} Team:")
    for i, p in enumerate(team):
        held = f" [held: {p['heldItem']}]" if p.get('heldItem') else ""
        debug_print(f"  {i+1}. {p['species']} (lvl {p['level']}){held}")
    
    return team, bag_items

def generate_progression(base_rank):
    if base_rank == 0: return [0, 3, 6]
    if base_rank == 1: return [1, 4, 7]
    if base_rank == 2: return [2, 5, 8]
    if base_rank == 3: return [3, 6, 8]
    if base_rank == 4: return [4, 7, 8]
    if base_rank == 5: return [5, 7, 8]
    return [6, 7, 8]