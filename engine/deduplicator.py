"""SHA-256 Content Deduplication and Idempotency Engine."""
import os
import json
import hashlib
from typing import Dict, Any, List

class ContentDeduplicator:
    def __init__(self, cache_file: str = "content_hashes.json"):
        self.cache_file = cache_file
        self.seen_hashes = self._load_cache()

    def _load_cache(self) -> Dict[str, str]:
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _save_cache(self):
        with open(self.cache_file, "w", encoding="utf-8") as f:
            json.dump(self.seen_hashes, f, indent=2)

    def compute_hash(self, content: str) -> str:
        """Generates a normalized SHA-256 digest of normalized text."""
        normalized = " ".join(content.lower().strip().split())
        return hashlib.sha256(normalized.encode("utf-8")).hexdigest()

    def is_duplicate(self, asset_id: str, content: str) -> bool:
        """Checks if content has been generated before under any asset ID."""
        content_hash = self.compute_hash(content)
        if content_hash in self.seen_hashes:
            return True
        return False

    def register(self, asset_id: str, content: str):
        """Registers a newly validated asset content hash."""
        content_hash = self.compute_hash(content)
        self.seen_hashes[content_hash] = asset_id
        self._save_cache()

    def reset(self):
        """Clears the deduplication cache."""
        self.seen_hashes = {}
        if os.path.exists(self.cache_file):
            os.remove(self.cache_file)
