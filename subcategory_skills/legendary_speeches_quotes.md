---
sub_category_id: legendary_speeches_quotes
sub_category_name: LEGENDARY SPEECHES & QUOTES
niche: whole_anime
focus: "Chills & Goosebumps Philosophy Monologues"
audio_track: public/audio/stems/speeches_quotes_bed.mp3
audio_source: "Samuel Kim - Erwin's Charge Epic Orchestral Version"
audio_bg_volume: 0.11
compositor: src/remotion/AnimeShort.tsx
cue_sheet: cue_sheet_legendary_speeches_quotes.json
---

# Sub-Category Skill: `legendary_speeches_quotes` ("LEGENDARY SPEECHES & QUOTES")

> **MANDATORY FOR AI PIPELINE:** This skill defines the production rules, multi-platform search queries, 5-clip escalation ladder, Remotion compositing, Earshot broadcast audio mastering, and automated description credit formatting for **LEGENDARY SPEECHES & QUOTES**.

---

## 1. Core Production Rules
1. **Header & Composition Props (`AnimeShort`):**
   - `titleHeader`: `"Anime Speeches That"`
   - `subjectHeader`: `"GIVE YOU ABSOLUTE CHILLS"`
   - `versionTag`: `"(Goosebumps Edition)"`
   - `subCategoryId`: `"legendary_speeches_quotes"`
   - `subCategoryName`: `"LEGENDARY SPEECHES & QUOTES"`
   - `globalAudioPath`: `"public/audio/stems/speeches_quotes_bed.mp3"`
2. **Escalating Narrative Arc:**
   - **Arc Formula:** Silent despair of army/protagonist -> Unshakable voice rises above fear -> Thundering war cry or philosophical revelation.
   - Each clip strictly escalates from **Rank 5 [Level 1]** to **Rank 1 [Level 5]** (the pinnacle climax).
   - Rank 1 features a mysterious locked badge (`[ 🔒 LOCKED ? ]`) on the left ladder until its reveal.
3. **Audio Architecture (Earshot Standard):**
   - Uses **Samuel Kim - Erwin's Charge Epic Orchestral Version** mixed at `volume: 0.11` ducked by `-14.0 dB` under character Japanese voice lines and screams.
   - Mastered to YouTube Shorts broadcast standards: **`-14.0 LUFS ± 1.0`**, True Peak `≤ -1.5 dBTP`.
4. **Mandatory Credit Attribution in Description:**
   - Requires Creator / Studio Credit: **YES (Studio & Official Attribution)**
   - Automatically populates the video description with author handles, source URLs, anime titles, studios, and legal fair-use disclaimers.

---

## 2. Multi-Platform Sourcing Queries

- **YouTube Shorts (`yt-dlp` reverse-engineered search):**
  - `"give you absolute chills clips 1080p #shorts"`
  - `"anime speeches that give you absolute chills anime"`
  - `"best anime legendary speeches quotes moments 60fps"`
- **TikTok & Instagram Reels (Reverse-Engineered Tags):**
  - `#animeedit #animetrend #legendary_speeches_quotes #sakuga #animefyp`
- **Reddit JSON API (`/r/AnimeEdits`, `/r/sakuga`, `/r/anime`):**
  - `"site:v.redd.it legendary speeches quotes"`
- **SakugaBooru REST API (`/post.json`):**
  - `tags=fighting order:score limit=15`

### Universal Negative Filters (Instant Disqualification):
- Low quality (<720p / 480p rips), screen recordings with battery icons, facecam reactions, watermarks covering the center action, and foreign sub clashing.

---

## 3. Verified 5-Clip Benchmark Ladder (Rank 5 -> Rank 1)

