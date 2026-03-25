# src/npc/__init__.py
from src.npc.trainer_npc import generate_all_npcs, generate_for_trainer
from src.npc.gym_leader_npc import generate_all_gym_leaders, generate_gym_leader_snbt
from src.npc.template import load_template, generate_uuids

__all__ = [
    'generate_all_npcs',
    'generate_for_trainer',
    'generate_all_gym_leaders',
    'generate_gym_leader_snbt',
    'load_template',
    'generate_uuids'
]