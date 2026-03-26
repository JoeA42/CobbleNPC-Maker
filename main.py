#!/usr/bin/env python3
"""
Pokémon Content Generator - Unified tool for generating:
- Trainer JSONs (regular and gym leaders)
- NPC SNBT files (trainers, gym leaders, quest NPCs)
- KubeJS quest definitions
- Obsidian quest documentation
"""

import sys
import os

# Add src and source to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'source'))

from src.menus.main_menu import main_menu

if __name__ == "__main__":
    main_menu()
