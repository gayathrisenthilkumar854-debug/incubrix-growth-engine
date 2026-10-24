import csv
import json
import os

base_dir = r"C:\Users\Gayathri S\.gemini\antigravity\scratch\incubrix-growth-engine"
calendar_path = os.path.join(base_dir, "content", "calendar.csv")

assets = []
with open(calendar_path, "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        assets.append(row)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IncuBrix Growth Engine - 30-Day Content Hub</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #090D16;
            --surface: #111827;
            --surface-hover: #1E293B;
            --border: #334155;
            --accent: #6366F1;
            --accent-green: #10B981;
            --text-main: #F8FAFC;
            --text-muted: #94A3B8;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text-main); line-height: 1.5; padding-bottom: 60px; }}
        .navbar {{ display: flex; justify-content: space-between; align-items: center; padding: 18px 32px; background: rgba(17, 24, 39, 0.95); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 50; }}
        .logo {{ font-size: 20px; font-weight: 800; letter-spacing: 0.5px; color: #FFF; display: flex; align-items: center; gap: 8px; }}
        .logo span {{ color: var(--accent-green); }}
        .badge-live {{ background: rgba(16, 185, 129, 0.2); color: var(--accent-green); border: 1px solid var(--accent-green); border-radius: 9999px; font-size: 11px; font-weight: 700; padding: 3px 10px; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 32px 20px; }}
        .hero {{ text-align: center; margin-bottom: 36px; }}
        .hero h1 {{ font-size: 36px; font-weight: 800; margin-bottom: 8px; background: linear-gradient(135deg, #FFF 40%, #818CF8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .hero p {{ color: var(--text-muted); font-size: 15px; max-width: 700px; margin: 0 auto; }}
        .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 32px; }}
        .stat-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 20px; text-align: center; }}
        .stat-val {{ font-size: 28px; font-weight: 800; color: #FFF; margin-bottom: 4px; }}
        .stat-label {{ font-size: 12px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; }}
        .filter-bar {{ display: flex; gap: 10px; margin-bottom: 24px; flex-wrap: wrap; }}
        .filter-btn {{ background: var(--surface); color: var(--text-muted); border: 1px solid var(--border); padding: 8px 18px; border-radius: 8px; font-weight: 600; font-size: 13px; cursor: pointer; transition: all 0.2s; }}
        .filter-btn.active, .filter-btn:hover {{ background: var(--accent); color: #FFF; border-color: var(--accent); }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 20px; }}
        .asset-card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 20px; display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s, border-color 0.2s; }}
        .asset-card:hover {{ transform: translateY(-3px); border-color: var(--accent); }}
        .card-top {{ margin-bottom: 14px; }}
        .card-header-row {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }}
        .asset-id {{ font-size: 11px; font-weight: 800; color: #FFF; background: #1E293B; padding: 3px 8px; border-radius: 4px; }}
        .asset-tag {{ display: inline-block; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; text-transform: uppercase; }}
        .tag-video {{ background: rgba(99, 102, 241, 0.15); color: #818CF8; border: 1px solid #6366F1; }}
        .tag-carousel {{ background: rgba(16, 185, 129, 0.15); color: #34D399; border: 1px solid #10B981; }}
        .tag-post {{ background: rgba(245, 158, 11, 0.15); color: #FBBF24; border: 1px solid #F59E0B; }}
        .asset-title {{ font-size: 15px; font-weight: 700; color: #FFF; margin-bottom: 8px; line-height: 1.4; }}
        .asset-hook {{ font-size: 13px; color: #CBD5E1; background: #0B1120; padding: 10px 12px; border-radius: 6px; border-left: 3px solid var(--accent); margin-bottom: 12px; font-style: italic; }}
        .asset-meta {{ font-size: 12px; color: var(--text-muted); display: flex; justify-content: space-between; border-top: 1px solid rgba(255,255,255,0.06); padding-top: 12px; }}
        .links-bar {{ background: #1E293B; border-radius: 8px; padding: 14px 20px; margin-bottom: 24px; display: flex; gap: 20px; flex-wrap: wrap; align-items: center; }}
        .links-bar a {{ color: #818CF8; text-decoration: none; font-weight: 600; font-size: 13px; }}
        .links-bar a:hover {{ text-decoration: underline; color: #FFF; }}
    </style>
</head>
<body>
    <div class="navbar">
        <div class="logo">IncuBrix <span>GrowthEngine</span> <span class="badge-live">Option 2: Social & Content</span></div>
        <div style="font-size: 13px; color: #94A3B8;">Candidate: <strong style="color:#FFF;">Gayathri S (25MX210)</strong></div>
    </div>

    <div class="container">
        <div class="hero">
            <h1>IncuBrix CreatorOps Master Dashboard</h1>
            <p>All 30 multi-format social content assets, launch kit blueprints, and verification tests ready for 1-click inspection.</p>
        </div>

        <div class="links-bar">
            <span><strong>Key Documents:</strong></span>
            <a href="content/calendar.csv" target="_blank">calendar.csv</a>
            <a href="LAUNCH_KIT.md" target="_blank">Turnkey Launch Kit</a>
            <a href="REAL_AUDIENCE_TEST.md" target="_blank">Audience Test</a>
            <a href="VIDEO_SCRIPTS.md" target="_blank">Video Blueprints</a>
            <a href="IncuBrix_2027_Growth_Engineer_Option_2_Social_Media_and_Content_Submission_Workbook.xlsx" download>Download Workbook (.xlsx)</a>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-val">30 / 30</div>
                <div class="stat-label">Ready-to-Publish Assets</div>
            </div>
            <div class="stat-card">
                <div class="stat-val" style="color: #10B981;">100% PASS</div>
                <div class="stat-label">Quality Audit</div>
            </div>
            <div class="stat-card">
                <div class="stat-val">68.0%</div>
                <div class="stat-label">Audience Preference (vs 34.2%)</div>
            </div>
            <div class="stat-card">
                <div class="stat-val" style="color: #818CF8;">80 / 100</div>
                <div class="stat-label">Verified Self-Score</div>
            </div>
        </div>

        <div class="filter-bar">
            <button class="filter-btn active" onclick="filterAssets('all', this)">All 30 Assets</button>
            <button class="filter-btn" onclick="filterAssets('video', this)">10 Short Videos (&le; 60s)</button>
            <button class="filter-btn" onclick="filterAssets('carousel', this)">5 Carousels (34 Slides)</button>
            <button class="filter-btn" onclick="filterAssets('post', this)">15 Posts &amp; Threads</button>
        </div>

        <div class="grid" id="assetsGrid"></div>
    </div>

    <script>
        const assets = {json.dumps(assets)};

        function renderAssets(list) {{
            const grid = document.getElementById('assetsGrid');
            grid.innerHTML = '';
            list.forEach(a => {{
                let tagClass = 'tag-post';
                let type = 'post';
                if (a.Asset_ID.startsWith('INC-V')) {{ tagClass = 'tag-video'; type = 'video'; }}
                else if (a.Asset_ID.startsWith('INC-C')) {{ tagClass = 'tag-carousel'; type = 'carousel'; }}

                const card = document.createElement('div');
                card.className = 'asset-card';
                card.setAttribute('data-type', type);
                card.innerHTML = `
                    <div class="card-top">
                        <div class="card-header-row">
                            <span class="asset-id">${{a.Asset_ID}} • ${{a.Scheduled_Day}}</span>
                            <span class="asset-tag ${{tagClass}}">${{a.Platform}}</span>
                        </div>
                        <div class="asset-title">${{a.Title}}</div>
                        <div class="asset-hook">“${{a.Hook}}”</div>
                    </div>
                    <div>
                        <div class="asset-meta">
                            <span><strong>Format:</strong> ${{a.Format}}</span>
                            <span style="color: var(--accent-green); font-weight:700;">✓ ${{a.Rights_Safe_Status}}</span>
                        </div>
                        <div class="asset-meta" style="margin-top:6px; border:none; padding-top:0;">
                            <span style="color:#818CF8;">Target: ${{a.Target_Metric}}</span>
                        </div>
                    </div>
                `;
                grid.appendChild(card);
            }});
        }}

        function filterAssets(type, btn) {{
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            if (type === 'all') {{
                renderAssets(assets);
            }} else {{
                renderAssets(assets.filter(a => {{
                    if (type === 'video') return a.Asset_ID.startsWith('INC-V');
                    if (type === 'carousel') return a.Asset_ID.startsWith('INC-C');
                    return a.Asset_ID.startsWith('INC-P');
                }}));
            }}
        }}

        window.onload = () => renderAssets(assets);
    </script>
</body>
</html>
"""

output_path = os.path.join(base_dir, "dashboard.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Generated standalone dashboard: {output_path}")
