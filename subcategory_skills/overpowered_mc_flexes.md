---
sub_category_id: overpowered_mc_flexes
sub_category_name: OVERPOWERED MC FLEXES
niche: whole_anime
focus: "Zero Damage Taken & Instant Traumatizing Counters"
audio_track: public/audio/stems/op_mc_bed.mp3
audio_source: "Kute - AVOID ME (Bass Boosted Flex Edit)"
audio_bg_volume: 0.13
compositor: src/remotion/AnimeShort.tsx
cue_sheet: cue_sheet_overpowered_mc_flexes.json
---

# Sub-Category Skill: `overpowered_mc_flexes` ("OVERPOWERED MC FLEXES")

> **MANDATORY FOR AI PIPELINE:** This skill defines the production rules, multi-platform search queries, 5-clip escalation ladder, Remotion compositing, Earshot broadcast audio mastering, and automated description credit formatting for **OVERPOWERED MC FLEXES**.

---

## 1. Core Production Rules
1. **Header & Composition Props (`AnimeShort`):**
   - `titleHeader`: `"When The MC Stops"`
   - `subjectHeader`: `"HOLDING BACK THEIR POWER"`
   - `versionTag`: `"(Absolute Domination)"`
   - `subCategoryId`: `"overpowered_mc_flexes"`
   - `subCategoryName`: `"OVERPOWERED MC FLEXES"`
   - `globalAudioPath`: `"public/audio/stems/op_mc_bed.mp3"`
2. **Escalating Narrative Arc:**
   - **Arc Formula:** Enemy boasts and unleashes supreme ultimate spell -> MC stands motionless -> Nonchalant counter wipes enemy existence.
   - Each clip strictly escalates from **Rank 5 [Level 1]** to **Rank 1 [Level 5]** (the pinnacle climax).
   - Rank 1 features a mysterious locked badge (`[ 🔒 LOCKED ? ]`) on the left ladder until its reveal.
3. **Audio Architecture (Earshot Standard):**
   - Uses **Kute - AVOID ME (Bass Boosted Flex Edit)** mixed at `volume: 0.13` ducked by `-14.0 dB` under character Japanese voice lines and screams.
   - Mastered to YouTube Shorts broadcast standards: **`-14.0 LUFS ± 1.0`**, True Peak `≤ -1.5 dBTP`.
4. **Mandatory Credit Attribution in Description:**
   - Requires Creator / Studio Credit: **YES (Studio & Official Attribution)**
   - Automatically populates the video description with author handles, source URLs, anime titles, studios, and legal fair-use disclaimers.

---

## 2. Multi-Platform Sourcing Queries

- **YouTube Shorts (`yt-dlp` reverse-engineered search):**
  - `"holding back their power clips 1080p #shorts"`
  - `"when the mc stops holding back their power anime"`
  - `"best anime overpowered mc flexes moments 60fps"`
- **TikTok & Instagram Reels (Reverse-Engineered Tags):**
  - `#animeedit #animetrend #overpowered_mc_flexes #sakuga #animefyp`
- **Reddit JSON API (`/r/AnimeEdits`, `/r/sakuga`, `/r/anime`):**
  - `"site:v.redd.it overpowered mc flexes"`
- **SakugaBooru REST API (`/post.json`):**
  - `tags=fighting order:score limit=15`

### Universal Negative Filters (Instant Disqualification):
- Low quality (<720p / 480p rips), screen recordings with battery icons, facecam reactions, watermarks covering the center action, and foreign sub clashing.

---

## 3. Verified 5-Clip Benchmark Ladder (Rank 5 -> Rank 1)

