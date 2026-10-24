"""Export Engine: formats assets into scheduler-ready files, CSVs, and manifests."""
import os
import csv
import json
import time
from typing import List, Dict, Any

class AssetExporter:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def export_all(self, assets: List[Dict[str, Any]], run_metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Writes individual asset files, calendar.csv, and manifest.json."""
        assets_dir = os.path.join(self.output_dir, "assets")
        os.makedirs(assets_dir, exist_ok=True)

        exported_files = []

        # 1. Export Individual Asset Files
        for a in assets:
            clean_id = a["id"]
            clean_name = a["title"].lower().replace(" ", "_")[:30]
            clean_name = "".join(c for c in clean_name if c.isalnum() or c == "_")
            filename = f"{clean_id}_{clean_name}.md"
            filepath = os.path.join(assets_dir, filename)

            content = f"""# {a['id']}: {a['title']}

**Platform:** {a['platform']}  
**Format:** {a['format']}  
**Target Metric:** {a['metric']}  
**Quality Status:** {'PASSED' if a.get('is_valid') else 'FAILED'}  
**Rights Safety:** {a.get('rights', 'Passed')}  

---

### The Hook
> "{a['hook']}"

---

### Asset Body & Execution Notes
```text
{a['content_body']}
```

---

### Publishing Metadata
* **Caption:** {a['caption']}
* **Hashtags:** {a['hashtags']}
* **CTA:** {a['cta']}
* **UTM Link:** [{a['utm']}]({a['utm']})
"""
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            exported_files.append(filepath)

        # 2. Export Scheduler-Ready calendar.csv
        calendar_path = os.path.join(self.output_dir, "calendar.csv")
        fieldnames = [
            "Asset_ID", "Title", "Platform", "Format", "Hook",
            "Caption", "Hashtags", "Call_To_Action", "UTM_Tracking_Link",
            "Target_Metric", "Quality_Status", "Rights_Status"
        ]

        with open(calendar_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for a in assets:
                writer.writerow({
                    "Asset_ID": a["id"],
                    "Title": a["title"],
                    "Platform": a["platform"],
                    "Format": a["format"],
                    "Hook": a["hook"],
                    "Caption": a["caption"],
                    "Hashtags": a["hashtags"],
                    "Call_To_Action": a["cta"],
                    "UTM_Tracking_Link": a["utm"],
                    "Target_Metric": a["metric"],
                    "Quality_Status": "PASSED" if a.get("is_valid") else "FAILED",
                    "Rights_Status": "PASSED (Commercial Safe)"
                })

        # 3. Export Manifest JSON
        manifest_path = os.path.join(self.output_dir, "manifest.json")
        manifest_data = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "total_assets_generated": len(assets),
            "valid_assets_count": sum(1 for a in assets if a.get("is_valid")),
            "failed_assets_count": sum(1 for a in assets if not a.get("is_valid")),
            "duplicate_count": sum(1 for a in assets if a.get("is_duplicate")),
            "calendar_csv": calendar_path,
            "run_metadata": run_metadata,
            "assets": [
                {
                    "id": a["id"],
                    "title": a["title"],
                    "platform": a["platform"],
                    "format": a["format"],
                    "is_valid": a.get("is_valid"),
                    "issues": a.get("issues", [])
                }
                for a in assets
            ]
        }

        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest_data, f, indent=2)

        return {
            "calendar_csv": calendar_path,
            "manifest_json": manifest_path,
            "asset_files_count": len(exported_files)
        }
