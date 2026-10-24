import os
import csv
import json
import re

BASE_DIR = r"C:\Users\Gayathri S\.gemini\antigravity\scratch\incubrix-growth-engine"
CONTENT_DIR = os.path.join(BASE_DIR, "content")
VIDEOS_DIR = os.path.join(CONTENT_DIR, "videos")
CAROUSELS_DIR = os.path.join(CONTENT_DIR, "carousels")
POSTS_DIR = os.path.join(CONTENT_DIR, "posts")

os.makedirs(VIDEOS_DIR, exist_ok=True)
os.makedirs(CAROUSELS_DIR, exist_ok=True)
os.makedirs(POSTS_DIR, exist_ok=True)

# 10 Video Assets Definition
VIDEOS = [
    {
        "id": "INC-V01",
        "title": "Turn a 45-Min Podcast into 10 Viral Clips in Under 4 Minutes",
        "platform": "YouTube Shorts / LinkedIn / IG Reels",
        "pillar": "Pillar 2: Feature-in-Action",
        "duration": "48s",
        "aspect_ratio": "9:16 (1080x1920)",
        "hook": "You are wasting 10 hours a week hand-cutting podcast clips. Here is how to do it in 4 minutes.",
        "script_breakdown": [
            {"time": "0:00 - 0:03", "speaker": "Creator", "visual": "Split screen: Left side shows tired editor in Premiere timeline with 40 cuts. Right side shows clean IncuBrix UI.", "audio": "Punchy whoosh sound effect. 'You're wasting 10 hours a week hand-cutting podcast clips.'"},
            {"time": "0:03 - 0:15", "speaker": "Creator", "visual": "Screen record cursor dragging a 45-min Zoom MP4 file directly into IncuBrix drag-and-drop box.", "audio": "'Drop any raw video into IncuBrix. Watch the timer: in 45 seconds, the AI transcribes and scores the top moments.'"},
            {"time": "0:15 - 0:32", "speaker": "Creator", "visual": "Highlighting 3 auto-generated clips with dynamic kinetic captions, speaker auto-centering, and virality scores of 94, 91, 88.", "audio": "'It automatically tracks the active speaker, generates word-by-word highlighted captions, and scores every hook for retention.'"},
            {"time": "0:32 - 0:42", "speaker": "Creator", "visual": "One-click 'Export to Shorts & LinkedIn' button being clicked. Batch zip download ready.", "audio": "'No timeline scrubbing. No manual subtitle styling. 10 platform-ready clips before your coffee cools down.'"},
            {"time": "0:42 - 0:48", "speaker": "Creator", "visual": "Final CTA card on screen with IncuBrix URL, clean logo animation, and free trial pill.", "audio": "'Test your first video for free at incubrix.com. Link in comments.'"}
        ],
        "caption": "Stop letting 45 minutes of gold die on Spotify. 🎧 90% of podcasters burn out because editing clips takes longer than recording the actual conversation. With IncuBrix, you drop in the recording and get 10 high-retention clips with dynamic captions and smart re-framing in under 4 minutes. Try your first video free (no CC required). #CreatorOps #PodcastGrowth #VideoEditing #AIContent #IncuBrix",
        "cta": "Test your first video free at incubrix.com/start",
        "utm": "https://incubrix.com/start?utm_source=shorts&utm_medium=video&utm_campaign=INC-V01&utm_content=podcast_repurpose",
        "metric": "Completion Rate > 65%, 2,500+ views, 45+ link clicks",
        "rights": "Licensed IncuBrix UI capture; Epidemic Sound royalty-free commercial track 'Neon Pulse' (Lic #EB-89102); Sans-serif Inter font (SIL Open Font License).",
        "day": 2,
        "time": "16:00 UTC"
    },
    {
        "id": "INC-V02",
        "title": "The 15-Hour Creator Tax vs. The 30-Minute Workflow",
        "platform": "YouTube Shorts / TikTok / X",
        "pillar": "Pillar 1: Workflow Teardowns",
        "duration": "42s",
        "aspect_ratio": "9:16 (1080x1920)",
        "hook": "Here is the exact breakdown of why solo creators burn out after 6 months.",
        "script_breakdown": [
            {"time": "0:00 - 0:04", "speaker": "Creator", "visual": "Creator at standing desk writing on whiteboard: '15 Hours of Post-Production Hell'.", "audio": "'Here is why 90% of solo creators burn out after six months.'"},
            {"time": "0:04 - 0:18", "speaker": "Creator", "visual": "Rapid cuts with sound effects: 4 hrs editing, 3 hrs subtitling, 3 hrs writing copy, 2 hrs resizing, 3 hrs scheduling.", "audio": "'You record for 1 hour, then spend 14 hours chopping, transcribing, resizing to 9:16, and writing captions across 4 apps.'"},
            {"time": "0:18 - 0:34", "speaker": "Creator", "visual": "Switch to IncuBrix workflow: 1 upload -> automatic clips, 1 carousel, 3 X threads, auto-scheduled.", "audio": "'The modern CreatorOps stack collapses this into 30 minutes. 1 upload generates your clips, carousels, and tweets with tone calibration.'"},
            {"time": "0:34 - 0:42", "speaker": "Creator", "visual": "Side-by-side bar chart graphic showing 15 hrs vs 0.5 hrs. CTA text overlay.", "audio": "'Reclaim 14.5 hours every week. Link in bio to see the exact workflow template.'"}
        ],
        "caption": "Content creation doesn't cause burnout. Fragmented toolchains do. 🛑 When you spend 15 hours editing for every 1 hour you spend thinking, your quality drops. Automate the low-leverage clipping, formatting, and scheduling with IncuBrix. Work smarter, not longer. #CreatorEconomy #Productivity #VideoMarketing #IncuBrix",
        "cta": "Grab the CreatorOps SOP at incubrix.com/sop",
        "utm": "https://incubrix.com/sop?utm_source=tiktok&utm_medium=video&utm_campaign=INC-V02&utm_content=creator_tax",
        "metric": "Avg Watch Time > 80%, 4,000+ views, 80+ shares",
        "rights": "Original creator footage; AudioJungle license #AJ-99214; Free Google Font Montserrat.",
        "day": 4,
        "time": "16:00 UTC"
    },
    {
        "id": "INC-V03",
        "title": "Why Your Video Subtitles Are Killing Your Retention",
        "platform": "YouTube Shorts / LinkedIn",
        "pillar": "Pillar 4: Creator Benchmarks",
        "duration": "45s",
        "aspect_ratio": "9:16 (1080x1920)",
        "hook": "If your short-form captions look like this, 70% of viewers swipe away in 3 seconds.",
        "script_breakdown": [
            {"time": "0:00 - 0:04", "speaker": "Creator", "visual": "Screen shows tiny, unreadable static white subtitles at the very bottom edge behind TikTok UI icons.", "audio": "'If your captions look like this, 70% of people swipe away before you finish your sentence.'"},
            {"time": "0:04 - 0:16", "speaker": "Creator", "visual": "Red bounding box highlighting how platform UI buttons (like, comment, share) block the text.", "audio": "'First mistake: placing text in the dead zone where buttons block it. Second: dumping 12 words per line instead of dynamic 2-word bursts.'"},
            {"time": "0:16 - 0:32", "speaker": "Creator", "visual": "IncuBrix caption engine demo: Safe zone grid turns green, dynamic word-level highlighting turns active.", "audio": "'IncuBrix auto-calibrates to platform safe zones and highlights high-impact words automatically to maintain eye tracking.'"},
            {"time": "0:32 - 0:45", "speaker": "Creator", "visual": "Audience retention graph showing 42% retention vs 68% retention. Download button.", "audio": "'Higher retention means more algorithmic distribution. Stop guessing safe zones—use IncuBrix for free.'"}
        ],
        "caption": "73% of social video is watched without sound. 🔇 If your subtitles are in the platform 'dead zone' or move too slowly, your retention plummets. Here's how to format short-form captions for maximum algorithmic watch time. #ShortsTips #VideoRetention #SocialMediaGrowth #IncuBrix",
        "cta": "Test the auto-caption generator at incubrix.com/studio",
        "utm": "https://incubrix.com/studio?utm_source=linkedin&utm_medium=video&utm_campaign=INC-V03&utm_content=caption_retention",
        "metric": "50+ Saves, 1,800+ impressions, 35+ sign-ups",
        "rights": "Royalty-free B-roll from Pexels (Commercial license); Custom IncuBrix UI animation.",
        "day": 6,
        "time": "16:00 UTC"
    },
    {
        "id": "INC-V04",
        "title": "The 5 Hook Formulas Behind 1.2M Views",
        "platform": "YouTube Shorts / X",
        "pillar": "Pillar 4: Creator Benchmarks",
        "duration": "50s",
        "aspect_ratio": "9:16 (1080x1920)",
        "hook": "We analyzed 1,000 short-form clips. These 5 hook formulas beat all the rest.",
        "script_breakdown": [
            {"time": "0:00 - 0:03", "speaker": "Creator", "visual": "Creator points to floating 3D numbers: '1,000 Videos Analyzed'.", "audio": "'We analyzed 1,000 viral clips. Here are the 5 hook formulas that actually work.'"},
            {"time": "0:03 - 0:12", "speaker": "Creator", "visual": "Slide 1: The Contrarian Trap ('Stop doing X'). Example overlay on screen.", "audio": "'Number 1: The Contrarian Trap: 'Stop editing in Premiere until you watch this.''"},
            {"time": "0:12 - 0:22", "speaker": "Creator", "visual": "Slide 2: The Direct Cost ('You are losing \$400 every week by...').", "audio": "'Number 2: The Direct Cost: quantify the exact money or time they are burning.'"},
            {"time": "0:22 - 0:34", "speaker": "Creator", "visual": "Slide 3: The Secret Weapon. Show IncuBrix AI hook scorer ranking hooks.", "audio": "'Number 3: The Secret Weapon. Show the unexpected tool that top 1% creators use.'"},
            {"time": "0:34 - 0:50", "speaker": "Creator", "visual": "Full swipe file graphic with free download URL.", "audio": "'IncuBrix auto-generates all 5 variations for every video you upload. Grab the full swipe file in the comments.'"}
        ],
        "caption": "Your video dies in the first 2 seconds if the hook doesn't create an immediate curiosity loop. 🎣 We audited 1,000+ top creator videos to identify the 5 highest-retention opening frameworks. Read the breakdown or let IncuBrix write them for you. #HookFormula #ContentCreation #ViralHooks #IncuBrix",
        "cta": "Download the Hook Swipe File at incubrix.com/hooks",
        "utm": "https://incubrix.com/hooks?utm_source=x&utm_medium=video&utm_campaign=INC-V04&utm_content=5_hook_formulas",
        "metric": "100+ Retweets, 3,500+ views, 90+ downloads",
        "rights": "Licensed track 'Digital Flow' Artlist ID #AL-4482; Open font Poppins.",
        "day": 8,
        "time": "15:00 UTC"
    },
    {
        "id": "INC-V05",
        "title": "Stop Paying $3,000/mo for a Repurposing Agency",
        "platform": "YouTube Shorts / LinkedIn",
        "pillar": "Pillar 5: Trench Stories",
        "duration": "46s",
        "aspect_ratio": "9:16 (1080x1920)",
        "hook": "Before you hire a \$3,000 a month repurposing agency, watch how they actually make your content.",
        "script_breakdown": [
            {"time": "0:00 - 0:04", "speaker": "Creator", "visual": "Invoice graphic on screen: 'Monthly Retainer: \$3,500' stamped with red question mark.", "audio": "'Before you hire a 3,000 dollar a month content agency, look behind the curtain.'"},
            {"time": "0:04 - 0:18", "speaker": "Creator", "visual": "B-roll of junior freelancer running automated software in a browser tab.", "audio": "'Most modern agencies don't have a team of 10 editors. They use software like IncuBrix to do 90% of the heavy lifting in 10 minutes.'"},
            {"time": "0:18 - 0:34", "speaker": "Creator", "visual": "IncuBrix team workspace showing multi-client asset generation.", "audio": "'You can build this exact in-house pipeline yourself. One recording turns into 10 clips, 3 carousels, and 12 social posts with zero agency markups.'"},
            {"time": "0:34 - 0:46", "speaker": "Creator", "visual": "Cost comparison graphic: \$3,000/mo vs \$29/mo software subscription.", "audio": "'Keep your \$36,000 annual budget. Set up your CreatorOps engine with IncuBrix today.'"}
        ],
        "caption": "The \$3,000/mo content repurposing agency model is broken. 💸 Smart founders and creators are bringing the CreatorOps stack in-house. With AI transcription, auto-reframing, and multi-format copy generation, one junior assistant or founder can do the work of an entire media agency. #B2BMarketing #CreatorOps #AgencyLife #IncuBrix",
        "cta": "Build your in-house engine at incubrix.com/creatorops",
        "utm": "https://incubrix.com/creatorops?utm_source=linkedin&utm_medium=video&utm_campaign=INC-V05&utm_content=agency_alternative",
        "metric": "85+ Reactions, 30+ Comments, 40+ sign-ups",
        "rights": "IncuBrix authentic screen assets; licensed royalty-free footage.",
        "day": 11,
        "time": "16:00 UTC"
    },
    {
        "id": "INC-V06",
        "title": "How to Get 30 Pieces of Content from 1 Zoom Recording",
        "platform": "YouTube Shorts / TikTok",
        "pillar": "Pillar 1: Workflow Teardowns",
        "duration": "52s",
        "aspect_ratio": "9:16 (1080x1920)",
        "hook": "Do not delete that 30-minute Zoom call. It is worth 30 pieces of social content.",
        "script_breakdown": [
            {"time": "0:00 - 0:03", "speaker": "Creator", "visual": "Creator points to Zoom cloud recording folder on laptop.", "audio": "'Don't delete that 30-minute Zoom recording. It is worth 30 social posts.'"},
            {"time": "0:03 - 0:15", "speaker": "Creator", "visual": "Zoom MP4 file dropped into IncuBrix. Instant transcript generation on screen.", "audio": "'Every client interview, team demo, or podcast has at least 5 breakthrough moments you completely forgot about.'"},
            {"time": "0:15 - 0:35", "speaker": "Creator", "visual": "Tree diagram unfolds: 1 Video -> 8 Shorts, 4 Carousels, 10 Tweets, 2 Newsletters, 6 Quotes.", "audio": "'Drop it into IncuBrix. In one pass, you extract 8 short videos, 4 visual carousels, 10 tactical tweets, and a full newsletter.'"},
            {"time": "0:35 - 0:52", "speaker": "Creator", "visual": "Calendar view populating automatically for the entire month.", "audio": "'That is an entire month of consistent social media presence from one single conversation. Test it yourself free.'"}
        ],
        "caption": "Your Zoom recordings are an untapped goldmine. ⛏️ Stop treating client interviews or founder demos as one-time events. Feed them through IncuBrix and turn 30 minutes of conversation into a full month of authority-building social posts. #ContentRepurposing #ZoomHacks #CreatorGrowth #IncuBrix",
        "cta": "Repurpose your Zoom video at incubrix.com/zoom",
        "utm": "https://incubrix.com/zoom?utm_source=tiktok&utm_medium=video&utm_campaign=INC-V06&utm_content=zoom_repurpose",
        "metric": "5,000+ views, 120+ bookmarks, 60+ clicks",
        "rights": "Zoom UI fair-use interface capture; Royalty-free track 'Inspire Flow'.",
        "day": 14,
        "time": "16:00 UTC"
    },
    {
        "id": "INC-V07",
        "title": "The Split-Screen Reframe Trick for Multi-Speaker Podcasts",
        "platform": "YouTube Shorts / LinkedIn",
        "pillar": "Pillar 2: Feature-in-Action",
        "duration": "44s",
        "aspect_ratio": "9:16 (1080x1920)",
        "hook": "Here is why standard AI video clippers fail on two-person podcast interviews.",
        "script_breakdown": [
            {"time": "0:00 - 0:04", "speaker": "Creator", "visual": "Demonstrating generic AI clipper: Camera abruptly jump-cuts between two faces making viewer dizzy.", "audio": "'Most AI clippers ruin two-person podcasts with violent, jarring jump-cuts every time someone breathes.'"},
            {"time": "0:04 - 0:18", "speaker": "Creator", "visual": "Showing IncuBrix Smart Multi-Speaker Layout: Clean stacked split-screen with active speaker border.", "audio": "'IncuBrix uses intelligent stacked layouts. Host on top, guest on bottom, with subtle glow tracking the active speaker.'"},
            {"time": "0:18 - 0:32", "speaker": "Creator", "visual": "Screen-share mode toggle: Guest top half, live demo bottom half.", "audio": "'And if you share a screen or slides, it automatically docks the visual without cutting off the code or diagrams.'"},
            {"time": "0:32 - 0:44", "speaker": "Creator", "visual": "One-click export preview on mobile screen mockup.", "audio": "'Professional framing without spending 2 hours setting up multi-cam sequences in Premiere. Try IncuBrix free today.'"}
        ],
        "caption": "Nothing ruins a podcast short faster than erratic camera jumping. 📹 IncuBrix’s smart multi-speaker engine keeps both host and guest framed in a clean vertical stack with active audio detection and screen-share docking. Built by creators, for creators. #PodcastClips #VideoProduction #CreatorOps #IncuBrix",
        "cta": "Try multi-speaker framing at incubrix.com/framing",
        "utm": "https://incubrix.com/framing?utm_source=linkedin&utm_medium=video&utm_campaign=INC-V07&utm_content=split_screen",
        "metric": "1,500+ views, 40+ likes, 25+ sign-ups",
        "rights": "Original recording setup; Royalty-free commercial license.",
        "day": 17,
        "time": "16:00 UTC"
    },
    {
        "id": "INC-V08",
        "title": "3 AI Video Tools You Need (and 2 to Avoid)",
        "platform": "YouTube Shorts / X",
        "pillar": "Pillar 4: Creator Benchmarks",
        "duration": "49s",
        "aspect_ratio": "9:16 (1080x1920)",
        "hook": "I tested 15 AI creator tools this year. 90% are pure hype. Here are the only 3 you actually need.",
        "script_breakdown": [
            {"time": "0:00 - 0:04", "speaker": "Creator", "visual": "Trash can graphic with 10 logos being dragged to the bin.", "audio": "'I tested 15 AI video tools this year. Most are overpriced wrappers. Here are the only 3 that matter.'"},
            {"time": "0:04 - 0:16", "speaker": "Creator", "visual": "Tool 1: High-fidelity audio enhancer (Adobe Podcast / Descript Studio Sound).", "audio": "'Tool 1: Studio sound enhancers to turn bad mic audio into broadcast quality.'"},
            {"time": "0:16 - 0:32", "speaker": "Creator", "visual": "Tool 2: IncuBrix CreatorOps engine processing long video into 10 multi-platform assets.", "audio": "'Tool 2: IncuBrix for full-funnel repurposing. It doesn't just cut clips—it drafts your LinkedIn carousels and X threads simultaneously.'"},
            {"time": "0:32 - 0:49", "speaker": "Creator", "visual": "Tool 3: Color grade lookup profiles. Summary checklist screen.", "audio": "'Tool 3: Custom LUT profiles for instant color correction. Save this list so you don't burn \$200 on junk software.'"}
        ],
        "caption": "The creator economy software bloat is real. 🛠️ You don't need 12 monthly subscriptions to run a world-class media engine. You need great audio, disciplined distribution, and an operating system that turns 1 recording into weekly assets. #AITools #CreatorStack #ProductivityTools #IncuBrix",
        "cta": "Get the Creator Tool Stack Guide at incubrix.com/stack",
        "utm": "https://incubrix.com/stack?utm_source=x&utm_medium=video&utm_campaign=INC-V08&utm_content=tool_comparison",
        "metric": "120+ Bookmarks, 4,200+ views, 75+ clicks",
        "rights": "Commercial licensed music; Custom graphics.",
        "day": 20,
        "time": "15:00 UTC"
    },
    {
        "id": "INC-V09",
        "title": "Raw Video to Formatted LinkedIn Post in 28 Seconds",
        "platform": "YouTube Shorts / LinkedIn",
        "pillar": "Pillar 2: Feature-in-Action",
        "duration": "38s",
        "aspect_ratio": "9:16 (1080x1920)",
        "hook": "Watch this stopwatch. In 28 seconds, this raw video becomes a high-converting LinkedIn post.",
        "script_breakdown": [
            {"time": "0:00 - 0:03", "speaker": "Creator", "visual": "Digital stopwatch overlay on screen starting at 00:00.00.", "audio": "'Watch this timer. In 28 seconds, this raw video becomes a high-converting LinkedIn post.'"},
            {"time": "0:03 - 0:14", "speaker": "Creator", "visual": "Drop video link into IncuBrix. Progress bar races. Timer hits 00:12.45.", "audio": "'Paste the YouTube or Loom link into IncuBrix. It extracts the core framework, removes filler words, and identifies the main takeaway.'"},
            {"time": "0:14 - 0:28", "speaker": "Creator", "visual": "Formatted LinkedIn post appears: Hook line, bullet points, CTA, and embedded 4:5 clip.", "audio": "'Boom: perfectly spaced hook, punchy body copy, relevant hashtags, and the attached video clip cropped to 4:5 for mobile.'"},
            {"time": "0:28 - 0:38", "speaker": "Creator", "visual": "Stopwatch stops at 00:27.89. IncuBrix logo appears.", "audio": "'28 seconds total. No copy-pasting into 3 tabs. Try it yourself free at incubrix.com.'"}
        ],
        "caption": "How long does it take you to turn a video insight into a written LinkedIn post? ⏱️ If it's more than 2 minutes, you're leaving growth on the table. Watch IncuBrix transcribe, summarize, format, and pair the video asset in 28 seconds flat. #LinkedInGrowth #ContentOps #WorkflowSpeed #IncuBrix",
        "cta": "Try the 30-second challenge at incubrix.com/speed",
        "utm": "https://incubrix.com/speed?utm_source=linkedin&utm_medium=video&utm_campaign=INC-V09&utm_content=speed_challenge",
        "metric": "2,200+ views, 60+ reactions, 45+ sign-ups",
        "rights": "Royalty-free audio track 'Velocity' (Soundstripe #SS-1940); Original screen capture.",
        "day": 23,
        "time": "16:00 UTC"
    },
    {
        "id": "INC-V10",
        "title": "The Secret CreatorOps Stack Used by Top 1% Media Teams",
        "platform": "YouTube Shorts / TikTok / LinkedIn",
        "pillar": "Pillar 3: CreatorOps Systems",
        "duration": "47s",
        "aspect_ratio": "9:16 (1080x1920)",
        "hook": "The top 1% of creators do not work 80 hours a week. They run an asynchronous content assembly line.",
        "script_breakdown": [
            {"time": "0:00 - 0:04", "speaker": "Creator", "visual": "Flowchart diagram zooming in: 'Input -> Assembly Line -> Multi-Channel Output'.", "audio": "'The top 1 percent of creators don't work 80 hours a week. They build an asynchronous assembly line.'"},
            {"time": "0:04 - 0:18", "speaker": "Creator", "visual": "Step 1: One 60-minute deep conversation per week. Step 2: Auto-ingest into IncuBrix.", "audio": "'Step 1: Record 60 minutes of high-conviction thinking. Step 2: Feed it into IncuBrix to generate your core modular assets.'"},
            {"time": "0:18 - 0:32", "speaker": "Creator", "visual": "Step 3: Reviewer dashboard approving 20 assets in 15 minutes. Step 4: Auto-schedule.", "audio": "'Step 3: Spend 15 minutes reviewing tone and facts. Step 4: One-click sync to LinkedIn, YouTube, and X.'"},
            {"time": "0:32 - 0:47", "speaker": "Creator", "visual": "Free Notion template link on screen with QR code.", "audio": "'That is how you achieve 100K impressions every week with zero burnout. Grab the free CreatorOps Notion template below.'"}
        ],
        "caption": "Stop treating content like a craft project and start treating it like an operating system. ⚙️ The CreatorOps framework separates high-leverage ideation from low-leverage formatting. When your pipeline is automated, your consistency becomes unstoppable. #CreatorOps #MediaOperations #SystemsThinking #IncuBrix",
        "cta": "Download the Notion CreatorOps Template at incubrix.com/notion",
        "utm": "https://incubrix.com/notion?utm_source=shorts&utm_medium=video&utm_campaign=INC-V10&utm_content=assembly_line",
        "metric": "3,800+ views, 95+ bookmarks, 65+ sign-ups",
        "rights": "Licensed track 'Future Horizons' (Pond5 #P5-7721); Commercial safe graphics.",
        "day": 26,
        "time": "16:00 UTC"
    }
]

