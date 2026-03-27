# src/utils/config.py - Complete updated Config class

"""Configuration management for CobbleNPC Maker"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv()

class Config:
    """Application configuration from environment variables"""
    
    # Server configuration
    SERVER_ROOT = Path(os.getenv('SERVER_ROOT', '~/MCServer-local')).expanduser()
    SERVER_HOST = os.getenv('SERVER_HOST', '192.168.1.42')
    SERVER_USER = os.getenv('SERVER_USER', 'jose')
    SERVER_PATH = os.getenv('SERVER_PATH', '/home/jose/MCServer')
    
    # Server subpath - for multiple servers, you can specify which one
    SERVER_SUBPATH = os.getenv('SERVER_SUBPATH', 'cobblemonServer')
    
    # Base data path
    DATA_PATH = SERVER_ROOT / SERVER_SUBPATH / "MCDocker/MCServer/MCData"
    
    # World path
    WORLD_PATH = DATA_PATH / "world"
    
    # Export destinations (relative to world)
    TRAINERS_REGULAR = WORLD_PATH / 'trainers/regular'
    TRAINERS_LEADERS = WORLD_PATH / 'trainers/leaders'
    NPCS_PATH = WORLD_PATH / 'npcs'
    KUBEJS_DATA = DATA_PATH / 'kubejs/data'
    KUBEJS_SCRIPTS = DATA_PATH / 'kubejs/server_scripts'
    
    # Trainer config file
    TRAINER_CONFIG = KUBEJS_DATA / "trainer_config.json"
    
    # TBCS config - FIXED PATH
    TBCS_CONFIG = DATA_PATH / 'config/tbcs-server.toml'
    
    # Mod sync paths
    MOD_SOURCE = Path(os.getenv('MOD_SOURCE', 
        '~/Documents/curseforge/minecraft/Instances/IndustrialMonServerDev/mods')).expanduser()
    MOD_TARGET = DATA_PATH / 'mods'
    
    # Export options
    BACKUP_ENABLED = os.getenv('BACKUP_ENABLED', 'true').lower() == 'true'
    AUTO_RELOAD = os.getenv('AUTO_RELOAD', 'false').lower() == 'true'
    
    # Output directory
    OUTPUT_DIR = Path('outputs')
    
    @classmethod
    def print_config(cls):
        """Print current configuration"""
        print("=" * 60)
        print("    CURRENT CONFIGURATION")
        print("=" * 60)
        print(f"Server root: {cls.SERVER_ROOT}")
        print(f"Server subpath: {cls.SERVER_SUBPATH}")
        print(f"Data path: {cls.DATA_PATH}")
        print(f"World path: {cls.WORLD_PATH}")
        print(f"Trainers regular: {cls.TRAINERS_REGULAR}")
        print(f"Trainers leaders: {cls.TRAINERS_LEADERS}")
        print(f"NPCs path: {cls.NPCS_PATH}")
        print(f"KubeJS data: {cls.KUBEJS_DATA}")
        print(f"KubeJS scripts: {cls.KUBEJS_SCRIPTS}")
        print(f"Trainer config: {cls.TRAINER_CONFIG}")
        print(f"TBCS config: {cls.TBCS_CONFIG}")
        print(f"Mod source: {cls.MOD_SOURCE}")
        print(f"Mod target: {cls.MOD_TARGET}")
        print(f"Backup enabled: {cls.BACKUP_ENABLED}")
        print(f"Auto reload: {cls.AUTO_RELOAD}")
        print("=" * 60)
    
    @classmethod
    def check_mount(cls):
        """Check if the server directory is mounted and accessible"""
        if not cls.SERVER_ROOT.exists():
            return False
        try:
            # Check if it's a mount point or has content
            if any(cls.SERVER_ROOT.iterdir()):
                return True
        except (PermissionError, OSError):
            pass
        return False
    
    @classmethod
    def get_mount_command(cls):
        """Get the SSHFS mount command for this server"""
        return f"sshfs {cls.SERVER_USER}@{cls.SERVER_HOST}:{cls.SERVER_PATH} {cls.SERVER_ROOT}"