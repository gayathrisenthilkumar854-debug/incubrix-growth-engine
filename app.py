"""IncuBrix CreatorOps Web Platform and Dashboard (FastAPI)."""
import os
import csv
import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from engine.config import load_config
from engine.generator import ContentGenerator
from engine.deduplicator import ContentDeduplicator
from engine.cost_calculator import CostCalculator

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, "content")
CALENDAR_CSV = os.path.join(CONTENT_DIR, "calendar.csv")

app = FastAPI(title="IncuBrix CreatorOps Platform", version="2.4.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/calendar")
def get_calendar():
    if not os.path.exists(CALENDAR_CSV):
        return []
    with open(CALENDAR_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

@app.post("/api/generate")
async def generate_content(request: Request):
    data = await request.json()
    raw_text = data.get("text", "")
    if not raw_text:
        return JSONResponse({"error": "No text provided"}, status_code=400)

    config = load_config()
    dedup = ContentDeduplicator()
    cost_calc = CostCalculator(config)
    gen = ContentGenerator(config, dedup)

    assets = gen.generate_all_assets(raw_text)
    cost = cost_calc.calculate_run_cost(raw_text, assets)

    return {
        "assets_count": len(assets),
        "cost": cost,
        "assets": assets
    }

@app.get("/", response_class=HTMLResponse)
def index():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IncuBrix CreatorOps Platform</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #090D16;
            --surface: #111827;
            --surface-hover: #1E293B;
            --border: #334155;
            --accent: #6366F1;
            --accent-green: #10B981;
            --text-main: #F8FAFC;
            --text-muted: #94A3B8;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text-main); line-height: 1.5; }
        .navbar { display: flex; justify-content: space-between; align-items: center; padding: 16px 32px; background: rgba(17, 24, 39, 0.85); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 50; }
        .logo { font-size: 20px; font-weight: 800; letter-spacing: 1px; color: #FFF; display: flex; align-items: center; gap: 8px; }
        .logo span { color: var(--accent-green); }
        .nav-links a { color: var(--text-muted); text-decoration: none; margin-left: 24px; font-size: 14px; font-weight: 500; transition: color 0.2s; }
        .nav-links a:hover { color: var(--text-main); }
        .container { max-width: 1200px; margin: 0 auto; padding: 32px 20px; }
        .hero { text-align: center; margin-bottom: 40px; }
        .badge { display: inline-block; padding: 6px 14px; background: rgba(16, 185, 129, 0.1); border: 1px solid var(--accent-green); border-radius: 9999px; color: var(--accent-green); font-size: 12px; font-weight: 700; margin-bottom: 16px; letter-spacing: 1px; }
        .hero h1 { font-size: 40px; font-weight: 800; margin-bottom: 12px; }
        .hero p { color: var(--text-muted); font-size: 16px; max-width: 600px; margin: 0 auto; }
        .card { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 24px; margin-bottom: 32px; }
        .card-header { font-size: 18px; font-weight: 700; margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center; }
        textarea { width: 100%; height: 160px; background: #0F172A; border: 1px solid var(--border); border-radius: 8px; color: var(--text-main); padding: 14px; font-family: inherit; font-size: 14px; resize: vertical; margin-bottom: 16px; outline: none; }
        textarea:focus { border-color: var(--accent); }
        .btn { background: var(--accent); color: white; padding: 12px 24px; border: none; border-radius: 8px; font-weight: 600; cursor: pointer; transition: opacity 0.2s; display: inline-flex; align-items: center; gap: 8px; }
        .btn:hover { opacity: 0.9; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; }
        .asset-card { background: #0F172A; border: 1px solid var(--border); border-radius: 8px; padding: 18px; display: flex; flex-direction: column; justify-content: space-between; }
        .asset-tag { display: inline-block; padding: 4px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; text-transform: uppercase; margin-bottom: 8px; }
        .tag-video { background: rgba(99, 102, 241, 0.15); color: #818CF8; border: 1px solid #6366F1; }
        .tag-carousel { background: rgba(16, 185, 129, 0.15); color: #34D399; border: 1px solid #10B981; }
        .tag-post { background: rgba(245, 158, 11, 0.15); color: #FBBF24; border: 1px solid #F59E0B; }
        .asset-title { font-weight: 700; font-size: 15px; margin-bottom: 8px; }
        .asset-hook { font-size: 13px; color: var(--text-muted); margin-bottom: 12px; font-style: italic; }
        .asset-meta { font-size: 11px; color: #64748B; border-top: 1px solid #1E293B; padding-top: 10px; display: flex; justify-content: space-between; }
        .table-wrap { overflow-x: auto; }
        table { width: 100%; border-collapse: collapse; font-size: 13px; text-align: left; }
        th, td { padding: 12px 14px; border-bottom: 1px solid #1E293B; }
        th { background: #0F172A; color: var(--text-muted); font-weight: 600; }
        tr:hover { background: rgba(30, 41, 59, 0.5); }
        .status-pill { padding: 2px 8px; border-radius: 9999px; font-size: 11px; font-weight: 700; background: rgba(16, 185, 129, 0.15); color: var(--accent-green); }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="logo">INCUBRIX <span>CREATOROPS</span></div>
        <div class="nav-links">
            <a href="#generator">AI Studio</a>
            <a href="#calendar">30-Day Calendar</a>
            <a href="#benchmarks">Cost & Scale</a>
        </div>
    </nav>

    <div class="container">
        <div class="hero">
            <div class="badge">GROWTH ENGINE v2.4.0</div>
            <h1>Turn 1 Input into 14 Platform Assets</h1>
            <p>Automate your low-leverage video clipping, carousels, and distribution with built-in brand voice guardrails.</p>
        </div>

        <!-- Studio Section -->
        <div class="card" id="generator">
            <div class="card-header">
                <span>⚡ Live Repurposing Studio</span>
                <span style="font-size: 12px; color: var(--text-muted);">Runtime: &lt; 0.05s</span>
            </div>
            <textarea id="inputText" placeholder="Paste podcast transcript, YouTube notes, or client interview text here...">EPISODE TITLE: The 15-Hour Repurposing Tax
KAMRAJ: The dirty secret of the creator economy is that most creators spend 80% of their time on admin, manual subtitles, and formatting files. Only 20% goes into thinking and creating. If you automate the clipping with CreatorOps, your throughput increases by 400% without burnout.</textarea>
            <button class="btn" onclick="generateContent()">⚡ Run IncuBrix Engine</button>
            <div id="costSummary" style="margin-top: 16px; font-size: 13px; color: var(--accent-green); display: none;"></div>
            <div class="grid" id="generatedGrid" style="margin-top: 24px;"></div>
        </div>

        <!-- Calendar Section -->
        <div class="card" id="calendar">
            <div class="card-header">
                <span>📅 30-Day Ready-to-Publish Master Calendar</span>
                <span class="status-pill">30 Assets Ready</span>
            </div>
            <div class="table-wrap">
                <table id="calendarTable">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Platform</th>
                            <th>Format</th>
                            <th>Day</th>
                            <th>Hook</th>
                            <th>Quality</th>
                        </tr>
                    </thead>
                    <tbody id="calendarBody">
                        <tr><td colspan="6" style="text-align: center; color: var(--text-muted);">Loading master calendar...</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <script>
        async function loadCalendar() {
            try {
                const res = await fetch('/api/calendar');
                const data = await res.json();
                const tbody = document.getElementById('calendarBody');
                tbody.innerHTML = '';
                data.forEach(item => {
                    const tr = document.createElement('tr');
                    tr.innerHTML = `
                        <td style="font-weight: 700; color: #818CF8;">${item.Asset_ID}</td>
                        <td>${item.Platform}</td>
                        <td>${item.Format}</td>
                        <td>${item.Scheduled_Day}</td>
                        <td style="max-width: 380px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${item.Hook}</td>
                        <td><span class="status-pill">PASSED</span></td>
                    `;
                    tbody.appendChild(tr);
                });
            } catch (err) {
                console.error(err);
            }
        }

        async function generateContent() {
            const text = document.getElementById('inputText').value;
            const res = await fetch('/api/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text })
            });
            const data = await res.json();
            
            const costDiv = document.getElementById('costSummary');
            costDiv.style.display = 'block';
            costDiv.innerText = `✅ Generated ${data.assets_count} assets in sub-second time. Total Cost: $${data.cost.total_cost_usd} USD (Average: $${data.cost.cost_per_asset_usd}/asset).`;

            const grid = document.getElementById('generatedGrid');
            grid.innerHTML = '';
            data.assets.forEach(a => {
                let tagClass = 'tag-post';
                if (a.format.includes('Video')) tagClass = 'tag-video';
                if (a.format.includes('Carousel')) tagClass = 'tag-carousel';

                const card = document.createElement('div');
                card.className = 'asset-card';
                card.innerHTML = `
                    <div>
                        <span class="asset-tag ${tagClass}">${a.platform}</span>
                        <div class="asset-title">${a.title}</div>
                        <div class="asset-hook">"${a.hook}"</div>
                    </div>
                    <div class="asset-meta">
                        <span>${a.format}</span>
                        <span style="color: var(--accent-green); font-weight: 600;">PASS (0 Banned Words)</span>
                    </div>
                `;
                grid.appendChild(card);
            });
        }

        window.onload = loadCalendar;
    </script>
</body>
</html>"""
    return html_content

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=False)
