# src/npc/template.py
import random

def load_template(template_path):
    """Load the base SNBT template"""
    with open(template_path, "r") as f:
        return f.read()

def generate_uuids():
    """Generate 4 random integers for UUIDs"""
    return [random.randint(-2147483648, 2147483647) for _ in range(4)]