---
sub_category_id: mind_game_tactical_battles
sub_category_name: 200 IQ TACTICAL BATTLES
niche: whole_anime
focus: "Brute Force Meant Nothing (Death Note / Geass)"
audio_track: public/audio/stems/mind_games_bed.mp3
audio_source: "Yoshihisa Hirano - Low of Solipsism (Death Note Remaster)"
audio_bg_volume: 0.12
compositor: src/remotion/AnimeShort.tsx
cue_sheet: cue_sheet_mind_game_tactical_battles.json
---

# Sub-Category Skill: `mind_game_tactical_battles` ("200 IQ TACTICAL BATTLES")

> **MANDATORY FOR AI PIPELINE:** This skill defines the production rules, multi-platform search queries, 5-clip escalation ladder, Remotion compositing, Earshot broadcast audio mastering, and automated description credit formatting for **200 IQ TACTICAL BATTLES**.

---

## 1. Core Production Rules
1. **Header & Composition Props (`AnimeShort`):**
   - `titleHeader`: `"Anime Battles Where"`
   - `subjectHeader`: `"BRUTE FORCE MEANT NOTHING"`
   - `versionTag`: `"(200 IQ Outplays)"`
   - `subCategoryId`: `"mind_game_tactical_battles"`
   - `subCategoryName`: `"200 IQ TACTICAL BATTLES"`
   - `globalAudioPath`: `"public/audio/stems/mind_games_bed.mp3"`
2. **Escalating Narrative Arc:**
   - **Arc Formula:** Complex psychological web -> Fast analytical deduction cuts -> Inescapable checkmate trap sprung.
   - Each clip strictly escalates from **Rank 5 [Level 1]** to **Rank 1 [Level 5]** (the pinnacle climax).
   - Rank 1 features a mysterious locked badge (`[ 🔒 LOCKED ? ]`) on the left ladder until its reveal.
3. **Audio Architecture (Earshot Standard):**
   - Uses **Yoshihisa Hirano - Low of Solipsism (Death Note Remaster)** mixed at `volume: 0.12` ducked by `-14.0 dB` under character Japanese voice lines and screams.
   - Mastered to YouTube Shorts broadcast standards: **`-14.0 LUFS ± 1.0`**, True Peak `≤ -1.5 dBTP`.
4. **Mandatory Credit Attribution in Description:**
   - Requires Creator / Studio Credit: **YES (Studio & Official Attribution)**
   - Automatically populates the video description with author handles, source URLs, anime titles, studios, and legal fair-use disclaimers.

---

## 2. Multi-Platform Sourcing Queries

- **YouTube Shorts (`yt-dlp` reverse-engineered search):**
  - `"brute force meant nothing clips 1080p #shorts"`
  - `"anime battles where brute force meant nothing anime"`
  - `"best anime mind game tactical battles moments 60fps"`
- **TikTok & Instagram Reels (Reverse-Engineered Tags):**
  - `#animeedit #animetrend #mind_game_tactical_battles #sakuga #animefyp`
- **Reddit JSON API (`/r/AnimeEdits`, `/r/sakuga`, `/r/anime`):**
  - `"site:v.redd.it mind game tactical battles"`
- **SakugaBooru REST API (`/post.json`):**
  - `tags=fighting order:score limit=15`

### Universal Negative Filters (Instant Disqualification):
- Low quality (<720p / 480p rips), screen recordings with battery icons, facecam reactions, watermarks covering the center action, and foreign sub clashing.

---

## 3. Verified 5-Clip Benchmark Ladder (Rank 5 -> Rank 1)