| Rank | Level | Anime & Scene | Studio / Creator | Story (Cause -> Payoff -> Reaction) | Trim (`ss` / `t`) | Impact Frame Offset | Kinetic Punchline Text |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **5** | Level 1 | Overlord - Ainz Ooal Gown 'Grasp Heart' | Madhouse | Knight charges in full plate armor -> Ainz casts Grasp Heart -> Knight collapses instantly. | `0.0s / 4.0s` | `45` | `INSTANT DEATH` |
| **4** | Level 2 | The Eminence in Shadow - Cid 'I Am Atomic' | Nexus | Cid whispers 'I... Am... Atomic' -> Shockwave expands in deep violet light. | `0.0s / 5.0s` | `65` | `I AM ATOMIC` |
| **3** | Level 3 | Solo Leveling - Sung Jinwoo 'Arise' | A-1 Pictures | Red Knight Igris falls -> Jinwoo commands shadows: 'Arise' -> Blue flames erupt. | `0.0s / 5.5s` | `90` | `ARISE COMMAND` |
| **2** | Level 4 | The Misfit of Demon King Academy - Anos Heartbeat | SILVER LINK. | Anos kills god of time with his heartbeat: 'Did you think killing me would make me die?' | `0.0s / 6.5s` | `115` | `HEARTBEAT KILL` |
| **1** | Level 5 | One Punch Man - Saitama 'Serious Punch' | Madhouse | Boros unleashes star-collapsing cannon -> Saitama delivers Serious Punch -> Atmosphere parts. | `0.0s / 8.0s` | `140` | `SERIOUS SERIES` |

---

## 4. Automated Description & Attribution Template

```text
🏆 OVERPOWERED MC FLEXES — Zero Damage Taken & Instant Traumatizing Counters
Which anime took the #1 spot? Drop your personal ranking in the comments! 👇🔥

══════════════════════════════════════════
🎬 FEATURED CLIPS & CREATOR CREDITS:
══════════════════════════════════════════
[Level 1] Rank 5: Overlord - Ainz Ooal Gown 'Grasp Heart' • Credit: Madhouse
[Level 2] Rank 4: The Eminence in Shadow - Cid 'I Am Atomic' • Credit: Nexus
[Level 3] Rank 3: Solo Leveling - Sung Jinwoo 'Arise' • Credit: A-1 Pictures
[Level 4] Rank 2: The Misfit of Demon King Academy - Anos Heartbeat • Credit: SILVER LINK.
[Level 5] Rank 1: One Punch Man - Saitama 'Serious Punch' • Credit: Madhouse

══════════════════════════════════════════
🎵 MUSIC & AUDIO CREDITS:
══════════════════════════════════════════
• Audio Bed: Kute - AVOID ME (Bass Boosted Flex Edit)

══════════════════════════════════════════
⚖️ COPYRIGHT & FAIR USE DISCLAIMER:
══════════════════════════════════════════
All footages, audio, edits, and characters used in this video belong to their respective anime studios, animators, and content creators.
This video is a transformative commentary and ranking compilation created under Fair Use guidelines (Section 107 of the Copyright Act 1976).
Full credit is proudly given to the talented creators, editors, and studios credited above.

#shorts #anime #overpowered_mc_flexes #animerecommendations #sakuga
```

---

## 5. Render, Mastering & Automated QA Commands

1. **Remotion 30 FPS Composition:**
   ```bash
   npx remotion render src/remotion/index.ts AnimeShort output/overpowered_mc_flexes_raw.mp4 --props=cue_sheet_overpowered_mc_flexes.json --overwrite
   ```
2. **EBU R128 Loudness Normalization (`-14.0 LUFS`):**
   ```bash
   ffmpeg -y -i output/overpowered_mc_flexes_raw.mp4 -af "loudnorm=I=-14.0:TP=-1.5:LRA=11:linear=true" -c:v copy -c:a aac -b:a 320k output/overpowered_mc_flexes_mastered.mp4
   ```
3. **Frame-by-Frame QA Contact Sheet (Zero Black Frames Guard):**
   ```bash
   ffmpeg -y -i output/overpowered_mc_flexes_mastered.mp4 -vf "fps=1,scale=260:-1,tile=6x7" -frames:v 1 -q:v 3 output/overpowered_mc_flexes_qa_sheet.jpg
   ```
