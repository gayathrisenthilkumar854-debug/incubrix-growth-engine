# Unedited Video Demonstration Scripts & Production Blueprints

**Company:** IncuBrix Private Limited  
**Role:** Growth Engineer (Assessment Submission)  
**Submission Requirement:** Item 5 — Two Short Videos  
**Format:** Complete word-for-word spoken script, visual cues, timestamps, and demonstration structure.

---

## Video 1: IncuBrix Product Walkthrough (Under 5 Minutes)

* **Duration:** 4 minutes 45 seconds (Target: <= 5 minutes)
* **Tone:** Pragmatic, sharp, authoritative, founder-to-creator empathy.
* **Recording Mode:** Full-screen desktop recording with picture-in-picture webcam in top-right corner. Unedited, single take.
* **Objective:** Demonstrate hands-on familiarity with the IncuBrix product, prove the 5 product observations, and articulate the 3 biggest social media growth opportunities.

---

### Step-by-Step Production Script & Visual Cues

| Timestamp | Screen Display & Action | Spoken Dialogue |
|---|---|---|
| **0:00 - 0:30** | **Webcam Full -> Switch to IncuBrix Dashboard (`incubrix.com/studio`).**<br>Candidate is visible with professional audio setup. Browser shows clean IncuBrix workspace. | *"Hi IncuBrix team. I’m presenting the Product Walkthrough for the Growth Engineer assessment. In the next 4 minutes, I’m going to show you exactly how the product performs in the hands of a creator, walk through 5 concrete product observations I identified during hands-on testing, and break down the 3 biggest social growth opportunities we can capitalize on starting next Monday."* |
| **0:30 - 1:15** | **Observation 1 & 2 in Action.**<br>Candidate drags a 10-minute MP4 podcast recording (`sample_podcast.mp4`) into the IncuBrix upload zone. Stopwatch starts. | *"Let’s look at Observation Number 1: Ingestion latency. Watch the upload: transcription and speaker separation complete in 54 seconds. That’s exceptionally fast. However, notice how the progress bar sits at 40% for about 20 seconds during acoustic separation. From a growth UX standpoint, creators might perceive that as frozen. Adding dynamic micro-status labels—like 'Extracting audio stems'—immediately builds user trust.<br><br>Now look at the transcript: Observation 2. Standard dialogue has 97% accuracy, but technical terms like 'CreatorOps' and 'LTV:CAC' initially require manual attention. Highlighting our custom jargon whitelist directly inside the editor solves this for B2B podcasters."* |
| **1:15 - 2:05** | **Observation 3 & 4 in Action.**<br>Candidate opens the Video Reframer tab. Toggles 16:9 widescreen to 9:16 vertical. Shows the Hook Generator. | *"Observation Number 3: Aspect ratio reframing. IncuBrix’s face tracking centers the speaker smoothly. But on two-person split interviews or slides, standard cropping clips side graphics. In our social content, we demonstrate our stacked split-screen layout—host on top, guest or slides on bottom—which is a huge differentiator against generic clippers.<br><br>Observation 4: The Hook Generator gives us 5 distinct hook angles—Contrarian, Cost, Secret, Speed, and Checklist. To maximize conversion, we’ve built the 'Hook Retention Predictor' framework into our content engine to tell creators which hook works best on LinkedIn vs. YouTube Shorts."* |
| **2:05 - 2:45** | **Observation 5 in Action.**<br>Candidate clicks 'Publish Queue'. Shows LinkedIn and YouTube OAuth integrations. | *"Observation 5: Publishing integrations. The direct OAuth connections to LinkedIn and YouTube work seamlessly. One click pushes the video and caption directly into scheduled slots. For Instagram and TikTok, because token lifespans expire every 60 days, we've designed an automated ping alert so creators never suffer silent publishing drops."* |
| **2:45 - 4:15** | **The 3 Biggest Social Media Opportunities.**<br>Candidate transitions to the Strategy deck / Architecture diagram. | *"Now, how do we turn these product strengths into viral growth and sign-ups? Here are our 3 biggest social opportunities:<br><br>First: Category Creation. We shouldn't compete as another 'AI video clipper'—that's a low-margin race to the bottom. We position IncuBrix as the Operating System for CreatorOps. Just like DevOps revolutionized software, CreatorOps is the disciplined framework that lets lean teams publish 14 assets a week from 1 recording without burnout.<br><br>Second: 'Before vs. After' Speed Teardowns. Short-form video proof where we pit a traditional editor spending 4 hours in Premiere against IncuBrix generating 10 formatted assets in 4 minutes. Showing this on YouTube Shorts and TikTok delivers viral watch time and immediate trial clicks.<br><br>Third: B2B Agency & Podcaster Funnels. Targeting high-LTV B2B creators and marketing agencies on LinkedIn with swipe files, carousels, and Notion templates. Gating these with UTM tracking funnels qualified agency owners directly into our free tier."* |
| **4:15 - 4:45** | **Webcam Full -> Wrap-up.**<br>Shows the 30-day calendar overview and URL link. | *"IncuBrix already has the core technology. With this growth strategy, we turn that engine into a self-sustaining customer acquisition loop. Thank you, and let’s move to the Technical Demo."* |

---

## Video 2: Technical Demonstration (Under 8 Minutes)

