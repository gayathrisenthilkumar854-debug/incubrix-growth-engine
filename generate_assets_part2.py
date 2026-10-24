import os
import csv
import json
import re

BASE_DIR = r"C:\Users\Gayathri S\.gemini\antigravity\scratch\incubrix-growth-engine"
CONTENT_DIR = os.path.join(BASE_DIR, "content")
CAROUSELS_DIR = os.path.join(CONTENT_DIR, "carousels")
POSTS_DIR = os.path.join(CONTENT_DIR, "posts")

os.makedirs(CAROUSELS_DIR, exist_ok=True)
os.makedirs(POSTS_DIR, exist_ok=True)

# Helper function to generate clean modern SVG slides
def create_svg_slide(title, subtitle, body_bullets, slide_num, total_slides, tag="CREATOROPS BLUEPRINT"):
    bullets_svg = ""
    y_start = 580
    for i, bullet in enumerate(body_bullets):
        bullets_svg += f"""
        <g transform="translate(100, {y_start + i * 110})">
            <rect width="48" height="48" rx="12" fill="#6366F1" fill-opacity="0.15"/>
            <circle cx="24" cy="24" r="8" fill="#10B981"/>
            <text x="70" y="32" font-family="Inter, system-ui, -apple-system, sans-serif" font-size="28" font-weight="500" fill="#E2E8F0">{bullet}</text>
        </g>
        """

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">
    <defs>
        <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#0F172A"/>
            <stop offset="50%" stop-color="#111827"/>
            <stop offset="100%" stop-color="#090D16"/>
        </linearGradient>
        <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#6366F1"/>
            <stop offset="100%" stop-color="#10B981"/>
        </linearGradient>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="60" result="blur"/>
            <feComposite in="SourceGraphic" in2="blur" operator="over"/>
        </filter>
    </defs>

    <!-- Background -->
    <rect width="1080" height="1350" fill="url(#bgGrad)"/>
    
    <!-- Ambient Glow Orbs -->
    <circle cx="950" cy="150" r="280" fill="#6366F1" fill-opacity="0.18" filter="url(#glow)"/>
    <circle cx="100" cy="1200" r="240" fill="#10B981" fill-opacity="0.14" filter="url(#glow)"/>

    <!-- Header Pill / Category -->
    <g transform="translate(100, 100)">
        <rect width="280" height="48" rx="24" fill="#1E293B" stroke="#334155" stroke-width="2"/>
        <text x="140" y="31" font-family="Inter, system-ui, sans-serif" font-size="16" font-weight="700" fill="#10B981" text-anchor="middle" letter-spacing="2">{tag}</text>
    </g>

    <!-- Slide Number Indicator -->
    <g transform="translate(880, 100)">
        <rect width="100" height="48" rx="24" fill="#1E293B" stroke="#334155" stroke-width="1.5"/>
        <text x="50" y="31" font-family="Inter, system-ui, sans-serif" font-size="18" font-weight="600" fill="#94A3B8" text-anchor="middle">{slide_num} / {total_slides}</text>
    </g>

    <!-- Main Title -->
    <text x="100" y="280" font-family="Inter, system-ui, sans-serif" font-size="56" font-weight="800" fill="#FFFFFF" width="880">
        <tspan x="100" dy="0">{title[:32]}</tspan>
        <tspan x="100" dy="68">{title[32:64]}</tspan>
    </text>

    <!-- Accent Divider Bar -->
    <rect x="100" y="390" width="140" height="6" rx="3" fill="url(#accentGrad)"/>

    <!-- Subtitle / Hook Description -->
    <text x="100" y="470" font-family="Inter, system-ui, sans-serif" font-size="28" font-weight="400" fill="#94A3B8">
        <tspan x="100" dy="0">{subtitle[:55]}</tspan>
        <tspan x="100" dy="40">{subtitle[55:110]}</tspan>
    </text>

    <!-- Body Bullets / Action Steps -->
    {bullets_svg}

    <!-- Footer Branding -->
    <line x1="100" y1="1220" x2="980" y2="1220" stroke="#1E293B" stroke-width="2"/>
    <g transform="translate(100, 1250)">
        <circle cx="16" cy="16" r="16" fill="url(#accentGrad)"/>
        <text x="44" y="23" font-family="Inter, system-ui, sans-serif" font-size="20" font-weight="800" fill="#FFFFFF" letter-spacing="1">INCUBRIX</text>
        <text x="160" y="22" font-family="Inter, system-ui, sans-serif" font-size="16" font-weight="400" fill="#64748B">| CreatorOps &amp; Distribution Platform</text>
    </g>
    <text x="980" y="1272" font-family="Inter, system-ui, sans-serif" font-size="18" font-weight="600" fill="#10B981" text-anchor="end">Swipe ➔</text>
