---
sub_category_id: brutal_dark_psychological
sub_category_name: BRUTAL DARK PSYCHOLOGICAL
niche: whole_anime
focus: "Grimdark & High Tension Masterpieces"
audio_track: public/audio/stems/dark_psychological_bed.mp3
audio_source: "Susumu Hirasawa - Forces / Kevin Penkin - The Rumble of Scientific Triumph"
audio_bg_volume: 0.13
compositor: src/remotion/AnimeShort.tsx
cue_sheet: cue_sheet_brutal_dark_psychological.json
---

# Sub-Category Skill: `brutal_dark_psychological` ("BRUTAL DARK PSYCHOLOGICAL")

> **MANDATORY FOR AI PIPELINE:** This skill defines the production rules, multi-platform search queries, 5-clip escalation ladder, Remotion compositing, Earshot broadcast audio mastering, and automated description credit formatting for **BRUTAL DARK PSYCHOLOGICAL**.

---

## 1. Core Production Rules
1. **Header & Composition Props (`AnimeShort`):**
   - `titleHeader`: `"Dark Anime That Are"`
   - `subjectHeader`: `"NOT FOR THE FAINT OF HEART"`
   - `versionTag`: `"(Psychological Grimdark)"`
   - `subCategoryId`: `"brutal_dark_psychological"`
   - `subCategoryName`: `"BRUTAL DARK PSYCHOLOGICAL"`
   - `globalAudioPath`: `"public/audio/stems/dark_psychological_bed.mp3"`
2. **Escalating Narrative Arc:**
   - **Arc Formula:** False sense of safety -> Unflinching psychological rupture -> Moral abyss where hope dies.
   - Each clip strictly escalates from **Rank 5 [Level 1]** to **Rank 1 [Level 5]** (the pinnacle climax).
   - Rank 1 features a mysterious locked badge (`[ 🔒 LOCKED ? ]`) on the left ladder until its reveal.
3. **Audio Architecture (Earshot Standard):**
   - Uses **Susumu Hirasawa - Forces / Kevin Penkin - The Rumble of Scientific Triumph** mixed at `volume: 0.13` ducked by `-14.0 dB` under character Japanese voice lines and screams.
   - Mastered to YouTube Shorts broadcast standards: **`-14.0 LUFS ± 1.0`**, True Peak `≤ -1.5 dBTP`.
4. **Mandatory Credit Attribution in Description:**
   - Requires Creator / Studio Credit: **YES (Studio & Official Attribution)**
   - Automatically populates the video description with author handles, source URLs, anime titles, studios, and legal fair-use disclaimers.

---

## 2. Multi-Platform Sourcing Queries

- **YouTube Shorts (`yt-dlp` reverse-engineered search):**
  - `"not for the faint of heart clips 1080p #shorts"`
  - `"dark anime that are not for the faint of heart anime"`
  - `"best anime brutal dark psychological moments 60fps"`
- **TikTok & Instagram Reels (Reverse-Engineered Tags):**
  - `#animeedit #animetrend #brutal_dark_psychological #sakuga #animefyp`
- **Reddit JSON API (`/r/AnimeEdits`, `/r/sakuga`, `/r/anime`):**
  - `"site:v.redd.it brutal dark psychological"`
- **SakugaBooru REST API (`/post.json`):**
  - `tags=fighting order:score limit=15`

### Universal Negative Filters (Instant Disqualification):
- Low quality (<720p / 480p rips), screen recordings with battery icons, facecam reactions, watermarks covering the center action, and foreign sub clashing.

---

## 3. Verified 5-Clip Benchmark Ladder (Rank 5 -> Rank 1)

