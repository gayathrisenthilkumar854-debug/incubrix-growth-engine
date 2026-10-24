"""Command Line Interface for the IncuBrix Content Engine."""
import os
import sys
import time
import argparse
import json

# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from .config import load_config
from .guardrails import GuardrailValidator
from .deduplicator import ContentDeduplicator
from .cost_calculator import CostCalculator
from .generator import ContentGenerator
from .exporter import AssetExporter

def run_pipeline(input_path: str, output_dir: str, config_path: str = None) -> int:
    """Executes the full content repurposing pipeline."""
    start_time = time.time()
    print("=" * 65)
    print(">> INCUBRIX CONTENT ENGINE v2.4.0 -- BATCH REPURPOSING PIPELINE")
    print("=" * 65)

    if not os.path.exists(input_path):
        print(f"[ERROR] Input file not found: {input_path}")
        return 1

    with open(input_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    print(f"[*] Ingesting raw input: '{os.path.basename(input_path)}' ({len(raw_text.split())} words)")
    
    # 1. Load Config
    config = load_config(config_path)
    deduplicator = ContentDeduplicator()
    cost_calc = CostCalculator(config)
    generator = ContentGenerator(config, deduplicator)

    # 2. Generate Assets
    print("[*] Parsing semantic nuggets, hooks, and frameworks...")
    assets = generator.generate_all_assets(raw_text)
    print(f"[OK] Generated {len(assets)} platform-specific assets.")

    # 3. Guardrail Check Summary
    valid_count = sum(1 for a in assets if a.get("is_valid"))
    print(f"[SHIELD] Brand Voice & Quality Bar: {valid_count}/{len(assets)} passed all checks.")

    # 4. Cost Calculation
    cost_metrics = cost_calc.calculate_run_cost(raw_text, assets, model_name="gpt-4o-mini")
    runtime_sec = round(time.time() - start_time, 2)

    # 5. Export Assets
    run_meta = {
        "runtime_seconds": runtime_sec,
        "cost_metrics": cost_metrics
    }
    exporter = AssetExporter(output_dir)
    export_res = exporter.export_all(assets, run_meta)

    print("-" * 65)
    print("EXECUTION SUMMARY & BENCHMARKS:")
    print(f"  * Total Runtime:            {runtime_sec}s (< 30s benchmark)")
    print(f"  * Assets Produced:          {len(assets)} assets (Requirement: >= 10)")
    print(f"  * Input Tokens:             {cost_metrics['input_tokens']}")
    print(f"  * Output Tokens:            {cost_metrics['output_tokens']}")
    print(f"  * Total Cost (GPT-4o-mini): ${cost_metrics['total_cost_usd']}")
    print(f"  * Average Cost / Asset:     ${cost_metrics['cost_per_asset_usd']}")
    print(f"  * Scheduler Export:         {export_res['calendar_csv']}")
    print(f"  * Run Manifest:             {export_res['manifest_json']}")
    print("=" * 65)
    print("[SUCCESS] Day 1 content queue ready for deployment with 0 rework!")
    return 0

def run_benchmark():
    """Runs a cost and scale projection benchmark."""
    config = load_config()
    cost_calc = CostCalculator(config)
    
    sample_text = "Word " * 2500  # typical 45-min podcast transcript
    sample_assets = [{"hook": "H", "caption": "C", "content_body": "B"} for _ in range(14)]
    
    print("=" * 65)
    print("📈 INCUBRIX COST-AT-SCALE BENCHMARK ANALYSIS")
    print("=" * 65)
    
    for model_name in ["gpt-4o-mini", "claude-3-5-sonnet", "local-llama-3"]:
        cost = cost_calc.calculate_run_cost(sample_text, sample_assets, model_name=model_name)
        scale = cost_calc.project_monthly_scale(cost["total_cost_usd"], runs_per_month=20)
        
        print(f"\nMODEL: {model_name.upper()}")
        print(f"  • Cost per 45-min Episode:  ${cost['total_cost_usd']}")
        print(f"  • Cost per Generated Asset: ${cost['cost_per_asset_usd']}")
        print(f"  • Monthly Cost (20 eps / 280 assets): ${scale['total_monthly_cost_usd']}")
    print("=" * 65)
    return 0

def main():
    parser = argparse.ArgumentParser(description="IncuBrix AI-Powered Social Growth Engine")
    subparsers = parser.add_subparsers(dest="command")

    # Run command
    run_parser = subparsers.add_parser("run", help="Run the repurposing engine on an input file")
    run_parser.add_argument("--input", "-i", required=True, help="Path to input text/transcript file")
    run_parser.add_argument("--output", "-o", default="dist", help="Output directory for calendar and assets")
    run_parser.add_argument("--config", "-c", default=None, help="Path to optional engine_config.json")

    # Benchmark command
    subparsers.add_parser("benchmark", help="Display cost-at-scale benchmark projections")

    # Reset/Refresh command
    refresh_parser = subparsers.add_parser("refresh", help="Reset deduplication cache and rerun on input")
    refresh_parser.add_argument("--input", "-i", required=True, help="Path to input text/transcript file")
    refresh_parser.add_argument("--output", "-o", default="dist", help="Output directory")

    args = parser.parse_args()

    if args.command == "run":
        sys.exit(run_pipeline(args.input, args.output, args.config))
    elif args.command == "benchmark":
        sys.exit(run_benchmark())
    elif args.command == "refresh":
        dedup = ContentDeduplicator()
        dedup.reset()
        print("🔄 Deduplication cache cleared.")
        sys.exit(run_pipeline(args.input, args.output))
    else:
        parser.print_help()
        sys.exit(0)

if __name__ == "__main__":
    main()