</svg>"""
    return svg

CAROUSELS = [
    {
        "id": "INC-C01",
        "title": "The Complete CreatorOps Blueprint: 1 Recording into 14 Platform Assets",
        "platform": "LinkedIn / IG Carousel",
        "pillar": "Pillar 3: CreatorOps Systems",
        "format": "Multi-page Carousel (7 Slides, 1080x1350)",
        "hook": "How top creators publish 14 high-performing assets every week from just one 45-minute recording (without hiring a 5-person team):",
        "caption": "The biggest misconception in the creator economy? Thinking you need to write and record content 7 days a week. 💡 The top 1% don't create more—they distribute smarter. Here is the complete CreatorOps Blueprint that turns 1 core conversation into 14 platform-native assets. Save this post for your next recording session! #CreatorOps #ContentStrategy #PodcastRepurposing #LinkedInGrowth #IncuBrix",
        "cta": "Download the PDF and Notion Template at incubrix.com/blueprint",
        "utm": "https://incubrix.com/blueprint?utm_source=linkedin&utm_medium=carousel&utm_campaign=INC-C01&utm_content=creatorops_blueprint",
        "metric": "300+ Document Downloads, 150+ Saves, 80+ sign-ups",
        "day": 1,
        "time": "13:00 UTC",
        "rights": "Original IncuBrix SVG vector assets; Inter Google Font; Zero third-party copyright.",
        "slides": [
            {
                "title": "The Complete CreatorOps Blueprint",
                "subtitle": "How to turn 1 weekly recording into 14 platform-native assets.",
                "bullets": ["The 1-to-14 Asset Multiplication Matrix", "Zero Burnout Content Architecture", "Save 15+ Hours of Manual Editing Every Week"]
            },
            {
                "title": "Step 1: The Core Recording",
                "subtitle": "Everything starts with 45 minutes of high-conviction dialogue.",
                "bullets": ["Focus 100% on depth and substance", "No script memorization needed", "Raw audio/video serves as the single source of truth"]
            },
            {
                "title": "Step 2: AI Ingestion & ASR",
                "subtitle": "Feed the raw file directly into IncuBrix in 54 seconds.",
                "bullets": ["Sub-millisecond word timestamp generation", "Smart acoustic noise reduction", "Automated vocabulary filtering for technical jargon"]
            },
            {
                "title": "Step 3: Multi-Format Extraction",
                "subtitle": "IncuBrix splits the transcript into 4 content streams simultaneously.",
                "bullets": ["Stream A: 6 Vertical Short Clips (9:16) with dynamic subtitles", "Stream B: 2 Tactical LinkedIn PDF Carousels", "Stream C: 4 Value-packed X / Twitter Threads", "Stream D: 1 Executive Summary Newsletter"]
            },
            {
                "title": "Step 4: The 15-Minute Review",
                "subtitle": "Quality control is human; repetitive formatting is automated.",
                "bullets": ["Verify product facts and claims", "Calibrate brand tone and voice sliders", "Select top 3 hook variations generated by AI"]
            },
            {
                "title": "Step 5: Automated Scheduling",
                "subtitle": "Sync directly to LinkedIn, YouTube Shorts, and X.",
                "bullets": ["One-click scheduled distribution queue", "Pre-set peak engagement time slots", "Automated UTM link generation for conversion tracking"]
            },
            {
                "title": "Ready to Build Your Engine?",
                "subtitle": "Stop trading hours for content. Start operating with leverage.",
                "bullets": ["Get the full Notion CreatorOps template free", "Turn your first video into 10 assets at incubrix.com", "Drop a comment with 'CREATOR' to get the PDF copy"]
            }
        ]
    },
    {
        "id": "INC-C02",
        "title": "The Repurposing Math: The True Cost of Manual Content Production",
        "platform": "LinkedIn / IG Carousel",
        "pillar": "Pillar 1: Workflow Teardowns",
        "format": "Multi-page Carousel (6 Slides, 1080x1350)",
        "hook": "We audited 50 creators producing 3 videos a week. Here is the shocking math on what manual editing actually costs:",
        "caption": "Are you spending \$4,000 a month on freelance video editors or 20 hours of your own founder time? 📊 When you break down the hourly cost of manual clipping, transcript cleaning, and resizing, manual post-production is the most expensive way to grow. Here is the exact economic breakdown and how modern CreatorOps changes the equation. #ContentROI #MarketingBudgets #Productivity #IncuBrix",
        "cta": "Calculate your repurposing cost at incubrix.com/calculator",
        "utm": "https://incubrix.com/calculator?utm_source=linkedin&utm_medium=carousel&utm_campaign=INC-C02&utm_content=repurposing_math",
        "metric": "250+ Saves, 100+ Comments, 60+ sign-ups",
        "day": 5,
        "time": "13:00 UTC",
        "rights": "Proprietary IncuBrix economic cost model; 100% rights-safe.",
        "slides": [
            {
                "title": "The Repurposing Math Breakdown",
                "subtitle": "What manual video production is actually costing your business.",
                "bullets": ["The Hidden 15-Hour Weekly Production Drain", "Freelance Editor Retainers vs. AI Leverage", "The ROI Formula for Solo Creators & Teams"]
            },
            {
                "title": "The Manual Breakdown: 17 Hours",
                "subtitle": "Where does the creator's time actually disappear every week?",
                "bullets": ["4.5 Hours: Finding clips & scrubbing timelines", "3.0 Hours: Manual subtitle timing & style fixes", "3.5 Hours: Drafting platform-native captions", "2.0 Hours: Resizing & rendering 9:16 and 4:5 assets", "4.0 Hours: Managing revisions and scheduling"]
            },
            {
                "title": "The Financial Cost: $3,600 / Mo",
                "subtitle": "Hiring an agency or mid-tier freelancer adds up fast.",
                "bullets": ["Average agency retainer: $3,000 - $5,000 / month", "Average turnaround time: 3 to 5 business days", "Inconsistent brand voice and constant revision cycles"]
            },
            {
                "title": "The IncuBrix Equation: 45 Mins",
                "subtitle": "What happens when you automate the low-leverage formatting?",
                "bullets": ["IncuBrix ingestion & multi-clip extraction: 4 minutes", "Reviewing & approving AI-generated copy: 15 minutes", "One-click cross-platform scheduling: 5 minutes", "Total time spent: under 30 minutes per week"]
            },
            {
                "title": "The 10x Operational Leverage",
                "subtitle": "Reclaim 16 hours of deep work every single week.",
                "bullets": ["Annual hours saved: 832 hours per year", "Annual cash saved: $35,000+ compared to agency retainers", "Focus 100% of your energy on client acquisition & product"]
            },
            {
                "title": "Run Your Own Content Audit",
                "subtitle": "Calculate your exact time and dollar savings in 60 seconds.",
                "bullets": ["Try the Free IncuBrix ROI Calculator", "Start with 3 free video repurpose credits", "Visit incubrix.com/calculator to see your score"]
            }
        ]
    },
    {
        "id": "INC-C03",
        "title": "The 7-Step Anatomy of a High-Retention Short-Form Clip",
        "platform": "LinkedIn / IG Carousel",
        "pillar": "Pillar 4: Creator Benchmarks",
        "format": "Multi-page Carousel (8 Slides, 1080x1350)",
        "hook": "Why do some short videos get 1M views while identical content gets stuck at 200? Here is the exact 7-step blueprint:",
        "caption": "Short-form algorithms in 2026 don't care about your production budget. They care about two things: 3-Second Retention and Average Watch Percentage. 📈 Here is the 7-step structural anatomy of clips that consistently hit 65%+ completion rates. Bookmark this framework for your next edit. #VideoMarketing #RetentionHacks #AlgorithmTips #ShortsStrategy #IncuBrix",
        "cta": "Get the Retention Checklist at incubrix.com/retention",
        "utm": "https://incubrix.com/retention?utm_source=linkedin&utm_medium=carousel&utm_campaign=INC-C03&utm_content=clip_anatomy",
        "metric": "400+ Saves, 180+ Reposts, 95+ sign-ups",
        "day": 9,
        "time": "13:00 UTC",
        "rights": "Original IncuBrix analysis; royalty-free typography and iconography.",
        "slides": [
            {
                "title": "Anatomy of a High-Retention Clip",
                "subtitle": "The 7 structural components of videos that beat the algorithm.",
                "bullets": ["Tested across 1,000+ top-performing vertical videos", "Optimized for YouTube Shorts, Reels, and TikTok", "The exact pacing blueprint from 0 to 60 seconds"]
            },
            {
                "title": "Component 1: The Visual Pattern Interrupt",
                "subtitle": "Seconds 0 to 2: Stop the downward thumb scroll instantly.",
                "bullets": ["Zero filler words ('Hey guys, welcome back')", "Immediate movement, split-screen, or zoom cut", "High-contrast hook headline in upper safe zone"]
            },
            {
                "title": "Component 2: The Curiosity Gap",
                "subtitle": "Seconds 2 to 6: Establish the unresolved question.",
                "bullets": ["State an unexpected outcome or counterintuitive truth", "Create an open cognitive loop that requires resolution", "IncuBrix auto-scores hook strength before you publish"]
            },
            {
                "title": "Component 3: Dynamic Micro-Pacing",
                "subtitle": "Seconds 6 to 20: Maintain continuous eye tracking.",
                "bullets": ["Cut audio silence > 0.3s automatically", "Kinetic 2-word subtitle bursts with color highlights", "Visual shift (zoom or angle switch) every 3.5 seconds"]
            },
            {
                "title": "Component 4: High-Density Value Delivery",
                "subtitle": "Seconds 20 to 45: Zero fluff, high-signal information.",
                "bullets": ["Provide actionable steps or tangible numbers", "Avoid abstract conceptual theory", "Show the real screen, spreadsheet, or workflow in action"]
            },
            {
                "title": "Component 5: The Loop Trigger",
                "subtitle": "Seconds 45 to 55: Seamlessly connect the end to the start.",
                "bullets": ["Make the final sentence grammatically flow into the hook", "Encourage viewers to watch a second time unconsciously", "Boosts average watch time past 100%"]
            },
            {
                "title": "Component 6: Platform-Safe Framing",
                "subtitle": "Never let UI buttons cover your key messaging.",
                "bullets": ["Keep captions between Y:400 and Y:1400 pixels", "Clear the right-hand interaction panel margin", "IncuBrix automatically overlays native platform guidelines"]
            },
            {
                "title": "Automate the 7 Steps with IncuBrix",
                "subtitle": "Don't spend 2 hours timing micro-cuts by hand.",
                "bullets": ["Auto-silence removal and dynamic zoom framing", "AI-powered hook scoring and safe-zone alignment", "Generate your first 5 high-retention clips free at incubrix.com"]
            }
        ]
    },
    {
        "id": "INC-C04",
        "title": "The B2B Podcaster's Distribution Engine (SOP Inside)",
        "platform": "LinkedIn / IG Carousel",
        "pillar": "Pillar 3: CreatorOps Systems",
        "format": "Multi-page Carousel (6 Slides, 1080x1350)",
        "hook": "If your B2B podcast gets fewer than 500 downloads per episode, your problem isn't the audio. It's distribution:",
        "caption": "Most B2B podcasts are corporate graveyards: great conversations recorded, uploaded to Apple Podcasts, and left to die. 🎙️ High-growth B2B brands treat the podcast as an raw asset generator, not an end product. Here is the step-by-step SOP to turn 1 executive interview into 20 pipeline-generating social touchpoints. #B2BMarketing #PodcastDistribution #DemandGen #IncuBrix",
        "cta": "Get the full B2B Distribution SOP at incubrix.com/b2b-sop",
        "utm": "https://incubrix.com/b2b-sop?utm_source=linkedin&utm_medium=carousel&utm_campaign=INC-C04&utm_content=b2b_distribution_sop",
        "metric": "320+ Downloads, 140+ Saves, 70+ sign-ups",
        "day": 15,
        "time": "13:00 UTC",
        "rights": "Proprietary IncuBrix distribution framework; commercial safe typography.",
        "slides": [
            {
                "title": "The B2B Podcaster's Distribution Engine",
                "subtitle": "Turn 1 executive interview into 20 pipeline-generating assets.",
                "bullets": ["The Modern Content Pipeline for SaaS & Agencies", "How to Extract Thought Leadership Automatically", "Step-by-Step Operating Procedure (SOP)"]
            },
            {
                "title": "Phase 1: Ingestion & Speaker Identification",
                "subtitle": "Separate the host questions from guest wisdom.",
                "bullets": ["Automated multi-speaker diarization", "Extract high-impact quotes and framework definitions", "Generate executive summary notes in 60 seconds"]
            },
            {
                "title": "Phase 2: The Multi-Asset Matrix",
                "subtitle": "Repurpose into 5 distinct B2B asset classes.",
                "bullets": ["3 Vertical video clips highlighting contrarian opinions", "1 PDF Slide Deck breaking down the guest's framework", "2 Founder LinkedIn posts ghostwritten from transcripts", "1 Tactical weekly email newsletter for subscribers"]
            },
            {
                "title": "Phase 3: The Guest Amplification Pack",
                "subtitle": "Make it effortless for high-profile guests to share.",
                "bullets": ["Generate a pre-formatted 'Guest Kit' in 1 click", "Include pre-cut vertical clips, ready-to-post copy, and tags", "Increase guest co-marketing participation by 400%"]
            },
            {
                "title": "Phase 4: Demand Gen & Pipeline Tracking",
                "subtitle": "Connect social impressions directly to qualified demos.",
                "bullets": ["Embed custom UTM tracking links in all assets", "Route traffic to interactive tools and case studies", "Turn passive listeners into enterprise software leads"]
            },
            {
                "title": "Implement the SOP Next Monday",
                "subtitle": "Get the complete distribution system running in 30 minutes.",
                "bullets": ["Download the pre-built IncuBrix SOP document", "Connect your podcast RSS feed or video files", "Scale your B2B reach at incubrix.com/b2b-sop"]
            }
        ]
    },
    {
        "id": "INC-C05",
        "title": "5 High-Converting Hook Frameworks for Video & Text",
        "platform": "LinkedIn / IG Carousel",
        "pillar": "Pillar 4: Creator Benchmarks",
        "format": "Multi-page Carousel (7 Slides, 1080x1350)",
        "hook": "Steal these 5 psychological hook formulas to double your click-through rates and watch time:",
        "caption": "Your content is only as good as the first sentence. If the hook fails, the rest of your post never gets read. 🪝 We battle-tested 50+ hook variations across LinkedIn and short-form video. These 5 psychological frameworks outperformed all others by an average of 2.8x. Swipe through, save the templates, and use them on your next post! #HookFormulas #CopywritingTips #ContentMarketing #IncuBrix",
        "cta": "Get the 50 Hook Swipe File at incubrix.com/hooks",
        "utm": "https://incubrix.com/hooks?utm_source=linkedin&utm_medium=carousel&utm_campaign=INC-C05&utm_content=5_hook_frameworks",
        "metric": "500+ Saves, 220+ Reposts, 110+ sign-ups",
        "day": 22,
        "time": "13:00 UTC",
        "rights": "Original IncuBrix copywriting research; royalty-free graphics.",
        "slides": [
            {
                "title": "5 High-Converting Hook Frameworks",
                "subtitle": "Battle-tested formulas for vertical video and written posts.",
                "bullets": ["Based on 2.4M organic impressions", "Engineered for high CTR and dwell time", "Ready-to-use plug-and-play templates"]
            },
            {
                "title": "Framework 1: The Contrarian Reality",
                "subtitle": "Challenge conventional wisdom immediately.",
                "bullets": ["Formula: 'Stop [Doing Common Practice]. Here is what top 1% do instead.'", "Why it works: Triggers fear of obsolescence and curiosity", "Example: 'Stop editing podcast clips in Premiere until you watch this.'"]
            },
            {
                "title": "Framework 2: The Direct Cost Audit",
                "subtitle": "Quantify the exact dollar or time penalty.",
                "bullets": ["Formula: 'You are losing $[X] / [Y] hours every week by [Mistake].'", "Why it works: Loss aversion is 2x more motivating than gain", "Example: 'You are wasting 14 hours every week on manual subtitles.'"]
            },
            {
                "title": "Framework 3: The Secret Weapon / Tear-Down",
                "subtitle": "Reveal the hidden mechanism behind big results.",
                "bullets": ["Formula: 'The exact [System/Tool] behind [Specific Big Outcome]:'", "Why it works: Promises tangible insider knowledge", "Example: 'The 30-minute CreatorOps engine behind 120 monthly posts.'"]
            },
            {
                "title": "Framework 4: The Speed Challenge",
                "subtitle": "Deliver immediate proof against the clock.",
                "bullets": ["Formula: 'Watch this timer: [Complex Task] done in [Seconds].'", "Why it works: High visual engagement and skepticism resolution", "Example: 'Watch me turn 1 Zoom recording into 10 clips in 28 seconds.'"]
            },
            {
                "title": "Framework 5: The Checklist / Guardrail",
                "subtitle": "Provide instant diagnostic value.",
                "bullets": ["Formula: 'If your [Asset] has [Mistake], 70% of people swipe away.'", "Why it works: Prompts the reader to self-evaluate immediately", "Example: 'If your captions are in the dead zone, retention drops 50%.'"]
            },
            {
                "title": "Generate All 5 Hooks Automatically",
                "subtitle": "Let IncuBrix AI draft and score these hooks for your content.",
                "bullets": ["Upload any video or audio file", "Get 5 scored hook variations in under 60 seconds", "Try it free at incubrix.com/hooks"]
            }
        ]
    }
]

# Generate Carousel Markdown & SVG Files
for c in CAROUSELS:
    c_folder = os.path.join(CAROUSELS_DIR, c["id"])
    os.makedirs(c_folder, exist_ok=True)
    
    total_slides = len(c["slides"])
    svg_files = []
    
    for i, slide in enumerate(c["slides"], 1):
        svg_filename = f"slide_{i}.svg"
        svg_path = os.path.join(c_folder, svg_filename)
        svg_content = create_svg_slide(
            title=slide["title"],
            subtitle=slide["subtitle"],
            body_bullets=slide["bullets"],
            slide_num=i,
            total_slides=total_slides,
            tag=c["pillar"].upper()
        )
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        svg_files.append(svg_filename)

    # Write Carousel Markdown master file
    md_path = os.path.join(c_folder, "README.md")
    md_content = f"""# {c['id']}: {c['title']}

