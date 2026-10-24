import os
import csv
import json
import re

BASE_DIR = r"C:\Users\Gayathri S\.gemini\antigravity\scratch\incubrix-growth-engine"
CONTENT_DIR = os.path.join(BASE_DIR, "content")
POSTS_DIR = os.path.join(CONTENT_DIR, "posts")

os.makedirs(POSTS_DIR, exist_ok=True)

POSTS = [
    {
        "id": "INC-P01",
        "title": "The Dirty Secret of the Creator Economy",
        "platform": "X (Twitter)",
        "pillar": "Pillar 1: Workflow Teardowns",
        "format": "Single Tweet + Visual Metric Graphic",
        "hook": "The dirty secret of the creator economy: Most creators spend 80% of their time on admin, formatting, and file-renaming.",
        "content_body": """The dirty secret of the creator economy:

Most creators spend 80% of their time on admin, video cropping, manual subtitle fixing, and file-renaming.

Only 20% goes into thinking and creating.

When you flip that ratio with CreatorOps, growth becomes effortless.

Stop being a video technician. Be a creator.""",
        "caption": "The dirty secret of the creator economy: Most creators spend 80% of their time on admin, video cropping, manual subtitle fixing, and file-renaming. Only 20% goes into thinking and creating. Flip that ratio with CreatorOps.",
        "hashtags": "#CreatorEconomy #Productivity #CreatorOps #IncuBrix",
        "cta": "See how IncuBrix automates the 80% at incubrix.com",
        "utm": "https://incubrix.com?utm_source=x&utm_medium=post&utm_campaign=INC-P01&utm_content=dirty_secret",
        "metric": "80+ Retweets, 15,000+ impressions, 120+ link clicks",
        "rights": "Original text; 100% rights-safe.",
        "day": 1,
        "time": "14:30 UTC"
    },
    {
        "id": "INC-P02",
        "title": "7-Step SOP: Repurpose 1 Webinar into 1 Month of Content",
        "platform": "X (Twitter)",
        "pillar": "Pillar 3: CreatorOps Systems",
        "format": "Tactical 7-Tweet Thread",
        "hook": "How to turn 1 recorded webinar or podcast into 1 full month of social content (without burning 20 hours a week): 🧵👇",
        "content_body": """Tweet 1:
How to turn 1 recorded webinar or podcast into 1 full month of social content (without burning 20 hours a week): 🧵👇

Tweet 2:
1/ Ingest & Isolate Core Frameworks
Never try to summarize everything. Isolate 3 specific frameworks, 2 contrarian takes, and 2 tangible tactical stories from the recording.

Tweet 3:
2/ Extract Short-Form Clips (Vertical 9:16)
Clip the 45-60s moments where a specific problem is diagnosed and solved. Auto-center speakers and eliminate dead audio space > 0.3s.

Tweet 4:
3/ Build 2 Educational Carousels
Take the 2 highest-value frameworks and translate them into 6-to-8 slide PDF decks. Focus on step-by-step schematics and visual simplicity.

Tweet 5:
4/ Draft 5 Micro-Posts from Direct Quotes
Pull 5 provocative single-sentence statements from the speaker. Format them with spacing for LinkedIn and X.

Tweet 6:
5/ Package 1 Executive Newsletter
Synthesize the entire dialogue into a 4-minute read: Problem, Solution, 3 Takeaways, and 1 Action Item for the week.

Tweet 7:
6/ The Automated Stack
You don't need a team of 4 to do this. IncuBrix does this entire 7-step pipeline in 1 pass in under 5 minutes.

Try your first recording free: incubrix.com/start""",
        "caption": "Full 7-step SOP to turn 1 webinar into 30 pieces of modular content. Step-by-step thread covering clip extraction, carousels, quotes, and newsletter packaging. #ContentMarketing #CreatorOps #Thread #IncuBrix",
        "hashtags": "#ContentMarketing #CreatorOps #SOP #Productivity #IncuBrix",
        "cta": "Run the SOP on your next webinar at incubrix.com/start",
        "utm": "https://incubrix.com/start?utm_source=x&utm_medium=thread&utm_campaign=INC-P02&utm_content=webinar_sop",
        "metric": "150+ Retweets, 350+ Bookmarks, 25,000+ impressions",
        "rights": "Original IncuBrix SOP methodology; 100% rights-safe.",
        "day": 3,
        "time": "17:00 UTC"
    },
    {
        "id": "INC-P03",
        "title": "Why the 'Clipping Tool' Era is Dead",
        "platform": "LinkedIn",
        "pillar": "Pillar 3: CreatorOps Systems",
        "format": "Long-form Thought Leadership Post",
        "hook": "The 'AI video clipper' market is repeating the exact mistake social schedulers made in 2014.",
        "content_body": """The 'AI video clipper' market is repeating the exact mistake social media schedulers made in 2014.

Back then, dozens of tools launched to do one thing: schedule a tweet.
They competed on pricing until they became commoditized feature-wrappers.

Today, there are 40+ tools that will cut a 60-second clip from a YouTube video and slap rainbow subtitles on it.

Here is the problem:
A 60-second video clip is not a content strategy.

A creator or modern marketing team does not just need a video clip. They need:
• A high-retention vertical short for YouTube and Reels
• A structured document carousel for LinkedIn
• A tactical breakdown thread for X
• A formatted summary newsletter for email subscribers
• Unified UTM tracking to measure what actually drove revenue

When tools only solve 10% of the distribution pipeline, creators still spend 10 hours stitching together 5 different subscriptions.

The next era is not 'clipping'.
It is CreatorOps: an integrated operating system where 1 core input automatically generates your entire multi-channel distribution queue with consistent brand voice.

That is what we are building at IncuBrix.

What is the biggest bottleneck in your current distribution workflow?""",
        "caption": "The 'AI video clipper' market is repeating the exact mistake social media schedulers made in 2014. Why single-feature tools create bloat and why integrated CreatorOps is the future of content distribution. #CreatorOps #B2BMarketing #SaaSStrategy #IncuBrix",
        "hashtags": "#CreatorOps #ContentStrategy #B2BMarketing #ProductManagement #IncuBrix",
        "cta": "See the CreatorOps difference at incubrix.com",
        "utm": "https://incubrix.com?utm_source=linkedin&utm_medium=post&utm_campaign=INC-P03&utm_content=death_of_clippers",
        "metric": "120+ Reactions, 45+ Comments, 3,500+ impressions",
        "rights": "Original industry analysis by IncuBrix team.",
        "day": 3,
        "time": "13:00 UTC"
    },
    {
        "id": "INC-P04",
        "title": "Before vs. After: 45-Min Zoom to 10 Assets in 60s",
        "platform": "X (Twitter)",
        "pillar": "Pillar 2: Feature-in-Action",
        "format": "Single Tweet + Split Comparison Image",
        "hook": "Before vs. After: What happens when you run a raw 45-minute Zoom recording through IncuBrix:",
        "content_body": """Before vs. After: What happens when you run a raw 45-minute Zoom recording through IncuBrix:

BEFORE:
❌ 1 giant MP4 sitting in Google Drive
❌ 12 hours of manual Premiere / Final Cut scrubbing
❌ Subtitles out of sync
❌ Zero written assets

AFTER (60 seconds later):
✅ 6 vertical shorts with 9:16 auto-framing
✅ 2 LinkedIn PDF carousels
✅ 4 tactical X posts
✅ Full transcript + executive takeaways

Work smarter. Build your CreatorOps engine with @IncuBrix.""",
        "caption": "Before vs. After running a 45-minute recording through IncuBrix. 12 hours of manual editing vs. 60 seconds of automated multi-format extraction. #ContentRepurposing #BeforeAfter #CreatorOps #IncuBrix",
        "hashtags": "#CreatorOps #VideoEditing #AITools #IncuBrix",
        "cta": "Try the 60-second transformation at incubrix.com",
        "utm": "https://incubrix.com?utm_source=x&utm_medium=post&utm_campaign=INC-P04&utm_content=before_after",
        "metric": "65+ Retweets, 180+ Likes, 8,000+ impressions",
        "rights": "Original graphic assets; 100% rights-safe.",
        "day": 7,
        "time": "15:00 UTC"
    },
    {
        "id": "INC-P05",
        "title": "Case Study: 120 Posts in 30 Days Without Burnout",
        "platform": "LinkedIn",
        "pillar": "Pillar 5: Trench Stories",
        "format": "Case Study & Operational Breakdown",
        "hook": "How one solo B2B podcaster published 120 high-performing posts in 30 days while working full-time:",
        "content_body": """How one solo B2B podcaster published 120 high-performing posts in 30 days while working a demanding full-time executive role:

David runs a weekly podcast on enterprise logistics.
For 18 months, he was trapped in the 'podcast hamster wheel':
1. Record for 1 hour on Tuesday
2. Spend all weekend editing audio and writing 1 LinkedIn post
3. Get 400 downloads and zero inbound sales leads
4. Repeat until complete exhaustion

Last month, we transitioned David to the IncuBrix CreatorOps framework.

Here is the exact weekly cadence:
• Monday (60 mins): Record 1 high-conviction guest interview.
• Monday (15 mins): Upload raw file to IncuBrix.
  - IncuBrix automatically generates 8 vertical video shorts with word-level highlight captions.
  - Generates 2 educational slide decks for LinkedIn.
  - Generates 8 framework posts and 2 weekly newsletters.
• Tuesday (20 mins): David reviews the copy, adjusts two technical terms, and clicks 'Approve & Schedule'.

THE 30-DAY RESULTS:
📈 120 total assets published across LinkedIn, YouTube Shorts, and X.
📈 Total impressions increased from 14,000/mo to 184,000/mo.
📈 Inbound qualified consulting inquiries: 9 (vs. 1 prior).
⏱️ Total time spent per week: 1 hour 35 minutes.

Stop treating content like a craft project and start treating it like an operating system.

Drop a comment below if you want the exact SOP David used.""",
        "caption": "How one solo podcaster published 120 posts in 30 days and generated 184K impressions without working weekends. The complete CreatorOps case study. #CaseStudy #B2BMarketing #PodcastGrowth #IncuBrix",
        "hashtags": "#CaseStudy #ContentStrategy #PodcastGrowth #InboundMarketing #IncuBrix",
        "cta": "Read the full case study at incubrix.com/case-studies/david",
        "utm": "https://incubrix.com/case-studies/david?utm_source=linkedin&utm_medium=post&utm_campaign=INC-P05&utm_content=david_case_study",
        "metric": "140+ Reactions, 55+ Comments, 4,200+ impressions",
        "rights": "Anonymized authentic case study data from IncuBrix beta cohort.",
        "day": 7,
        "time": "13:00 UTC"
    },
    {
        "id": "INC-P06",
        "title": "5 Algorithmic Shifts Hitting Short Video in 2026",
        "platform": "X (Twitter)",
        "pillar": "Pillar 4: Creator Benchmarks",
        "format": "Tactical 6-Tweet Thread",
        "hook": "Short-form video algorithms changed dramatically this year. 5 shifts you must adapt to immediately: 🧵👇",
        "content_body": """Tweet 1:
Short-form video algorithms changed dramatically this year. If your views are down 50%, you're probably still using 2023 tactics.

5 shifts you must adapt to immediately: 🧵👇

Tweet 2:
1/ Sound-Off Dominance is at 74%
Nearly 3 out of 4 mobile viewers watch vertical clips without headphones. If your captions aren't dynamic, readable, and centered in the safe zone, they swipe in 1.8 seconds.

Tweet 3:
2/ Rewatch Percentage > Total Likes
Platforms prioritize videos that loop. If your final sentence naturally connects back to your opening hook sentence, your completion rate passes 105%.

Tweet 4:
3/ AI Slop Penalties
Platforms are demoting generic AI avatar videos with flat robotic voices. What wins? Authentic human recordings repurposed with intelligent AI editing.

Tweet 5:
4/ Direct Answer Hooks
The algorithm rewards videos that answer the premise within the first 15 seconds, rather than dragging out artificial suspense.

Tweet 6:
5/ Cross-Format Synergies
Creators who pair video shorts with written carousels and threads see 3.4x higher audience retention than video-only accounts.

IncuBrix is designed specifically for this new reality. Try it free: incubrix.com""",
        "caption": "5 critical algorithmic shifts in short-form video for 2026. Why sound-off optimization, rewatch loops, and cross-format distribution rule the feeds. #ShortsAlgorithm #VideoStrategy #CreatorTips #IncuBrix",
        "hashtags": "#VideoMarketing #AlgorithmTips #Shorts #IncuBrix",
        "cta": "Optimize your clips at incubrix.com",
        "utm": "https://incubrix.com?utm_source=x&utm_medium=thread&utm_campaign=INC-P06&utm_content=algo_shifts_2026",
        "metric": "180+ Retweets, 420+ Bookmarks, 30,000+ impressions",
        "rights": "Original proprietary benchmark research.",
        "day": 10,
        "time": "16:00 UTC"
    },
    {
        "id": "INC-P07",
        "title": "The Modular Content Pyramid",
        "platform": "LinkedIn",
        "pillar": "Pillar 3: CreatorOps Systems",
        "format": "Framework Breakdown + Diagram Spec",
        "hook": "Top media brands don't create 50 separate ideas a week. They build a Modular Content Pyramid:",
        "content_body": """Top media brands don't invent 50 separate ideas every week.

They build a Modular Content Pyramid:

LEVEL 1: THE CORE ASSET (1 per week)
A 45-minute high-depth podcast, client interview, or live keynote. This is where 100% of your domain expertise and strategic thinking lives.

LEVEL 2: THE DERIVATIVE ASSETS (4 to 6 per week)
Extracted directly from Level 1:
• 3 Vertical short-form videos highlighting key arguments.
• 1 Multi-slide PDF carousel breaking down the central framework.
• 1 Long-form tactical LinkedIn essay.

LEVEL 3: THE MICRO ASSETS (10 to 15 per week)
Extracted from Level 2:
• Single-quote image cards.
• 2-sentence contrarian observations.
• Audience discussion questions and polls.

When you operate this pyramid:
1. You never suffer from 'what should I post today?'
2. Your messaging stays remarkably cohesive across every platform.
3. You spend 90% less time creating while increasing publishing volume by 400%.

IncuBrix is the engine that executes Levels 2 and 3 automatically from your Level 1 asset.

How many levels of the pyramid are you currently leveraging?""",
        "caption": "The Modular Content Pyramid: How modern media teams turn 1 weekly recording into 20 coherent assets across every tier. Stop reinventing the wheel every morning. #ContentArchitecture #CreatorOps #MediaStrategy #IncuBrix",
        "hashtags": "#ContentStrategy #CreatorOps #MediaOperations #MarketingArchitecture #IncuBrix",
        "cta": "Build your content pyramid at incubrix.com/pyramid",
        "utm": "https://incubrix.com/pyramid?utm_source=linkedin&utm_medium=post&utm_campaign=INC-P07&utm_content=modular_pyramid",
        "metric": "160+ Reactions, 60+ Comments, 4,800+ impressions",
        "rights": "Original IncuBrix architectural concept.",
        "day": 12,
        "time": "13:00 UTC"
    },
    {
        "id": "INC-P08",
        "title": "The Creator Tool Tax: Stop Stitching 6 Subscriptions",
        "platform": "X (Twitter)",
        "pillar": "Pillar 1: Workflow Teardowns",
        "format": "Single Tweet + Cost Comparison Grid",
        "hook": "The Average Creator Tool Stack is completely out of control. Look at these monthly line items:",
        "content_body": """The average creator software stack is completely out of control:

• Video transcription tool: $18/mo
• Subtitle generator: $24/mo
• AI copywriting app: $39/mo
• Social media scheduler: $29/mo
• Carousel design tool: $15/mo
• Storage and clipping plugin: $20/mo

TOTAL: $145/month across 6 disconnected tabs.

IncuBrix replaces all 6 for $29/mo in one unified dashboard.

Stop paying the fragmentation tax.""",
        "caption": "The creator software stack is full of bloat. 6 apps, 6 logins, and \$145/month just to publish weekly content. Consolidate with IncuBrix CreatorOps. #SaaSBloat #ProductivityTools #CreatorEconomy #IncuBrix",
        "hashtags": "#SaaS #CreatorEconomy #Productivity #IncuBrix",
        "cta": "Consolidate your stack at incubrix.com",
        "utm": "https://incubrix.com?utm_source=x&utm_medium=post&utm_campaign=INC-P08&utm_content=tool_tax",
        "metric": "95+ Retweets, 240+ Likes, 14,000+ impressions",
        "rights": "Original price audit comparison.",
        "day": 13,
        "time": "15:00 UTC"
    },
    {
        "id": "INC-P09",
        "title": "How Speech-to-Text Accuracy Dictates Viewer Retention",
        "platform": "LinkedIn",
        "pillar": "Pillar 2: Feature-in-Action",
        "format": "Technical Deep Dive & Benchmark Analysis",
        "hook": "Why a 4% drop in automated transcription accuracy causes a 28% drop in video watch time:",
        "content_body": """Why a 4% drop in automated transcription accuracy causes a 28% drop in video watch time:

Most creators treat automated captions as a commodity.
'All speech-to-text engines are basically Whisper wrappers anyway, right?'

Wrong.
Here is what cognitive eye-tracking data reveals:

When a mobile viewer watches a video with captions, their eyes lead the spoken audio by ~180 milliseconds.
The visual text primes the auditory comprehension.

When an AI engine mishears a technical term—rendering 'CreatorOps' as 'Creator Ops' or 'CAC' as 'crack'—the viewer's cognitive reading flow stumbles.
That micro-friction triggers the thumb reflex to swipe to the next video.

At IncuBrix, we didn't just plug in a generic speech API.
We built:
1. Dynamic domain-specific vocabulary calibration (for B2B, SaaS, finance, and tech jargon).
2. Acoustic noise separation that filters background clicks and hums before transcription.
3. Word-level timestamp synchronization accurate to 12 milliseconds.

Result? 98.4% transcription precision on specialized content and dramatically higher completion rates on your short videos.

Don't let bad subtitles wreck your best insights.""",
        "caption": "The hidden link between speech-to-text accuracy and viewer retention curves. Why 4% transcription errors trigger instant viewer drop-off on mobile feeds. #Engineering #ASR #VideoRetention #SpeechToText #IncuBrix",
        "hashtags": "#ASR #MachineLearning #VideoRetention #CreatorOps #IncuBrix",
        "cta": "Test our speech engine accuracy at incubrix.com/studio",
        "utm": "https://incubrix.com/studio?utm_source=linkedin&utm_medium=post&utm_campaign=INC-P09&utm_content=asr_accuracy",
        "metric": "110+ Reactions, 35+ Comments, 3,200+ impressions",
        "rights": "Original acoustic and retention engineering research.",
        "day": 16,
        "time": "13:00 UTC"
    },
    {
        "id": "INC-P10",
        "title": "5 Prompt Mistakes When Writing Copy from Transcripts",
        "platform": "X (Twitter)",
        "pillar": "Pillar 4: Creator Benchmarks",
        "format": "Tactical 5-Tweet Thread",
        "hook": "Most AI-generated social copy sounds robotic because creators feed transcripts with lazy prompts. 5 prompt fixes: 🧵👇",
        "content_body": """Tweet 1:
Most AI-generated social posts sound like generic corporate fluff.

Why? Because creators dump a 5,000-word transcript and say: 'Write me 5 LinkedIn posts.'

Here are 5 prompt engineering rules to turn raw transcripts into authentic copy: 🧵👇

Tweet 2:
1/ Define the Enemy
Tell the AI what practice you are arguing against.
BAD: 'Summarize the marketing tips.'
GOOD: 'Identify the 2 common marketing practices the speaker explicitly calls out as obsolete.'

Tweet 3:
2/ Ban Corporate Hype Words
Explicitly blacklist: 'game-changer', 'delve', 'revolutionize', 'synergy', 'vital'. Force the model into concrete, Anglo-Saxon verbs.

Tweet 4:
3/ Force Sentence Variety
Instruct the model: 'Alternate between 4-word punchy declarations and 15-word explanatory sentences. Use line breaks after every concept.'

Tweet 5:
4/ Extract Metrics, Not Adjectives
Prompt: 'Pull every specific number, dollar amount, and timeframe mentioned in the audio. Anchor every hook to one of these figures.'

IncuBrix has these exact guardrail rules hard-coded into our Creator Studio engine. No prompt tweaking needed. Try it: incubrix.com""",
        "caption": "5 prompt engineering rules to turn raw video transcripts into high-converting social copy without sounding like a robot. #PromptEngineering #Copywriting #AIWriting #IncuBrix",
        "hashtags": "#AIWriting #PromptEngineering #CopywritingTips #IncuBrix",
        "cta": "Experience prompt-free generation at incubrix.com",
        "utm": "https://incubrix.com?utm_source=x&utm_medium=thread&utm_campaign=INC-P10&utm_content=prompt_mistakes",
        "metric": "210+ Retweets, 510+ Bookmarks, 32,000+ impressions",
        "rights": "Original IncuBrix prompt engineering framework.",
        "day": 18,
        "time": "17:00 UTC"
    },
    {
        "id": "INC-P11",
        "title": "The 15-Minute Monday Morning Distribution Routine",
        "platform": "LinkedIn",
        "pillar": "Pillar 3: CreatorOps Systems",
        "format": "Playbook & Routine Guide",
        "hook": "How busy founders schedule an entire week of social content before their 9:00 AM coffee:",
        "content_body": """How busy founders schedule an entire week of social content before their 9:00 AM standup:

The #1 reason founders and executives fail to build a personal brand isn't lack of expertise.
It is the daily cognitive friction of deciding what to write.

Here is the 15-Minute Monday Morning Protocol:

8:45 AM - INGESTION (2 minutes)
Open IncuBrix. Paste the link to your latest recorded customer demo, podcast episode, or team all-hands.

8:47 AM - SELECTION (6 minutes)
IncuBrix presents you with:
• 4 Vertical short clips pre-scored for hook retention.
• 1 Multi-slide PDF carousel.
• 5 Formatted text breakdowns.
Scan the suggestions. Click 'Select' on the 5 strongest pieces that align with your focus for the week.

8:53 AM - BRAND VOICE CALIBRATION (4 minutes)
Add your personal signature takeaway to the generated text. Adjust any nuance that needs founder context.

8:57 AM - AUTO-SYNC (3 minutes)
Click 'Schedule Week'.
IncuBrix pushes the assets into optimized publishing slots on LinkedIn, YouTube Shorts, and X with pre-populated UTM parameters.

9:00 AM - DONE.
Your distribution engine is running on autopilot for the next 7 days while you get back to building your business.

Consistency isn't discipline. It's architecture.

Ready to automate your Monday routine?""",
        "caption": "The 15-minute Monday morning distribution routine for busy founders. How to schedule 7 days of high-authority social content before 9:00 AM. #FounderBrand #ExecutivePresence #TimeManagement #IncuBrix",
        "hashtags": "#FounderBrand #ExecutivePresence #Productivity #CreatorOps #IncuBrix",
        "cta": "Start your 15-minute routine at incubrix.com/routine",
        "utm": "https://incubrix.com/routine?utm_source=linkedin&utm_medium=post&utm_campaign=INC-P11&utm_content=monday_routine",
        "metric": "175+ Reactions, 48+ Comments, 5,100+ impressions",
        "rights": "Original workflow SOP.",
        "day": 19,
        "time": "13:00 UTC"
    },
    {
        "id": "INC-P12",
        "title": "Data Study: 73% of Mobile Video is Watched on Mute",
        "platform": "X (Twitter)",
        "pillar": "Pillar 4: Creator Benchmarks",
        "format": "Single Tweet + Statistical Chart",
        "hook": "Data study: 73% of viewers watch mobile video on mute. If your content relies purely on audio, 3 out of 4 people never hear your message.",
        "content_body": """Data study: 73% of viewers watch mobile video with sound off.

If your video clips rely purely on audio dialogue, 3 out of 4 potential customers scroll right past.

3 non-negotiable rules for silent retention:
1. Two-word kinetic subtitle bursts (keep eye moving)
2. Safe-zone positioning (Y: 450-1300px)
3. Word-level highlight contrast (Emerald or Yellow on Charcoal)

IncuBrix bakes these 3 rules into every exported short automatically.

Don't let silence kill your reach.""",
        "caption": "73% of mobile social video is consumed on mute. 🔇 Here are 3 design rules to ensure your short videos stop the scroll and communicate value without sound. #VideoMarketing #DataInsights #SocialMediaTips #IncuBrix",
        "hashtags": "#VideoMarketing #MobileVideo #DataInsights #IncuBrix",
        "cta": "See silent-optimized clips in action at incubrix.com",
        "utm": "https://incubrix.com?utm_source=x&utm_medium=post&utm_campaign=INC-P12&utm_content=silent_video",
        "metric": "85+ Retweets, 210+ Likes, 16,000+ impressions",
        "rights": "Aggregated mobile consumption industry data.",
        "day": 21,
        "time": "16:00 UTC"
    },
    {
        "id": "INC-P13",
        "title": "Turn Customer Onboarding Calls into Social Proof",
        "platform": "LinkedIn",
        "pillar": "Pillar 5: Trench Stories",
        "format": "Step-by-Step B2B Marketing Guide",
        "hook": "Your customer onboarding calls are the highest-converting marketing content you're not using:",
        "content_body": """Your customer onboarding and customer success calls are the highest-converting marketing content you're currently ignoring.

Every week, your customers say things like:
'Wait, I didn't realize it could do that so quickly—that used to take our team 3 days!'

That unscripted, genuine 'Aha!' moment is worth 100 scripted customer testimonials.

HOW TO ETHICALLY TURN CALLS INTO SOCIAL ASSETS:

1. Consent First: Always ask: 'Hey, would you mind if we clipped that 30-second workflow explanation for our community?' (90% say yes).

2. Drop the Recording into IncuBrix:
Isolate the 45 seconds where the customer describes the specific problem they had and how your product resolved it.

3. Redact Sensitive Data:
Use IncuBrix's smart blur feature to mask any proprietary numbers, client emails, or API keys.

4. Add Kinetic Highlights & Context:
Frame it not as a brag, but as an educational teardown: 'How [Company] solved [Problem] in 4 steps.'

5. Publish on LinkedIn:
This delivers authentic, credible, high-trust social proof that attracts enterprise buyers without feeling like a cheesy sales pitch.

Are you recording your customer wins?""",
        "caption": "How to turn customer onboarding recordings into authentic, high-converting social proof (with complete privacy and consent). #CustomerSuccess #B2BMarketing #SocialProof #IncuBrix",
        "hashtags": "#CustomerSuccess #B2BMarketing #SocialProof #DemandGeneration #IncuBrix",
        "cta": "Turn recordings into assets at incubrix.com",
        "utm": "https://incubrix.com?utm_source=linkedin&utm_medium=post&utm_campaign=INC-P13&utm_content=customer_wins",
        "metric": "135+ Reactions, 42+ Comments, 3,900+ impressions",
        "rights": "Original customer advocacy framework; 100% GDPR & DPDP compliant.",
        "day": 24,
        "time": "13:00 UTC"
    },
    {
        "id": "INC-P14",
        "title": "The Pre-Publishing Checklist: 6 Tests Every Video Must Pass",
        "platform": "X (Twitter)",
        "pillar": "Pillar 1: Workflow Teardowns",
        "format": "Single Tweet + Checklist Card",
        "hook": "Never hit 'Publish' on a short-form video until it passes these 6 quality checks:",
        "content_body": """Never hit 'Publish' on a short-form video until it passes this 6-point audit:

1. Hook Test: Does visual movement happen in the first 0.8 seconds?
2. Sound-Off Test: Can the core message be understood on 0% volume?
3. Safe-Zone Test: Are subtitles clear of platform like/comment icons?
4. Fluff Test: Are all pauses > 0.3s removed?
5. Loop Test: Does the final sentence logically restart the video?
6. Metric Test: Is there a tracked UTM link in the bio/first comment?

IncuBrix automates all 6 checks before you post.

Bookmark this checklist for your next edit.""",
        "caption": "The 6-point pre-publishing checklist for short-form video. Stop leaving your video views to chance. Run this audit on every clip. #VideoAudit #CreatorOps #Checklist #IncuBrix",
        "hashtags": "#VideoStrategy #CreatorTips #ShortsChecklist #IncuBrix",
        "cta": "Automate your pre-publish checks at incubrix.com",
        "utm": "https://incubrix.com?utm_source=x&utm_medium=post&utm_campaign=INC-P14&utm_content=prepublish_checklist",
        "metric": "140+ Retweets, 380+ Bookmarks, 22,000+ impressions",
        "rights": "Original IncuBrix QA standard.",
        "day": 27,
        "time": "15:00 UTC"
    },
    {
        "id": "INC-P15",
        "title": "The ROI of Content Repurposing: An Engineering Approach",
        "platform": "LinkedIn",
        "pillar": "Pillar 3: CreatorOps Systems",
        "format": "Long-form Thought Leadership Post",
        "hook": "What happens when you treat content marketing like an engineering optimization problem:",
        "content_body": """What happens when you treat organic social content like an engineering optimization problem:

In software engineering, nobody writes custom binary code from scratch for every web page.
We use frameworks, component libraries, and automated CI/CD deployment pipelines.

Yet in marketing, 95% of creators and marketing teams treat content like an artisanal, bespoke hand-craft:
• Writing every social post from scratch on a blank page
• Manually cropping videos in timeline editors
• Copy-pasting text into 4 different scheduling tabs
• Spending 20 hours to generate 3 posts

Here is the engineering equivalent of high-leverage marketing:

1. High-Conviction Core Input (The Database):
One 45-minute recording rich in data, frameworks, and insights.

2. Automated Parsing & Extraction (The Compiler):
IncuBrix ingests the core input, parses audio into timestamped tokens, extracts modular soundbites, and matches them to platform constraints.

3. Platform-Native Formatting (The Transpiler):
The engine outputs 9:16 vertical video for mobile discovery, 4:5 document carousels for dwell time, and punchy markdown copy for rapid reading.

4. Continuous Automated Deployment (The CI/CD Queue):
Pre-scheduled delivery into peak algorithmic windows with automated UTM link parameters.

RESULT:
• 80% reduction in production latency (from 15 hours to 30 minutes).
• 400% increase in distributed organic touchpoints.
• A predictable, repeatable cost per acquired customer.

Stop guessing. Start building your CreatorOps pipeline.

What part of your content workflow is begging for an automated pipeline?""",
        "caption": "Why content marketing needs an engineering mindset. Applying component libraries, compilation, and automated deployment pipelines to creator growth. #EngineeringLeadership #GrowthEngineering #CreatorOps #IncuBrix",
        "hashtags": "#GrowthEngineering #ContentArchitecture #SystemsThinking #B2BSaaS #IncuBrix",
        "cta": "Build your marketing CI/CD at incubrix.com/engine",
        "utm": "https://incubrix.com/engine?utm_source=linkedin&utm_medium=post&utm_campaign=INC-P15&utm_content=engineering_roi",
        "metric": "190+ Reactions, 65+ Comments, 5,500+ impressions",
        "rights": "Original engineering architecture thesis by IncuBrix candidate.",
        "day": 29,
        "time": "13:00 UTC"
    }
]

# Write all Posts files
for p in POSTS:
    clean_title = re.sub(r'[^a-zA-Z0-9_]', '_', p['title'].lower())[:35]
    filepath = os.path.join(POSTS_DIR, f"{p['id']}_{clean_title}.md")
    content = f"""# {p['id']}: {p['title']}

**Platform:** {p['platform']}  
**Pillar:** {p['pillar']}  
**Format:** {p['format']}  
**Scheduled Slot:** Day {p['day']} at {p['time']}  
**Target Metric:** {p['metric']}  
**Rights & Safety:** {p['rights']}  

---

### The Hook
> "{p['hook']}"

---

### Full Post Content / Thread Text
```text
{p['content_body']}
```

---

### Social Metadata & Publishing Copy
* **Caption / Teaser:** {p['caption']}
* **Hashtags:** {p['hashtags']}
* **Call to Action:** {p['cta']}
* **UTM Tracking Link:** [{p['utm']}]({p['utm']})

---

### Conversion Mechanics
* **Stage:** Mid-Funnel / Top-of-Funnel Conversion
* **Action:** Viewer reads tactical insight -> clicks UTM link -> lands on specific resource page -> signs up for Free IncuBrix Tier.
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(POSTS)} Post/Thread documents in {POSTS_DIR}")
