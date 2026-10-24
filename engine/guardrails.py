"""Brand Voice Guardrails and Quality Assurance Validator."""
import re
from typing import Dict, List, Any, Tuple

class GuardrailValidator:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.banned_words = [w.lower() for w in config.get("brand_voice", {}).get("banned_words", [])]
        self.preferred_terms = config.get("brand_voice", {}).get("preferred_terms", [])
        self.max_hook_words = config.get("guardrails", {}).get("max_hook_words", 18)
        self.require_utm = config.get("guardrails", {}).get("require_utm_links", True)
        self.require_disclosure = config.get("guardrails", {}).get("require_ai_disclosure", True)

    def validate_asset(self, asset: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validates a single asset against all brand and platform rules."""
        issues = []
        
        # 1. Banned Words Check
        full_text = f"{asset.get('hook', '')} {asset.get('caption', '')} {asset.get('content_body', '')}".lower()
        for banned in self.banned_words:
            if re.search(r'\b' + re.escape(banned) + r'\b', full_text):
                issues.append(f"Contains banned hype term: '{banned}'")

        # 2. Hook Strength Check
        hook = asset.get("hook", "").strip()
        if not hook:
            issues.append("Hook is missing or empty")
        else:
            word_count = len(hook.split())
            if word_count > self.max_hook_words:
                issues.append(f"Hook exceeds length limit ({word_count} words > {self.max_hook_words} words)")

        # 3. UTM Link Verification
        if self.require_utm:
            utm = asset.get("utm", "") or asset.get("utm_link", "")
            if not utm:
                issues.append("Missing UTM tracking link")
            elif not ("utm_source=" in utm and "utm_medium=" in utm and "utm_campaign=" in utm):
                issues.append(f"Incomplete UTM parameters in link: {utm}")

        # 4. Rights and Disclosure Check
        if self.require_disclosure:
            text_to_check = f"{asset.get('caption', '')} {asset.get('hashtags', '')}"
            if not ("IncuBrix" in text_to_check or "AI" in text_to_check):
                issues.append("Missing platform-compliant brand or AI attribution tag")

        # 5. Video Duration Check
        if "video" in asset.get("format", "").lower():
            duration_str = str(asset.get("duration", "60s"))
            match = re.search(r'(\d+)', duration_str)
            if match and int(match.group(1)) > 60:
                issues.append(f"Video duration ({duration_str}) exceeds 60-second limit")

        is_passed = len(issues) == 0
        return is_passed, issues

    def sanitize_text(self, text: str) -> str:
        """Removes banned words and replaces them with preferred professional terms."""
        sanitized = text
        replacements = {
            "revolutionary": "disciplined",
            "game-changing": "high-leverage",
            "magic": "automation",
            "synergy": "alignment",
            "unleash": "scale",
            "effortless": "streamlined",
            "miraculous": "predictable",
            "10x your output": "multiply your throughput"
        }
        for bad, good in replacements.items():
            pattern = re.compile(r'\b' + re.escape(bad) + r'\b', re.IGNORECASE)
            sanitized = pattern.sub(good, sanitized)
        return sanitized