**Platform:** {c['platform']}  
**Pillar:** {c['pillar']}  
**Format:** {c['format']}  
**Scheduled Slot:** Day {c['day']} at {c['time']}  
**Target Metric:** {c['metric']}  
**Rights & Safety:** {c['rights']}  

---

### The Hook (Opening Slide)
> "{c['hook']}"

---

### Slide-by-Slide Copy & Layout Specification

"""
    for i, slide in enumerate(c["slides"], 1):
        md_content += f"""#### Slide {i} of {total_slides}: {slide['title']}
* **Header / Category:** `{c['pillar'].upper()}`
* **Headline:** {slide['title']}
* **Sub-headline:** {slide['subtitle']}
* **Bullet Points / Action Steps:**
"""
        for b in slide["bullets"]:
            md_content += f"  - {b}\n"
        md_content += f"* **Editable Vector Source:** [`slide_{i}.svg`](./slide_{i}.svg)\n\n"

    md_content += f"""---

### Publishing Caption & Hashtags
```text
{c['caption']}
```

---

### Call to Action & UTM Link
* **Call to Action:** {c['cta']}
* **UTM Tracking URL:** [{c['utm']}]({c['utm']})

---

### Visual Design Specifications
* **Canvas Resolution:** 1080 x 1350 px (4:5 Portrait Ratio, optimized for LinkedIn Document Carousel & Instagram)
* **Brand Color Palette:**
  - Background Gradient: Deep Slate `#0F172A` to Dark Charcoal `#090D16`
  - Primary Highlight / Brand Gradient: Electric Violet `#6366F1` to Emerald Teal `#10B981`
  - High-Contrast Text: Pure White `#FFFFFF` for titles, Slate Gray `#94A3B8` for secondary text
* **Typography:** Inter Bold (800) for headlines, Inter Regular (400) & Medium (500) for body copy.
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

print(f"Generated {len(CAROUSELS)} Carousel packages with SVG slides in {CAROUSELS_DIR}")
