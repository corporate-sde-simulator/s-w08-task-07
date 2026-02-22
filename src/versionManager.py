"""
Version Manager — tracks versions and generates version tags.

Author: Meera Sharma (Release team)
Last Modified: 2026-03-25
"""

from typing import Dict, List, Optional


class VersionManager:
    """Tracks release versions and generates tags."""

    def __init__(self):
        self.versions: List[Dict] = []

    def record_release(self, version: str, notes: str, commit_count: int):
        """Record a new release."""
        self.versions.append({
            'version': version,
            'notes': notes,
            'commit_count': commit_count,
            'index': len(self.versions),
        })

    def get_latest(self) -> Optional[Dict]:
        if not self.versions:
            return None
        return self.versions[-1]

    def get_version(self, version: str) -> Optional[Dict]:
        for v in self.versions:
            if v['version'] == version:
                return v
        return None

    def get_all_versions(self) -> List[str]:
        return [v['version'] for v in self.versions]

    def compare_versions(self, v1: str, v2: str) -> int:
        """Compare two semantic versions. Returns -1, 0, or 1."""
        parts1 = [int(p) for p in v1.split('.')]
        parts2 = [int(p) for p in v2.split('.')]

        for a, b in zip(parts1, parts2):
            if a < b:
                return -1
            if a > b:
                return 1
        return 0