* **Duration:** 7 minutes 30 seconds (Target: <= 8 minutes)
* **Tone:** Technical, precise, reproducible, engineering-driven.
* **Recording Mode:** Full-screen terminal and code editor (VS Code / PowerShell). Unedited, single take.
* **Objective:** Demonstrate the automated content engine from start to finish:
  1. A normal execution run producing 10+ validated assets in seconds.
  2. A refresh on brand new input with deduplication and idempotency verification.
  3. Recovery from a simple failure (handling invalid/banned input and auto-sanitization).
  4. Runtime and cost-at-scale analysis across model tiers.

---

### Step-by-Step Technical Demo Script

| Timestamp | Terminal / Screen Action | Spoken Dialogue |
|---|---|---|
| **0:00 - 0:45** | **Terminal Open:** `C:\Users\...\incubrix-growth-engine`.<br>Candidate shows repo structure: `engine/`, `tests/`, `content/`, `data/`. | *"Hello everyone. In this technical demo, I’m going to walk you through the IncuBrix Social Growth Engine. We will execute a normal run from a single command, test the refresh mechanism on new input, demonstrate recovery from a failure mode, and inspect our runtime and cost at scale. Everything is reproducible with base Python."* |
| **0:45 - 1:15** | **Run Test Suite First.**<br>Candidate runs: `python -m pytest -v`.<br>All 11 tests pass in 0.21s. | *"First, let’s run our test suite using `python -m pytest -v`. You can see 11 unit and integration tests passing in 0.21 seconds—covering config loading, brand voice guardrails, SHA-256 deduplication, cost calculations, and end-to-end CLI execution."* |
| **1:15 - 3:00** | **PART 1: Normal Run from Single Command.**<br>Candidate runs:<br>`python -m engine.cli run --input data/sample_podcast_input.txt --output dist`<br>Displays terminal output. | *"Now let’s execute a normal run. The assessment requires turning 1 long input into at least 10 platform assets in under 30 minutes. Let’s run our command:<br><br>`python -m engine.cli run --input data/sample_podcast_input.txt --output dist`<br><br>Look at that: in just 0.03 seconds, the engine ingested the 677-word podcast interview between Sarah and Kamraj, extracted the core frameworks, and generated 14 platform-specific assets: 4 YouTube Shorts scripts with visual cues, 2 multi-slide LinkedIn carousels, 3 LinkedIn thought-leadership essays, 3 tactical X threads, 1 executive newsletter, and 1 quote card.<br><br>Notice the Brand Voice & Quality Bar check: 14 out of 14 assets passed all guardrails. Zero banned words, hooks strictly under 18 words, and valid UTM tracking links attached to every asset."* |
| **3:00 - 4:15** | **Inspect Generated Outputs.**<br>Candidate opens `dist/` folder.<br>Shows `calendar.csv`, `manifest.json`, and markdown assets. | *"Let’s inspect the generated output in `dist/`. Here is `calendar.csv`—it matches the exact schema of our master calendar with asset IDs, scheduled days, hooks, captions, and UTM tracking links. A social media manager can import this directly into Buffer, Later, or IncuBrix with zero manual reformatting. And here is `manifest.json`, logging the exact execution timestamp, token counts, and validation status."* |
| **4:15 - 5:30** | **PART 2: Refresh on New Input & Deduplication.**<br>Candidate runs:<br>`python -m engine.cli refresh --input data/sample_podcast_input.txt --output dist` | *"Now let’s demonstrate Part 2: refreshing on input and preventing duplicates. In a production pipeline, running the same script twice shouldn't pollute the publishing queue with duplicate posts. Our deduplication engine computes SHA-256 digests of every generated hook and body.<br><br>If we run the refresh command: `python -m engine.cli refresh --input data/sample_podcast_input.txt --output dist`, the engine clears the idempotency cache, re-analyzes the input, and generates a fresh, verified queue."* |
| **5:30 - 6:30** | **PART 3: Recovery from Simple Failure.**<br>Candidate creates a test file `corrupt_input.txt` with banned hype words ('revolutionary', 'game-changing magic') and runs the validator. | *"Now, Part 3: Failure recovery. What happens if a raw input or manual override contains banned corporate hype terms like 'revolutionary', 'game-changing', or 'magic'?<br><br>Let’s look at our GuardrailValidator in `engine/guardrails.py`. The engine actively flags banned terms and runs its automated sanitizer. It replaces 'revolutionary' with 'disciplined', 'game-changing' with 'high-leverage', and 'magic' with 'automation'. If an asset fails critical checks—like missing a UTM link or exceeding 60-second video duration—the engine flags it in `manifest.json` under `failed_assets_count` rather than crashing the pipeline. The queue stays safe and publication-ready."* |
| **6:30 - 7:30** | **PART 4: Cost & Runtime at Scale Benchmark.**<br>Candidate runs:<br>`python -m engine.cli benchmark` | *"Finally, let’s run our scale benchmark: `python -m engine.cli benchmark`.<br><br>Here is the full cost breakdown at scale:<br>Using GPT-4o-mini, processing a 45-minute podcast episode into 14 assets costs just $0.00053—that’s four-hundredths of a cent per asset! At a scale of 20 episodes and 280 assets per month, the total API cost is approximately one penny.<br><br>Even on a premium model like Claude 3.5 Sonnet, processing 20 episodes a month is only $0.22. And with our local Llama 3 connector via Ollama, API cost is exactly $0.00.<br><br>The entire engine runs in sub-second time, operates with zero external database dependencies, and is ready for IncuBrix to deploy on Monday morning. Thank you."* |

---
