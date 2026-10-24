"""Runtime and Cost-at-Scale Calculator for the Content Engine."""
from typing import Dict, Any

class CostCalculator:
    def __init__(self, config: Dict[str, Any]):
        self.models = config.get("cost_models", {
            "gpt-4o-mini": {"input_cost_per_million_tokens": 0.15, "output_cost_per_million_tokens": 0.60},
            "claude-3-5-sonnet": {"input_cost_per_million_tokens": 3.00, "output_cost_per_million_tokens": 15.00},
            "local-llama-3": {"input_cost_per_million_tokens": 0.00, "output_cost_per_million_tokens": 0.00}
        })

    def estimate_tokens(self, text: str) -> int:
        """Rough token estimate: 1 word ≈ 1.33 tokens."""
        words = len(text.split())
        return int(words * 1.33)

    def calculate_run_cost(self, input_text: str, output_assets: list, model_name: str = "gpt-4o-mini") -> Dict[str, Any]:
        """Calculates precise execution cost for a single pipeline run."""
        model = self.models.get(model_name, self.models["gpt-4o-mini"])
        
        in_tokens = self.estimate_tokens(input_text)
        total_out_text = " ".join([
            f"{a.get('hook', '')} {a.get('caption', '')} {a.get('content_body', '')}"
            for a in output_assets
        ])
        out_tokens = self.estimate_tokens(total_out_text)

        in_cost = (in_tokens / 1_000_000) * model["input_cost_per_million_tokens"]
        out_cost = (out_tokens / 1_000_000) * model["output_cost_per_million_tokens"]
        total_cost = in_cost + out_cost

        return {
            "model": model_name,
            "input_tokens": in_tokens,
            "output_tokens": out_tokens,
            "total_tokens": in_tokens + out_tokens,
            "input_cost_usd": round(in_cost, 5),
            "output_cost_usd": round(out_cost, 5),
            "total_cost_usd": round(total_cost, 5),
            "cost_per_asset_usd": round(total_cost / max(len(output_assets), 1), 5)
        }

    def project_monthly_scale(self, single_run_cost: float, runs_per_month: int = 20) -> Dict[str, Any]:
        """Projects operational cost at monthly scale (e.g. 20 episodes/mo or 100 episodes/mo)."""
        monthly_cost = single_run_cost * runs_per_month
        assets_produced = runs_per_month * 14  # avg 14 assets per run
        cost_per_asset = monthly_cost / max(assets_produced, 1)

        return {
            "episodes_processed_per_month": runs_per_month,
            "total_assets_generated": assets_produced,
            "total_monthly_cost_usd": round(monthly_cost, 2),
            "average_cost_per_asset_usd": round(cost_per_asset, 4)
        }
