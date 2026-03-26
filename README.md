# CobbleNPC Maker

A comprehensive tool for generating Pokémon trainer NPCs for Minecraft Cobblemon modpacks. Creates fully functional NPCs compatible with Easy NPCs mod, with progressive difficulty based on player badge count.

## What It Does

- **Generates Trainer NPCs**: Creates Easy NPCs .snbt files with:
  - Auto-battle on approach
  - Rank-based difficulty scaling (novice → elite)
  - Custom dialog for each rank
  - Flavor text on right-click
  - Daily cooldown system

- **Generates Gym Leader NPCs**: Specialized NPCs with:
  - Challenge dialogs with Accept/Refuse buttons
  - Badge ceremony with TM and TM Case rewards
  - Daily rematches with 24-hour cooldown
  - Rank-specific victory dialogs (all 12 ranks)

- **Generates Pokémon Trainer JSONs**: Complete trainer profiles with:
  - Pokémon teams scaled to rank
  - Appropriate moves, abilities, held items
  - EVs/IVs and natures
  - Bag items

## Requirements

### Minecraft Server (to use the NPCs)
- **Minecraft** 1.21.1
- ***NeoForge** 21.1.219
- **Easy NPCs** (6.11.0+) - For NPC entities
- **TBCS (Trainer Battle Commands System)** - For Pokémon battles
- **RCT API** - For trainer AI
- **KubeJS** (2101.7.2+) - For server-side logic
- **Cobblemon** - For Pokémon mechanics
- **SimpleTMs** - For TM items and TM Case
- **Numismatics** - For currency/rewards

### Python Environment (to run this tool)
- Python 3.9+
- Required packages: `pyyaml`, `requests`

## Installation

```bash
git clone https://github.com/JoeA42/CobbleNPC-Maker.git
cd CobbleNPC-Maker
pip install pyyaml requests
python main.py
```

## Quick Start

1. **First, generate Pokémon pools** (optional - uses default pools if skipped):
   ```
   Main Menu → 5. Pool Generation Operations → 1. Generate Pokémon pools
   ```

2. **Generate a trainer**:
   ```
   Main Menu → 1. Trainer Operations → 1. Generate a single trainer (interactive)
   ```

3. **Generate the NPC file**:
   ```
   Main Menu → 3. NPC Operations → 1. Generate NPCs for all trainers
   ```

4. **Copy outputs to your server**:
   ```bash
   cp outputs/npcs/regular/*.npc.snbt /path/to/server/npcs/
   cp outputs/trainers/regular/**/*.json /path/to/server/trainers/regular/
   ```

## Output Structure

```
outputs/
├── trainers/           # Pokémon trainer JSONs
│   ├── regular/        # Regular trainers by class
│   └── leaders/        # Gym leader JSONs
├── npcs/               # Easy NPCs .snbt files
│   ├── regular/        # Regular trainer NPCs
│   ├── gym_leaders/    # Gym leader NPCs
│   └── quests/         # Quest NPCs (future)
└── kubejs/             # KubeJS configs
    └── data/           # trainer_config.json
```

## Source Files

```
source/
├── game_data.py        # Core configuration (ranks, pools, names, dialogs)
├── templates/          # SNBT templates
│   ├── base_trainer.snbt
│   └── base_gym_leader.snbt
└── leaders/            # Seed gym leader JSON files (manual templates)
    └── ikuma/
        └── ikuma_novice.json
```

## Features

### Regular Trainers
- **3-rank progression** (novice → challenger → elite)
- **Team scaling** based on badge count
- **Daily cooldown**: 24h on win, 20m on loss
- **Customizable dialogs** per trainer class

### Gym Leaders
- **12-rank progression** (novice → master → master★★★)
- **First victory**: Badge + TM + TM Case (first badge only)
- **Rematches**: Daily with coin rewards
- **Rank-specific victory dialogs**

### Pokémon Pool Generation
- Fetches Pokémon from PokéAPI by type
- Rarity tiers based on catch rate
- Class-specific pools (bug catchers, scientists, etc.)

## License

MIT License - See LICENSE file for details

## Credits

Created for the IndustrialMon modpack. Built with:
- Easy NPCs mod
- TBCS (Trainer Battle Commands System)
- Cobblemon
- KubeJS
```

Now rename the main file references:

```bash
cd ~/Documents/CobbleNPC-Maker

# Update main.py to reference new name
sed -i 's/POKÉMON TRAINER GENERATOR/COBBLE NPC MAKER/g' src/menus/*.py
sed -i 's/Pokémon Trainer Generator/Cobble NPC Maker/g' README.md
```

Now commit and push:

```bash
git add .
git commit -m "Rename project to CobbleNPC Maker and update README"
git remote add origin https://github.com/JoeA42/CobbleNPC-Maker.git
git push -u origin main
```