| Rank | Level | Anime & Scene | Studio / Creator | Story (Cause -> Payoff -> Reaction) | Trim (`ss` / `t`) | Impact Frame Offset | Kinetic Punchline Text |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **5** | Level 1 | Naruto Shippuden - Madara Uchiha's Reality Quote | Studio Pierrot | 'Wake up to reality! Nothing ever goes as planned in this accursed world.' | `0.0s / 4.5s` | `50` | `WAKE UP TO REALITY` |
| **4** | Level 2 | Demon Slayer: Mugen Train - Rengoku's Mother Promise | ufotable | 'Set your heart ablaze. Go beyond your limits.' Flame breathing aura rises. | `0.0s / 5.2s` | `75` | `SET YOUR HEART ABLAZE` |
| **3** | Level 3 | Fate/Zero - Rider's King of Heroes Banquet | ufotable | Iskandar summons Ionian Hetairoi desert reality marble with a laugh. | `0.0s / 5.8s` | `95` | `ARMY OF THE KING` |
| **2** | Level 4 | Naruto Shippuden - Pain's Cycle of Hatred | Studio Pierrot | Pain hovers over Konoha: 'Feel pain, contemplate pain, accept pain, know pain.' | `0.0s / 6.5s` | `120` | `FEEL PAIN SHINRA TENSEI` |
| **1** | Level 5 | Attack on Titan - Commander Erwin Smith's Final Charge | Wit Studio | 'My soldiers rage! My soldiers scream! My soldiers FIGHT!' Green flares pierce smoke. | `0.0s / 8.0s` | `145` | `MY SOLDIERS RAGE` |

---

## 4. Automated Description & Attribution Template

```text
🏆 LEGENDARY SPEECHES & QUOTES — Chills & Goosebumps Philosophy Monologues
Which anime took the #1 spot? Drop your personal ranking in the comments! 👇🔥

══════════════════════════════════════════
🎬 FEATURED CLIPS & CREATOR CREDITS:
══════════════════════════════════════════
[Level 1] Rank 5: Naruto Shippuden - Madara Uchiha's Reality Quote • Credit: Studio Pierrot
[Level 2] Rank 4: Demon Slayer: Mugen Train - Rengoku's Mother Promise • Credit: ufotable
[Level 3] Rank 3: Fate/Zero - Rider's King of Heroes Banquet • Credit: ufotable
[Level 4] Rank 2: Naruto Shippuden - Pain's Cycle of Hatred • Credit: Studio Pierrot
[Level 5] Rank 1: Attack on Titan - Commander Erwin Smith's Final Charge • Credit: Wit Studio

══════════════════════════════════════════
🎵 MUSIC & AUDIO CREDITS:
══════════════════════════════════════════
• Audio Bed: Samuel Kim - Erwin's Charge Epic Orchestral Version

══════════════════════════════════════════
⚖️ COPYRIGHT & FAIR USE DISCLAIMER:
══════════════════════════════════════════
All footages, audio, edits, and characters used in this video belong to their respective anime studios, animators, and content creators.
This video is a transformative commentary and ranking compilation created under Fair Use guidelines (Section 107 of the Copyright Act 1976).
Full credit is proudly given to the talented creators, editors, and studios credited above.

#shorts #anime #legendary_speeches_quotes #animerecommendations #sakuga
```

---

## 5. Render, Mastering & Automated QA Commands

1. **Remotion 30 FPS Composition:**
   ```bash
   npx remotion render src/remotion/index.ts AnimeShort output/legendary_speeches_quotes_raw.mp4 --props=cue_sheet_legendary_speeches_quotes.json --overwrite
   ```
2. **EBU R128 Loudness Normalization (`-14.0 LUFS`):**
   ```bash
   ffmpeg -y -i output/legendary_speeches_quotes_raw.mp4 -af "loudnorm=I=-14.0:TP=-1.5:LRA=11:linear=true" -c:v copy -c:a aac -b:a 320k output/legendary_speeches_quotes_mastered.mp4
   ```
3. **Frame-by-Frame QA Contact Sheet (Zero Black Frames Guard):**
   ```bash
   ffmpeg -y -i output/legendary_speeches_quotes_mastered.mp4 -vf "fps=1,scale=260:-1,tile=6x7" -frames:v 1 -q:v 3 output/legendary_speeches_quotes_qa_sheet.jpg
   ```
