"""Configuration loader for the IncuBrix Content Engine."""
import os
import json
from typing import Dict, Any

DEFAULT_CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "engine_config.json"
)

def load_config(config_path: str = None) -> Dict[str, Any]:
    """Loads configuration from JSON file with sensible defaults."""
    path = config_path or DEFAULT_CONFIG_PATH
    if not os.path.exists(path):
        return {
            "brand_name": "IncuBrix",
            "version": "2.4.0",
            "brand_voice": {
                "banned_words": ["revolutionary", "game-changing", "magic", "synergy", "unleash", "effortless", "miraculous"],
                "preferred_terms": ["CreatorOps", "operating leverage", "repurposing throughput"]
            },
            "guardrails": {
                "require_utm_links": True,
                "require_ai_disclosure": True,
                "max_hook_words": 18,
                "max_video_duration_seconds": 60,
                "min_assets_per_run": 10
            }
        }
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
