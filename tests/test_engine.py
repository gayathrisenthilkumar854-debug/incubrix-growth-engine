"""Comprehensive Test Suite for the IncuBrix Content Engine."""
import os
import shutil
import pytest

from engine.config import load_config
from engine.guardrails import GuardrailValidator
from engine.deduplicator import ContentDeduplicator
from engine.cost_calculator import CostCalculator
from engine.generator import ContentGenerator
from engine.exporter import AssetExporter
from engine.cli import run_pipeline

SAMPLE_CONFIG = {
    "brand_name": "IncuBrix",
    "brand_voice": {
        "banned_words": ["revolutionary", "game-changing", "magic"],
        "preferred_terms": ["CreatorOps", "operating leverage"]
    },
    "guardrails": {
        "require_utm_links": True,
        "require_ai_disclosure": True,
        "max_hook_words": 18,
        "max_video_duration_seconds": 60,
        "min_assets_per_run": 10
    }
}

def test_config_loading():
    config = load_config()
    assert "brand_name" in config
    assert "brand_voice" in config
    assert "guardrails" in config
    assert "banned_words" in config["brand_voice"]

def test_guardrail_validator_clean_asset():
    validator = GuardrailValidator(SAMPLE_CONFIG)
    asset = {
        "hook": "Stop wasting 15 hours on manual video clipping.",
        "caption": "Turn 1 recording into 10 assets with IncuBrix. #CreatorOps #IncuBrix",
        "content_body": "Pragmatic breakdown of content distribution.",
        "utm": "https://incubrix.com/start?utm_source=linkedin&utm_medium=video&utm_campaign=test",
        "format": "Short Video (45s, 9:16)",
        "duration": "45s"
    }
    is_valid, issues = validator.validate_asset(asset)
    assert is_valid is True
    assert len(issues) == 0

def test_guardrail_validator_catches_banned_words():
    validator = GuardrailValidator(SAMPLE_CONFIG)
    asset = {
        "hook": "This revolutionary new tool is pure magic for creators.",
        "caption": "A game-changing platform. #IncuBrix",
        "content_body": "More magic.",
        "utm": "https://incubrix.com/start?utm_source=linkedin&utm_medium=video&utm_campaign=test",
        "format": "Post"
    }
    is_valid, issues = validator.validate_asset(asset)
    assert is_valid is False
    assert any("revolutionary" in issue for issue in issues)
    assert any("magic" in issue for issue in issues)
    assert any("game-changing" in issue for issue in issues)

def test_guardrail_sanitizer():
    validator = GuardrailValidator(SAMPLE_CONFIG)
    dirty_text = "This revolutionary tool has game-changing magic."
    clean_text = validator.sanitize_text(dirty_text)
    assert "revolutionary" not in clean_text
    assert "game-changing" not in clean_text
    assert "magic" not in clean_text
    assert "disciplined" in clean_text or "high-leverage" in clean_text

def test_guardrail_hook_length():
    validator = GuardrailValidator(SAMPLE_CONFIG)
    long_hook = " ".join(["word"] * 25)
    asset = {
        "hook": long_hook,
        "caption": "Test #IncuBrix",
        "utm": "https://incubrix.com/start?utm_source=li&utm_medium=p&utm_campaign=t"
    }
    is_valid, issues = validator.validate_asset(asset)
    assert is_valid is False
    assert any("Hook exceeds length limit" in issue for issue in issues)

def test_guardrail_missing_utm():
    validator = GuardrailValidator(SAMPLE_CONFIG)
    asset = {
        "hook": "Short hook here.",
        "caption": "Caption #IncuBrix",
        "utm": ""
    }
    is_valid, issues = validator.validate_asset(asset)
    assert is_valid is False
    assert any("Missing UTM" in issue for issue in issues)

def test_deduplicator(tmp_path):
    cache_file = os.path.join(tmp_path, "test_hashes.json")
    dedup = ContentDeduplicator(cache_file=cache_file)
    content = "You are wasting 15 hours a week hand-cutting podcast clips."
    
    assert dedup.is_duplicate("ASSET-01", content) is False
    dedup.register("ASSET-01", content)
    assert dedup.is_duplicate("ASSET-02", content) is True

def test_cost_calculator():
    calc = CostCalculator(SAMPLE_CONFIG)
    input_text = "This is a test transcript with forty words " * 20
    output_assets = [{"hook": "H", "caption": "C", "content_body": "B"} for _ in range(10)]
    
    cost = calc.calculate_run_cost(input_text, output_assets, model_name="gpt-4o-mini")
    assert cost["input_tokens"] > 0
    assert cost["output_tokens"] > 0
    assert cost["total_cost_usd"] > 0
    assert "cost_per_asset_usd" in cost

def test_generator_produces_minimum_assets():
    generator = ContentGenerator(SAMPLE_CONFIG)
    sample_text = """
    EPISODE TITLE: The CreatorOps Future
    HOST: Sarah Jenkins
    GUEST: Kamraj Subramanian
    [00:01:00] KAMRAJ: The 15-hour creator tax is completely broken. Solo creators waste 80% of their time on admin.
    [00:03:00] SARAH: What about short-form video retention?
    [00:03:15] KAMRAJ: 73% of viewers watch without sound. If your captions are in the dead zone, you lose 80% of views.
    """
    assets = generator.generate_all_assets(sample_text)
    assert len(assets) >= 10
    for a in assets:
        assert "id" in a
        assert "title" in a
        assert "hook" in a
        assert "platform" in a
        assert "utm" in a
        assert a.get("is_valid") is True

def test_exporter(tmp_path):
    output_dir = os.path.join(tmp_path, "export_test")
    exporter = AssetExporter(output_dir)
    assets = [
        {
            "id": "T-01",
            "title": "Test Title",
            "platform": "LinkedIn",
            "format": "Post",
            "hook": "Hook text",
            "content_body": "Body text",
            "caption": "Caption text",
            "hashtags": "#IncuBrix",
            "cta": "Click here",
            "utm": "https://incubrix.com/start?utm_source=li&utm_medium=p&utm_campaign=t",
            "metric": "100 clicks",
            "is_valid": True
        }
    ]
    res = exporter.export_all(assets, {"runtime_seconds": 0.1})
    assert os.path.exists(res["calendar_csv"])
    assert os.path.exists(res["manifest_json"])
    assert res["asset_files_count"] == 1

def test_cli_end_to_end(tmp_path):
    input_file = os.path.join(tmp_path, "input.txt")
    with open(input_file, "w", encoding="utf-8") as f:
        f.write("EPISODE TITLE: Test\nKAMRAJ: The creator tax is broken. 73% watch on mute.")
    output_dir = os.path.join(tmp_path, "cli_dist")
    
    code = run_pipeline(input_file, output_dir)
    assert code == 0
    assert os.path.exists(os.path.join(output_dir, "calendar.csv"))
    assert os.path.exists(os.path.join(output_dir, "manifest.json"))
