"""Backup utilities for safe file operations"""
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Union

class BackupManager:
    """Create and manage backups of server directories"""
    
    def __init__(self, server_root: Path):
        self.server_root = server_root
        self.backup_base = server_root / ".backups"
    
    def create_backup(self, paths: List[Union[Path, str]], description: str = "") -> Path:
        """
        Create a timestamped backup of given paths
        
        Args:
            paths: List of paths to backup (relative to server_root)
            description: Optional description (e.g., "before_trainer_sync")
        
        Returns:
            Path to the backup directory
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_name = f"{timestamp}_{description}" if description else timestamp
        backup_dir = self.backup_base / backup_name
        
        print(f"\n💾 Creating backup: {backup_dir}")
        backup_dir.mkdir(parents=True, exist_ok=True)
        
        backed_up = []
        for path in paths:
            full_path = path if isinstance(path, Path) else Path(path)
            if not full_path.is_absolute():
                full_path = self.server_root / full_path
            
            if full_path.exists():
                # Create relative path for backup structure
                rel_path = full_path.relative_to(self.server_root)
                backup_path = backup_dir / rel_path
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                
                if full_path.is_file():
                    shutil.copy2(full_path, backup_path)
                    backed_up.append(str(rel_path))
                elif full_path.is_dir():
                    shutil.copytree(full_path, backup_path, dirs_exist_ok=True)
                    backed_up.append(f"{rel_path}/ (folder)")
        
        if backed_up:
            print(f"   ✅ Backed up {len(backed_up)} items")
        else:
            print(f"   ⚠️ No files found to backup")
            # Remove empty backup directory
            backup_dir.rmdir()
            return None
        
        return backup_dir
    
    def list_backups(self) -> List[Path]:
        """List all available backups"""
        if not self.backup_base.exists():
            return []
        return sorted([p for p in self.backup_base.iterdir() if p.is_dir()])
    
    def restore_from_backup(self, backup_name: str, dry_run: bool = True):
        """Restore from a backup (implementation later)"""
        # This will be implemented when needed
        pass
    
    def cleanup_old_backups(self, keep_days: int = 7):
        """Remove backups older than keep_days"""
        if not self.backup_base.exists():
            return
        
        cutoff = datetime.now().timestamp() - (keep_days * 24 * 3600)
        removed = 0
        
        for backup in self.backup_base.iterdir():
            if backup.is_dir() and backup.stat().st_mtime < cutoff:
                shutil.rmtree(backup)
                removed += 1
        
        if removed:
            print(f"🧹 Cleaned up {removed} old backups (older than {keep_days} days)")