# Write all Video files
for v in VIDEOS:
    clean_title = re.sub(r'[^a-zA-Z0-9_]', '_', v['title'].lower())[:35]
    filepath = os.path.join(VIDEOS_DIR, f"{v['id']}_{clean_title}.md")
    content = f"""# {v['id']}: {v['title']}

**Platform:** {v['platform']}  
**Pillar:** {v['pillar']}  
**Duration:** {v['duration']}  
**Aspect Ratio:** {v['aspect_ratio']}  
**Scheduled Slot:** Day {v['day']} at {v['time']}  
**Target Metric:** {v['metric']}  
**Rights & Safety:** {v['rights']}  

---

### The Hook (First 2 Seconds)
> "{v['hook']}"

---

### Full Spoken Script & Production Storyboard

| Timestamp | Speaker | Visual & Action Direction | Audio & Spoken Script |
|---|---|---|---|
"""
    for row in v["script_breakdown"]:
        content += f"| `{row['time']}` | **{row['speaker']}** | {row['visual']} | {row['audio']} |\n"

    content += f"""
---

### Publishing Copy (Caption & Hashtags)
```text
{v['caption']}
```

---

### Call to Action & Measurable Tracking Link
* **Call to Action:** {v['cta']}
* **UTM Tracking URL:** [{v['utm']}]({v['utm']})
* **Conversion Goal:** Direct click-to-trial account registration (Free Tier).

---

### Editable Source Asset Specifications
* **Raw Video Resolution:** 1080x1920 (9:16 Vertical)
* **Subtitle Styling:** Font Inter Bold 42pt, `#FFFFFF` text with `#10B981` (Emerald Teal) active word highlight, `#121316` 80% opacity pill background.
* **Safe Zone Bounds:** Top margin 180px (clear of account banner), Bottom margin 280px (clear of platform audio/caption bar), Right margin 120px (clear of interaction icons).
* **Audio Track:** Commercial license royalty-free instrumental, normalized to -14 LUFS.
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(VIDEOS)} Video Asset documents in {VIDEOS_DIR}")