| Rank | Level | Anime & Scene | Studio / Creator | Story (Cause -> Payoff -> Reaction) | Trim (`ss` / `t`) | Impact Frame Offset | Kinetic Punchline Text |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **5** | Level 1 | Classroom of the Elite - Ayanokoji Rooftop Trap | Lerche | Ryuen thinks he cornered Ayanokoji -> Ayanokoji reveals everyone was just a tool. | `0.0s / 4.5s` | `50` | `TOOL MONOLOGUE` |
| **4** | Level 2 | No Game No Life - Sora's Materialization Shiritori | Madhouse | Sora removes atmospheric oxygen and nuclear mantle to checkmate Jibril. | `0.0s / 5.0s` | `70` | `SHIRITORI OUTPLAY` |
| **3** | Level 3 | Code Geass - Lelouch Zero Requiem Broadcast | Sunrise | Schneizel's fleet surrounded as Damocles shield calculation backfires. | `0.0s / 5.5s` | `90` | `CHECKMATE SCHNEIZEL` |
| **2** | Level 4 | JoJo: Battle Tendency - Joseph Joestar 'Next You'll Say' | David Production | Joseph predicts Esidisi's exact sentence and ties string trap around volcano spikes. | `0.0s / 6.2s` | `110` | `YOUR NEXT LINE IS` |
| **1** | Level 5 | Death Note - Light Yagami Potato Chip & Lind L. Tailor | Madhouse | L uses Lind L. Tailor television broadcast to pinpoint Kira's exact Kanto district. | `0.0s / 7.5s` | `135` | `L PINPOINTS KIRA` |

---

## 4. Automated Description & Attribution Template

```text
🏆 200 IQ TACTICAL BATTLES — Brute Force Meant Nothing (Death Note / Geass)
Which anime took the #1 spot? Drop your personal ranking in the comments! 👇🔥

══════════════════════════════════════════
🎬 FEATURED CLIPS & CREATOR CREDITS:
══════════════════════════════════════════
[Level 1] Rank 5: Classroom of the Elite - Ayanokoji Rooftop Trap • Credit: Lerche
[Level 2] Rank 4: No Game No Life - Sora's Materialization Shiritori • Credit: Madhouse
[Level 3] Rank 3: Code Geass - Lelouch Zero Requiem Broadcast • Credit: Sunrise
[Level 4] Rank 2: JoJo: Battle Tendency - Joseph Joestar 'Next You'll Say' • Credit: David Production
[Level 5] Rank 1: Death Note - Light Yagami Potato Chip & Lind L. Tailor • Credit: Madhouse

══════════════════════════════════════════
🎵 MUSIC & AUDIO CREDITS:
══════════════════════════════════════════
• Audio Bed: Yoshihisa Hirano - Low of Solipsism (Death Note Remaster)

══════════════════════════════════════════
⚖️ COPYRIGHT & FAIR USE DISCLAIMER:
══════════════════════════════════════════
All footages, audio, edits, and characters used in this video belong to their respective anime studios, animators, and content creators.
This video is a transformative commentary and ranking compilation created under Fair Use guidelines (Section 107 of the Copyright Act 1976).
Full credit is proudly given to the talented creators, editors, and studios credited above.

#shorts #anime #mind_game_tactical_battles #animerecommendations #sakuga
```

---

## 5. Render, Mastering & Automated QA Commands

1. **Remotion 30 FPS Composition:**
   ```bash
   npx remotion render src/remotion/index.ts AnimeShort output/mind_game_tactical_battles_raw.mp4 --props=cue_sheet_mind_game_tactical_battles.json --overwrite
   ```
2. **EBU R128 Loudness Normalization (`-14.0 LUFS`):**
   ```bash
   ffmpeg -y -i output/mind_game_tactical_battles_raw.mp4 -af "loudnorm=I=-14.0:TP=-1.5:LRA=11:linear=true" -c:v copy -c:a aac -b:a 320k output/mind_game_tactical_battles_mastered.mp4
   ```
3. **Frame-by-Frame QA Contact Sheet (Zero Black Frames Guard):**
   ```bash
   ffmpeg -y -i output/mind_game_tactical_battles_mastered.mp4 -vf "fps=1,scale=260:-1,tile=6x7" -frames:v 1 -q:v 3 output/mind_game_tactical_battles_qa_sheet.jpg
   ```
