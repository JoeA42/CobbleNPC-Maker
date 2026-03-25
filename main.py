#!/usr/bin/env python3
"""
Pokémon Trainer Generator - Main Entry Point
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.menus.main_menu import main_menu

if __name__ == "__main__":
    main_menu()