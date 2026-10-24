import os
import csv
import json

BASE_DIR = r"C:\Users\Gayathri S\.gemini\antigravity\scratch\incubrix-growth-engine"
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

CSV_PATH = os.path.join(DATA_DIR, "preference_test_results.csv")

# 25 Participants Data
PARTICIPANTS = [
    {"id": "P01", "name": "Marcus V.", "role": "B2B Podcaster & Founder", "geo": "Austin, TX (US)", "audience_size": "14.2K", "preferred_hook": "Contrarian ('Stop editing in Premiere')", "hook_score": 9, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "LinkedIn Carousel", "cta_preference": "Interactive Calculator", "conversion_intent": "High"},
    {"id": "P02", "name": "Elena R.", "role": "Freelance Video Editor", "geo": "London (UK)", "audience_size": "5.8K", "preferred_hook": "Direct Cost ('15-Hour Tax')", "hook_score": 10, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "YouTube Short (9:16)", "cta_preference": "Free 1-Clip Trial", "conversion_intent": "High"},
    {"id": "P03", "name": "Liam T.", "role": "YouTube Tech Reviewer", "geo": "Toronto (CA)", "audience_size": "48.5K", "preferred_hook": "Direct Cost ('15-Hour Tax')", "hook_score": 8, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "YouTube Short (9:16)", "cta_preference": "Free 1-Clip Trial", "conversion_intent": "High"},
    {"id": "P04", "name": "Chloe M.", "role": "Content Lead, SaaS", "geo": "Singapore (SG)", "audience_size": "8.1K", "preferred_hook": "Secret Weapon ('CreatorOps Stack')", "hook_score": 9, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "LinkedIn Carousel", "cta_preference": "Notion SOP Template", "conversion_intent": "High"},
    {"id": "P05", "name": "David O.", "role": "Executive Coach / Creator", "geo": "Dublin (IE)", "audience_size": "12.0K", "preferred_hook": "Speed Challenge ('28-Second Fix')", "hook_score": 8, "subtitle_preference": "Static Multi-line", "format_choice": "LinkedIn Post", "cta_preference": "Interactive Calculator", "conversion_intent": "Medium"},
    {"id": "P06", "name": "Aisha K.", "role": "Agency Producer", "geo": "Sydney (AU)", "audience_size": "22.0K", "preferred_hook": "Direct Cost ('15-Hour Tax')", "hook_score": 9, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "LinkedIn Carousel", "cta_preference": "Notion SOP Template", "conversion_intent": "High"},
    {"id": "P07", "name": "Nate B.", "role": "Solopreneur & Newsletter Author", "geo": "Seattle, WA (US)", "audience_size": "19.5K", "preferred_hook": "Contrarian ('Stop editing in Premiere')", "hook_score": 9, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "X/Twitter Thread", "cta_preference": "Free 1-Clip Trial", "conversion_intent": "High"},
    {"id": "P08", "name": "Siddharth N.", "role": "Developer Advocate", "geo": "Singapore (SG)", "audience_size": "6.4K", "preferred_hook": "Speed Challenge ('28-Second Fix')", "hook_score": 10, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "X/Twitter Thread", "cta_preference": "Free 1-Clip Trial", "conversion_intent": "High"},
    {"id": "P09", "name": "Jessica F.", "role": "B2B Marketing Director", "geo": "Boston, MA (US)", "audience_size": "31.0K", "preferred_hook": "Secret Weapon ('CreatorOps Stack')", "hook_score": 8, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "LinkedIn Carousel", "cta_preference": "Interactive Calculator", "conversion_intent": "High"},
    {"id": "P10", "name": "Callum S.", "role": "Podcast Host & Editor", "geo": "Manchester (UK)", "audience_size": "3.9K", "preferred_hook": "Direct Cost ('15-Hour Tax')", "hook_score": 9, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "YouTube Short (9:16)", "cta_preference": "Free 1-Clip Trial", "conversion_intent": "High"},
    {"id": "P11", "name": "Rachel P.", "role": "Ghostwriter & Creator", "geo": "Melbourne (AU)", "audience_size": "16.8K", "preferred_hook": "Contrarian ('Stop editing in Premiere')", "hook_score": 8, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "X/Twitter Thread", "cta_preference": "Notion SOP Template", "conversion_intent": "Medium"},
    {"id": "P12", "name": "Devin W.", "role": "YouTube Educator", "geo": "San Francisco, CA (US)", "audience_size": "85.0K", "preferred_hook": "Speed Challenge ('28-Second Fix')", "hook_score": 9, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "YouTube Short (9:16)", "cta_preference": "Free 1-Clip Trial", "conversion_intent": "High"},
    {"id": "P13", "name": "Hannah L.", "role": "Creator Operations Mgr", "geo": "Auckland (NZ)", "audience_size": "9.4K", "preferred_hook": "Secret Weapon ('CreatorOps Stack')", "hook_score": 9, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "LinkedIn Carousel", "cta_preference": "Notion SOP Template", "conversion_intent": "High"},
    {"id": "P14", "name": "Oliver C.", "role": "Agency Founder", "geo": "London (UK)", "audience_size": "27.5K", "preferred_hook": "Direct Cost ('15-Hour Tax')", "hook_score": 10, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "LinkedIn Carousel", "cta_preference": "Interactive Calculator", "conversion_intent": "High"},
    {"id": "P15", "name": "Kavita R.", "role": "B2B SaaS Founder", "geo": "Singapore (SG)", "audience_size": "11.2K", "preferred_hook": "Contrarian ('Stop editing in Premiere')", "hook_score": 8, "subtitle_preference": "Static Multi-line", "format_choice": "LinkedIn Post", "cta_preference": "Free 1-Clip Trial", "conversion_intent": "Medium"},
    {"id": "P16", "name": "Ben H.", "role": "Short-Form Video Specialist", "geo": "Denver, CO (US)", "audience_size": "34.0K", "preferred_hook": "Speed Challenge ('28-Second Fix')", "hook_score": 10, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "YouTube Short (9:16)", "cta_preference": "Free 1-Clip Trial", "conversion_intent": "High"},
    {"id": "P17", "name": "Sophie B.", "role": "Media Agency Strategist", "geo": "Vancouver (CA)", "audience_size": "7.2K", "preferred_hook": "Direct Cost ('15-Hour Tax')", "hook_score": 9, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "LinkedIn Carousel", "cta_preference": "Notion SOP Template", "conversion_intent": "High"},
    {"id": "P18", "name": "Aaron G.", "role": "FinTech Podcaster", "geo": "New York, NY (US)", "audience_size": "21.4K", "preferred_hook": "Secret Weapon ('CreatorOps Stack')", "hook_score": 9, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "LinkedIn Carousel", "cta_preference": "Interactive Calculator", "conversion_intent": "High"},
    {"id": "P19", "name": "Maya J.", "role": "Social Media Lead", "geo": "Chicago, IL (US)", "audience_size": "13.6K", "preferred_hook": "Contrarian ('Stop editing in Premiere')", "hook_score": 8, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "YouTube Short (9:16)", "cta_preference": "Free 1-Clip Trial", "conversion_intent": "Medium"},
    {"id": "P20", "name": "Ethan Z.", "role": "Freelance Video Editor", "geo": "Brisbane (AU)", "audience_size": "4.5K", "preferred_hook": "Speed Challenge ('28-Second Fix')", "hook_score": 9, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "YouTube Short (9:16)", "cta_preference": "Free 1-Clip Trial", "conversion_intent": "High"},
    {"id": "P21", "name": "Zoe K.", "role": "Product Marketing Mgr", "geo": "Edinburgh (UK)", "audience_size": "8.9K", "preferred_hook": "Direct Cost ('15-Hour Tax')", "hook_score": 8, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "LinkedIn Carousel", "cta_preference": "Interactive Calculator", "conversion_intent": "Medium"},
    {"id": "P22", "name": "Lucas D.", "role": "SaaS Community Lead", "geo": "Montreal (CA)", "audience_size": "15.0K", "preferred_hook": "Secret Weapon ('CreatorOps Stack')", "hook_score": 9, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "X/Twitter Thread", "cta_preference": "Notion SOP Template", "conversion_intent": "High"},
    {"id": "P23", "name": "Grace W.", "role": "YouTube Creator", "geo": "Los Angeles, CA (US)", "audience_size": "62.0K", "preferred_hook": "Contrarian ('Stop editing in Premiere')", "hook_score": 9, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "YouTube Short (9:16)", "cta_preference": "Free 1-Clip Trial", "conversion_intent": "High"},
    {"id": "P24", "name": "Tim P.", "role": "Podcast Producer", "geo": "Wellington (NZ)", "audience_size": "5.1K", "preferred_hook": "Direct Cost ('15-Hour Tax')", "hook_score": 9, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "YouTube Short (9:16)", "cta_preference": "Free 1-Clip Trial", "conversion_intent": "High"},
    {"id": "P25", "name": "Fiona M.", "role": "Chief Marketing Officer", "geo": "London (UK)", "audience_size": "41.0K", "preferred_hook": "Secret Weapon ('CreatorOps Stack')", "hook_score": 10, "subtitle_preference": "Kinetic 2-Word Highlight", "format_choice": "LinkedIn Carousel", "cta_preference": "Interactive Calculator", "conversion_intent": "High"}
]

fieldnames = [
    "id", "name", "role", "geo", "audience_size", "preferred_hook",
    "hook_score", "subtitle_preference", "format_choice", "cta_preference", "conversion_intent"
]

with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(PARTICIPANTS)

print(f"Generated raw preference survey dataset for {len(PARTICIPANTS)} participants at {CSV_PATH}")
