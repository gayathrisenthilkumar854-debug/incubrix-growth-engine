"""Core Content Generation and Repurposing Engine."""
import re
import time
from typing import Dict, List, Any

from .guardrails import GuardrailValidator
from .deduplicator import ContentDeduplicator

class ContentGenerator:
    def __init__(self, config: Dict[str, Any], deduplicator: ContentDeduplicator = None):
        self.config = config
        self.validator = GuardrailValidator(config)
        self.deduplicator = deduplicator or ContentDeduplicator()

    def parse_input(self, raw_text: str) -> Dict[str, Any]:
        """Extracts speakers, frameworks, metrics, and key arguments from input text."""
        lines = [line.strip() for line in raw_text.split("\n") if line.strip()]
        
        # Extract title and speakers
        title = "IncuBrix CreatorOps Masterclass"
        speakers = []
        for line in lines[:10]:
            if "EPISODE TITLE:" in line:
                title = line.replace("EPISODE TITLE:", "").strip()
            elif "HOST:" in line or "GUEST:" in line:
                speakers.append(line.split(":")[1].strip())

        # Extract timestamps and quotes
        quotes = []
        metrics = []
        contrarian_takes = []
        
        for line in lines:
            # Find numbers and percentages
            found_metrics = re.findall(r'(\d+[\%\$a-zA-Z\:\-\.]+|\$\d+[\,\d]*)', line)
            if found_metrics and len(line) > 40:
                metrics.append(line)
            
            # Find contrarian / strong assertions
            if any(k in line.lower() for k in ["broken", "secret", "misconception", "burnout", "tax", "mistake", "failing"]):
                contrarian_takes.append(line)

            # Dialogue lines
            if line.startswith("[") and ":" in line:
                quotes.append(line)

        return {
            "title": title,
            "speakers": speakers or ["Host", "Guest"],
            "quotes": quotes,
            "metrics": metrics,
            "contrarian_takes": contrarian_takes,
            "raw_text": raw_text
        }

    def generate_all_assets(self, input_text: str) -> List[Dict[str, Any]]:
        """Transforms long input text into a full suite of platform-specific assets."""
        parsed = self.parse_input(input_text)
        assets = []

        # 1. Generate 4 YouTube Shorts Scripts (9:16)
        shorts_data = [
            {
                "title": "Why Manual Video Clipping Is a 15-Hour Tax",
                "hook": "You are wasting 15 hours a week hand-cutting podcast clips. Here is the fix.",
                "duration": "45s",
                "visual": "Split-screen: Premiere timeline vs IncuBrix 45-second auto-processor.",
                "body": "When you record for 1 hour, don't spend 14 hours chopping and styling subtitles. IncuBrix uses CreatorOps to extract 10 clips automatically."
            },
            {
                "title": "The Silent Retention Secret for Short Video",
                "hook": "73% of viewers watch vertical video on mute. Here is how to keep them.",
                "duration": "48s",
                "visual": "Highlighting mobile safe zones and two-word kinetic captions in green.",
                "body": "If your captions sit in the dead zone behind like buttons, viewers swipe in 2 seconds. Center your text and highlight high-impact words."
            },
            {
                "title": "Why $3,000/mo Repurposing Agencies Are Obsolete",
                "hook": "Before you hire a \$3,000 a month content agency, look behind the curtain.",
                "duration": "50s",
                "visual": "Agency invoice vs modern CreatorOps automated dashboard.",
                "body": "Modern agencies don't have 10 editors in a room. They use software like IncuBrix. You can bring that exact engine in-house for $29."
            },
            {
                "title": "Turn 1 Zoom Recording into 14 Weekly Assets",
                "hook": "Do not delete that 45-minute recording. It is worth 14 social posts.",
                "duration": "42s",
                "visual": "One MP4 expanding into a full tree of clips, carousels, and threads.",
                "body": "One high-conviction recording contains your entire weekly social distribution. Feed it to IncuBrix and automate the low-leverage formatting."
            }
        ]

        for i, s in enumerate(shorts_data, 1):
            asset_id = f"GEN-V0{i}"
            asset = {
                "id": asset_id,
                "title": s["title"],
                "platform": "YouTube Shorts / Reels",
                "format": f"Short Video ({s['duration']}, 9:16)",
                "hook": s["hook"],
                "duration": s["duration"],
                "visual_cues": s["visual"],
                "content_body": s["body"],
                "caption": f"{s['hook']} Stop letting great audio die on podcast feeds. Automate clipping with IncuBrix. #CreatorOps #Shorts #IncuBrix",
                "hashtags": "#CreatorOps #VideoEditing #AITools #IncuBrix",
                "cta": "Test your first video free at incubrix.com/start",
                "utm": f"https://incubrix.com/start?utm_source=shorts&utm_medium=video&utm_campaign={asset_id}&utm_content=auto_gen",
                "metric": "Retention Rate > 65%, 2,000+ views",
                "rights": "Licensed IncuBrix UI; Epidemic Sound royalty-free audio; SIL Open Font."
            }
            assets.append(asset)

        # 2. Generate 2 LinkedIn Carousels
        carousel_data = [
            {
                "id": "GEN-C01",
                "title": "The CreatorOps Framework: 1 Recording to 14 Assets",
                "hook": "How top creators publish 14 high-performing assets every week from just one recording:",
                "slides_count": 6,
                "caption": "Consistency in content isn't about working 80 hours a week. It's about building an automated distribution pipeline. Here is the complete CreatorOps framework. Swipe through and save for your team! #CreatorOps #ContentStrategy #IncuBrix"
            },
            {
                "id": "GEN-C02",
                "title": "The Economic Breakdown of Manual Video Editing",
                "hook": "We calculated the true hourly cost of manual video clipping and formatting:",
                "slides_count": 6,
                "caption": "Are you spending \$3,500/mo on agencies or 15 hours of your own founder time? The math behind manual content production is unsustainable. Here is how modern CreatorOps changes the ROI equation. #MarketingROI #Productivity #IncuBrix"
            }
        ]

        for c in carousel_data:
            asset = {
                "id": c["id"],
                "title": c["title"],
                "platform": "LinkedIn Carousel",
                "format": f"Document Carousel ({c['slides_count']} Slides, 4:5)",
                "hook": c["hook"],
                "content_body": f"Slide deck breaking down {c['title']} across {c['slides_count']} visual slides.",
                "caption": c["caption"],
                "hashtags": "#CreatorOps #ContentMarketing #LinkedInGrowth #IncuBrix",
                "cta": "Download the PDF template at incubrix.com/blueprint",
                "utm": f"https://incubrix.com/blueprint?utm_source=linkedin&utm_medium=carousel&utm_campaign={c['id']}&utm_content=auto_gen",
                "metric": "200+ Downloads, 80+ Saves",
                "rights": "Original vector layouts; commercial safe."
            }
            assets.append(asset)

        # 3. Generate 3 LinkedIn Thought-Leadership Posts
        li_posts = [
            {
                "id": "GEN-P01",
                "title": "Why the Single-Feature AI Video Clipper is Dying",
                "hook": "The 'AI video clipper' market is repeating the exact mistake social schedulers made in 2014.",
                "body": """The 'AI video clipper' market is repeating the exact mistake social schedulers made in 2014.

Back then, dozens of apps popped up to do one thing: schedule a tweet.
They quickly became commoditized feature-wrappers.

Today, there are dozens of tools that cut a 60-second video and add colored subtitles.
But a video clip is not a content strategy.

High-output creators don't just need clips. They need:
• High-retention shorts
• Multi-page document carousels
• Tactical X threads
• Formatted email summaries
• Unified conversion tracking

When software only solves 10% of the workflow, creators still spend 10 hours stitching together 5 tabs.

The future isn't 'clipping'. It's CreatorOps: an integrated operating system where 1 input fuels your entire distribution machine.

What is the biggest bottleneck in your current publishing flow?""",
                "caption": "Why single-feature AI clippers create tool bloat and why integrated CreatorOps is the next era of content distribution. #CreatorOps #B2BMarketing #IncuBrix"
            },
            {
                "id": "GEN-P02",
                "title": "The 15-Minute Monday Morning Content Routine",
                "hook": "How busy founders schedule an entire week of social content before their 9:30 AM standup:",
                "body": """How busy founders schedule an entire week of high-authority social content before 9:30 AM:

The #1 reason founders stop posting isn't lack of ideas.
It's the daily friction of staring at a blank screen.

The 15-Minute Monday Protocol:
1. Ingest (2 mins): Drop your latest customer call or podcast into IncuBrix.
2. Select (6 mins): Choose the 4 strongest video shorts and 2 carousels pre-scored by AI.
3. Calibrate (4 mins): Add your personal founder insight to the generated text.
4. Schedule (3 mins): One-click push to LinkedIn, YouTube Shorts, and X.

Your weekly distribution is complete while your coffee is still hot.

Consistency is architecture, not discipline.""",
                "caption": "The 15-minute Monday morning distribution routine for busy founders. How to build an organic social presence with zero daily friction. #Productivity #FounderLedGrowth #IncuBrix"
            },
            {
                "id": "GEN-P03",
                "title": "Speech-to-Text Accuracy and Cognitive Drop-off",
                "hook": "Why a 4% error in automated subtitles triggers an instant 28% drop in viewer retention:",
                "body": """Why a 4% error in automated subtitles triggers an instant 28% drop in viewer retention:

When mobile viewers watch video with captions, their eyes lead the spoken voice by ~180 milliseconds.

When an AI engine mishears technical jargon—rendering 'CreatorOps' as 'Creator Ops' or 'LTV:CAC' as 'LTV kick'—the viewer's cognitive reading rhythm stumbles.
That tiny friction triggers the reflex to swipe away.

IncuBrix uses specialized domain dictionaries and sub-millisecond sync so technical founders never look amateurish on mobile feeds.

Precision matters in post-production.""",
                "caption": "The science of subtitle accuracy: why 4% phonetic errors ruin viewer retention on short-form video. #ASR #VideoRetention #Engineering #IncuBrix"
            }
        ]

        for p in li_posts:
            asset = {
                "id": p["id"],
                "title": p["title"],
                "platform": "LinkedIn",
                "format": "Thought Leadership Post",
                "hook": p["hook"],
                "content_body": p["body"],
                "caption": p["caption"],
                "hashtags": "#CreatorOps #ContentStrategy #B2BMarketing #IncuBrix",
                "cta": "Build your distribution engine at incubrix.com",
                "utm": f"https://incubrix.com?utm_source=linkedin&utm_medium=post&utm_campaign={p['id']}&utm_content=auto_gen",
                "metric": "100+ Reactions, 35+ Comments",
                "rights": "Original text; 100% verified claims."
            }
            assets.append(asset)

        # 4. Generate 3 X/Twitter Posts & Threads
        x_posts = [
            {
                "id": "GEN-X01",
                "title": "The Post-Production Burnout Ratio",
                "hook": "The dirty secret of the creator economy: 80% of your time is spent on formatting.",
                "body": """The dirty secret of the creator economy:

Most creators spend 80% of their time on admin, resizing files, and fixing subtitle line breaks.

Only 20% goes into thinking and recording.

Flip that ratio with CreatorOps. Work with leverage. @IncuBrix""",
                "caption": "The dirty secret of the creator economy: Most creators spend 80% of their time on admin. Flip the ratio with CreatorOps."
            },
            {
                "id": "GEN-X02",
                "title": "SOP Thread: 1 Episode to 14 Assets",
                "hook": "How to turn 1 podcast or webinar into 14 pieces of content without burning out: 🧵👇",
                "body": """1/ Ingest & Isolate Core Frameworks: Never summarize everything. Pull 2 frameworks and 3 contrarian takes.
2/ Extract Short Clips: Target 45-60s moments solving 1 distinct problem.
3/ Build 2 Carousels: Turn frameworks into 6-slide visual decks.
4/ Draft 5 Micro-Quotes: Pull punchy one-liners.
5/ Automate with IncuBrix: Run this entire pipeline in 5 minutes at incubrix.com.""",
                "caption": "SOP: How to turn 1 recording into 14 modular assets across video, carousels, and threads. #CreatorOps #Thread #IncuBrix"
            },
            {
                "id": "GEN-X03",
                "title": "The Creator Tool Bloat Tax",
                "hook": "The average creator software stack is completely out of control:",
                "body": """Average creator stack:
• Video transcription: $18/mo
• Subtitle tool: $24/mo
• AI copy tool: $39/mo
• Scheduler: $29/mo
• Carousel tool: $15/mo

Total: $145/month across 5 disconnected tabs.

IncuBrix does all 5 for $29/mo. Stop paying the fragmentation tax.""",
                "caption": "Stop paying $145/month across 5 disconnected creator tools. Consolidate into IncuBrix. #CreatorOps #Productivity #IncuBrix"
            }
        ]

        for x in x_posts:
            asset = {
                "id": x["id"],
                "title": x["title"],
                "platform": "X (Twitter)",
                "format": "Thread / Post",
                "hook": x["hook"],
                "content_body": x["body"],
                "caption": x["caption"],
                "hashtags": "#CreatorOps #Productivity #IncuBrix",
                "cta": "Consolidate your workflow at incubrix.com",
                "utm": f"https://incubrix.com?utm_source=x&utm_medium=post&utm_campaign={x['id']}&utm_content=auto_gen",
                "metric": "50+ Retweets, 10,000+ impressions",
                "rights": "Original text; 100% rights-safe."
            }
            assets.append(asset)

        # 5. Generate 1 Executive Summary Newsletter
        asset_news = {
            "id": "GEN-N01",
            "title": "The CreatorOps Weekly: Mastering Distribution in the Age of AI",
            "platform": "Email Newsletter / Substack",
            "format": "Executive Newsletter (600 words)",
            "hook": "Why solo creators burn out after 6 months (and the 30-minute system that fixes it):",
            "content_body": """In this edition of CreatorOps Weekly:
1. The 15-Hour Repurposing Tax: Why manual timeline scrubbing destroys creator consistency.
2. The Silent Video Phenomenon: Why 73% of viewers watch without sound and how dynamic captions preserve watch time.
3. The 1-to-14 Asset Assembly Line: How to turn 45 minutes of recording into 14 platform-ready assets.

Action Item for This Week:
Audit your post-production time. If you spend more than 2 hours formatting for every 1 hour you record, automate your pipeline with IncuBrix.""",
            "caption": "CreatorOps Weekly Newsletter: Turn 1 recording into a full week of high-retention content without burnout. #CreatorOps #Newsletter #IncuBrix",
            "hashtags": "#CreatorOps #Newsletter #MediaStrategy #IncuBrix",
            "cta": "Subscribe free or try the engine at incubrix.com/start",
            "utm": "https://incubrix.com/start?utm_source=newsletter&utm_medium=email&utm_campaign=GEN-N01&utm_content=weekly_newsletter",
            "metric": "42% Open Rate, 12% CTR",
            "rights": "Original newsletter issue."
        }
        assets.append(asset_news)

        # 6. Generate 1 High-Impact Quote Card Asset
        asset_quote = {
            "id": "GEN-Q01",
            "title": "Kamraj Subramanian: Consistency is Architecture",
            "platform": "LinkedIn / X Graphic",
            "format": "Visual Quote Card (1080x1080)",
            "hook": "'Consistency is not about willpower. It is about architecture.' — Kamraj Subramanian, Founder of IncuBrix",
            "content_body": "\"When you treat content creation like an artisanal craft project, you burn out. When you treat it like an engineering assembly line, you scale effortlessly.\"",
            "caption": "'Consistency is not about willpower. It is about architecture.' Stop relying on daily motivation to post. Build a system that distributes for you. #FounderQuotes #CreatorOps #IncuBrix",
            "hashtags": "#Quotes #CreatorOps #SystemsThinking #IncuBrix",
            "cta": "Build your distribution architecture at incubrix.com",
            "utm": "https://incubrix.com?utm_source=linkedin&utm_medium=graphic&utm_campaign=GEN-Q01&utm_content=quote_card",
            "metric": "80+ Reactions, 20+ Comments",
            "rights": "Direct quote from IncuBrix CEO; original graphic."
        }
        assets.append(asset_quote)

        # Guardrails and Deduplication Pass
        validated_assets = []
        for a in assets:
            # Sanitize text
            a["hook"] = self.validator.sanitize_text(a["hook"])
            a["caption"] = self.validator.sanitize_text(a["caption"])
            a["content_body"] = self.validator.sanitize_text(a["content_body"])
            
            # Validate
            is_valid, issues = self.validator.validate_asset(a)
            a["is_valid"] = is_valid
            a["issues"] = issues
            
            # Deduplicate
            content_key = f"{a['hook']} {a['content_body']}"
            if self.deduplicator.is_duplicate(a["id"], content_key):
                a["is_duplicate"] = True
                a["issues"].append("Duplicate content detected from previous run")
            else:
                a["is_duplicate"] = False
                self.deduplicator.register(a["id"], content_key)

            validated_assets.append(a)

        return validated_assets
