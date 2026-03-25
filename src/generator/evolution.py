# evolution.py
from src.api import get_evolution_chain, get_evolution_method

def get_base_form(species):
    """Get the base form of a Pokémon (lowest in evolution chain)"""
    evo_chain = get_evolution_chain(species)
    if evo_chain:
        return evo_chain["chain"]["species"]["name"]
    return species

def get_min_evolution_level_for_species(species):
    """Get the minimum level at which this specific species can appear (considering its evolution chain)"""
    base_form = get_base_form(species)
    if base_form == species:
        return 1  # Base forms can appear at level 1
    
    # Find the evolution path from base to this species
    evo_chain = get_evolution_chain(base_form)
    if not evo_chain:
        return 1
    
    def traverse_evolution(chain, target, current_level):
        if chain.get("species", {}).get("name") == target:
            return current_level
        evolves_to = chain.get("evolves_to", [])
        for evo in evolves_to:
            for detail in evo.get("evolution_details", []):
                min_level = detail.get("min_level")
                next_species = evo["species"]["name"]
                new_level = current_level
                if min_level:
                    new_level = max(current_level, min_level)
                result = traverse_evolution(evo, target, new_level)
                if result:
                    return result
        return None
    
    result = traverse_evolution(evo_chain["chain"], species, 1)
    
    # For trade/stone/item evolutions without level requirement, set a default minimum
    if result is None:
        evo_method = get_evolution_method(species)
        if evo_method:
            trigger = evo_method.get("trigger", {}).get("name")
            if trigger in ["trade", "use-item"]:
                return 20  # Minimum level 20 for trade/stone evolutions
        return 1
    
    return result or 1

def get_min_evolution_level(base_species, evolved_species, trainer_class=None):
    """Find the minimum level at which a Pokémon can evolve into its form (for scaling)"""
    evo_chain = get_evolution_chain(base_species)
    if not evo_chain:
        return None
    
    def find_min_level(chain, current_species, target_species, current_min=1):
        if chain.get("species", {}).get("name") == current_species:
            evolves_to = chain.get("evolves_to", [])
            for evo in evolves_to:
                for detail in evo.get("evolution_details", []):
                    min_level = detail.get("min_level")
                    next_species = evo["species"]["name"]
                    new_min = current_min
                    if min_level:
                        new_min = max(current_min, min_level)
                    
                    if next_species == target_species:
                        return new_min
                    
                    result = find_min_level(evo, next_species, target_species, new_min)
                    if result:
                        return result
            return None
        
        for evo in chain.get("evolves_to", []):
            result = find_min_level(evo, current_species, target_species, current_min)
            if result:
                return result
        return None
    
    return find_min_level(evo_chain["chain"], base_species, evolved_species)

def is_valid_for_level(species, level, rank_idx=None):
    """Check if a Pokémon can exist at this level and rank"""
    base_form = get_base_form(species)
    if base_form == species:
        return True
    
    min_level = get_min_evolution_level_for_species(species)
    if level < min_level:
        return False
    
    # For trade/stone/item evolutions, require minimum rank (Challenger = 4)
    if rank_idx is not None:
        evo_method = get_evolution_method(species)
        if evo_method:
            trigger = evo_method.get("trigger", {}).get("name")
            if trigger in ["trade", "use-item"]:
                if rank_idx < 4:  # Require rank 4 (Challenger) or higher
                    return False
    
    return True