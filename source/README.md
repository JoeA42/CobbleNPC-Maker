# Source Files

This folder contains source/template files used by the generator.

## Structure

- `leaders/` - Seed gym leader JSON files (the base rank file for each gym leader)
- `templates/` - SNBT templates for NPC generation
- `profiles/` - Optional seed profiles for regular trainers

## Usage

The generator reads from `source/` for templates and seed files, and writes generated output to `outputs/`.

Do not edit files in `outputs/` directly. Make changes in `source/` and regenerate.