| Rank | Level | Anime & Scene | Studio / Creator | Story (Cause -> Payoff -> Reaction) | Trim (`ss` / `t`) | Impact Frame Offset | Kinetic Punchline Text |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **5** | Level 1 | Neon Genesis Evangelion - Third Impact | Gainax | Shinji screams as Unit-01 hovers above the red LCL ocean of souls. | `0.0s / 4.5s` | `50` | `PSYCHOLOGICAL BREAKDOWN` |
| **4** | Level 2 | Re:Zero - Subaru's Rabbit Death | White Fox | Snow field in Sanctuary turns red as Great Rabbit devours Subaru alive. | `0.0s / 5.0s` | `75` | `TRUE TRAUMA LOOP` |
| **3** | Level 3 | Made in Abyss: Dawn of the Deep Soul | Kinema Citrus | Bondrewd reveals elevator cartridge sacrifice mechanism to Riko. | `0.0s / 5.8s` | `95` | `BONDREWD CARTRIDGES` |
| **2** | Level 4 | Monster - The Red Rose Mansion Mystery | Madhouse | Reading 'The Nameless Monster' picture book inside the secret dark room. | `0.0s / 6.5s` | `120` | `THE NAMELESS MONSTER` |
| **1** | Level 5 | Berserk - The Eclipse | OLM | The Crimson Behelit cries blood as the God Hand descends upon the Band of the Hawk. | `0.0s / 8.0s` | `145` | `THE ECLIPSE SACRIFICE` |

---

## 4. Automated Description & Attribution Template

```text
🏆 BRUTAL DARK PSYCHOLOGICAL — Grimdark & High Tension Masterpieces
Which anime took the #1 spot? Drop your personal ranking in the comments! 👇🔥

══════════════════════════════════════════
🎬 FEATURED CLIPS & CREATOR CREDITS:
══════════════════════════════════════════
[Level 1] Rank 5: Neon Genesis Evangelion - Third Impact • Credit: Gainax
[Level 2] Rank 4: Re:Zero - Subaru's Rabbit Death • Credit: White Fox
[Level 3] Rank 3: Made in Abyss: Dawn of the Deep Soul • Credit: Kinema Citrus
[Level 4] Rank 2: Monster - The Red Rose Mansion Mystery • Credit: Madhouse
[Level 5] Rank 1: Berserk - The Eclipse • Credit: OLM

══════════════════════════════════════════
🎵 MUSIC & AUDIO CREDITS:
══════════════════════════════════════════
• Audio Bed: Susumu Hirasawa - Forces / Kevin Penkin - The Rumble of Scientific Triumph

══════════════════════════════════════════
⚖️ COPYRIGHT & FAIR USE DISCLAIMER:
══════════════════════════════════════════
All footages, audio, edits, and characters used in this video belong to their respective anime studios, animators, and content creators.
This video is a transformative commentary and ranking compilation created under Fair Use guidelines (Section 107 of the Copyright Act 1976).
Full credit is proudly given to the talented creators, editors, and studios credited above.

#shorts #anime #brutal_dark_psychological #animerecommendations #sakuga
```

---

## 5. Render, Mastering & Automated QA Commands

1. **Remotion 30 FPS Composition:**
   ```bash
   npx remotion render src/remotion/index.ts AnimeShort output/brutal_dark_psychological_raw.mp4 --props=cue_sheet_brutal_dark_psychological.json --overwrite
   ```
2. **EBU R128 Loudness Normalization (`-14.0 LUFS`):**
   ```bash
   ffmpeg -y -i output/brutal_dark_psychological_raw.mp4 -af "loudnorm=I=-14.0:TP=-1.5:LRA=11:linear=true" -c:v copy -c:a aac -b:a 320k output/brutal_dark_psychological_mastered.mp4
   ```
3. **Frame-by-Frame QA Contact Sheet (Zero Black Frames Guard):**
   ```bash
   ffmpeg -y -i output/brutal_dark_psychological_mastered.mp4 -vf "fps=1,scale=260:-1,tile=6x7" -frames:v 1 -q:v 3 output/brutal_dark_psychological_qa_sheet.jpg
   ```
