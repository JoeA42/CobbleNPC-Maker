# src/utils/debug.py
import os

DEBUG = True

def debug_print(msg, level=0):
    if DEBUG:
        indent = "  " * level
        print(f"{indent}{msg}")

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')