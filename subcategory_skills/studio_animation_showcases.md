---
sub_category_id: studio_animation_showcases
sub_category_name: STUDIO SHOWCASE (MAPPA VS UFOTABLE)
niche: whole_anime
focus: "Studio Wars: Trademark Aesthetics & Sakuga Styles"
audio_track: public/audio/stems/studio_showcase_bed.mp3
audio_source: "Tommee Profitt - In The End (Epic Orchestral Hybrid)"
audio_bg_volume: 0.13
compositor: src/remotion/AnimeShort.tsx
cue_sheet: cue_sheet_studio_animation_showcases.json
---

# Sub-Category Skill: `studio_animation_showcases` ("STUDIO SHOWCASE (MAPPA VS UFOTABLE)")

> **MANDATORY FOR AI PIPELINE:** This skill defines the production rules, multi-platform search queries, 5-clip escalation ladder, Remotion compositing, Earshot broadcast audio mastering, and automated description credit formatting for **STUDIO SHOWCASE (MAPPA VS UFOTABLE)**.

---

## 1. Core Production Rules
1. **Header & Composition Props (`AnimeShort`):**
   - `titleHeader`: `"Which Studio Rules Anime?"`
   - `subjectHeader`: `"MAPPA VS UFOTABLE VS WIT"`
   - `versionTag`: `"(Studio Showcase)"`
   - `subCategoryId`: `"studio_animation_showcases"`
   - `subCategoryName`: `"STUDIO SHOWCASE (MAPPA VS UFOTABLE)"`
   - `globalAudioPath`: `"public/audio/stems/studio_showcase_bed.mp3"`
2. **Escalating Narrative Arc:**
   - **Arc Formula:** Trademark studio lighting / framing -> Iconic action kinematics -> Fandom score comparison.
   - Each clip strictly escalates from **Rank 5 [Level 1]** to **Rank 1 [Level 5]** (the pinnacle climax).
   - Rank 1 features a mysterious locked badge (`[ 🔒 LOCKED ? ]`) on the left ladder until its reveal.
3. **Audio Architecture (Earshot Standard):**
   - Uses **Tommee Profitt - In The End (Epic Orchestral Hybrid)** mixed at `volume: 0.13` ducked by `-14.0 dB` under character Japanese voice lines and screams.
   - Mastered to YouTube Shorts broadcast standards: **`-14.0 LUFS ± 1.0`**, True Peak `≤ -1.5 dBTP`.
4. **Mandatory Credit Attribution in Description:**
   - Requires Creator / Studio Credit: **YES (Mandatory Creator Attribution)**
   - Automatically populates the video description with author handles, source URLs, anime titles, studios, and legal fair-use disclaimers.

---

## 2. Multi-Platform Sourcing Queries

- **YouTube Shorts (`yt-dlp` reverse-engineered search):**
  - `"mappa vs ufotable vs wit clips 1080p #shorts"`
  - `"which studio rules anime? mappa vs ufotable vs wit anime"`
  - `"best anime studio animation showcases moments 60fps"`
- **TikTok & Instagram Reels (Reverse-Engineered Tags):**
  - `#animeedit #animetrend #studio_animation_showcases #sakuga #animefyp`
- **Reddit JSON API (`/r/AnimeEdits`, `/r/sakuga`, `/r/anime`):**
  - `"site:v.redd.it studio animation showcases"`
- **SakugaBooru REST API (`/post.json`):**
  - `tags=fighting order:score limit=15`

### Universal Negative Filters (Instant Disqualification):
- Low quality (<720p / 480p rips), screen recordings with battery icons, facecam reactions, watermarks covering the center action, and foreign sub clashing.

---

## 3. Verified 5-Clip Benchmark Ladder (Rank 5 -> Rank 1)

| Rank | Level | Anime & Scene | Studio / Creator | Story (Cause -> Payoff -> Reaction) | Trim (`ss` / `t`) | Impact Frame Offset | Kinetic Punchline Text |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **5** | Level 1 | Kyoto Animation - Violet Evergarden Parasol Water Jump | Kyoto Animation | Violet steps across water lilies in golden sunlight, peak photographic reflection. | `0.0s / 4.5s` | `50` | `KYOTO HYPER-REALISM` |
| **4** | Level 2 | Studio Bones - My Hero Academia All Might vs All For One | Studio Bones | United States of Smash corkscrews clouds with pure hand-drawn kinetic ink. | `0.0s / 5.2s` | `75` | `BONES EMOTIONAL IMPACT` |
| **3** | Level 3 | Wit Studio - Attack on Titan Levi vs Beast Titan | Wit Studio | Arifumi Imai's 3D background tracking through giant forest trees. | `0.0s / 5.8s` | `95` | `WIT 3D MANEUVER SAKUGA` |
| **2** | Level 4 | MAPPA - Jujutsu Kaisen S2 Sukuna vs Mahoraga | MAPPA | Monochrome destruction and relentless speed in modern Shibuya rubble. | `0.0s / 6.5s` | `120` | `MAPPA UNFILTERED CHAOS` |
| **1** | Level 5 | ufotable - Demon Slayer Tengen vs Gyutaro Climax | ufotable | Nozomu Abe's volumetric fire and sparks illuminate dark red entertainment district. | `0.0s / 8.0s` | `145` | `UFOTABLE DIGITAL SAKUGA` |

---

## 4. Automated Description & Attribution Template

```text
🏆 STUDIO SHOWCASE (MAPPA VS UFOTABLE) — Studio Wars: Trademark Aesthetics & Sakuga Styles
Which anime took the #1 spot? Drop your personal ranking in the comments! 👇🔥

══════════════════════════════════════════
🎬 FEATURED CLIPS & CREATOR CREDITS:
══════════════════════════════════════════
[Level 1] Rank 5: Kyoto Animation - Violet Evergarden Parasol Water Jump • Credit: Kyoto Animation
[Level 2] Rank 4: Studio Bones - My Hero Academia All Might vs All For One • Credit: Studio Bones
[Level 3] Rank 3: Wit Studio - Attack on Titan Levi vs Beast Titan • Credit: Wit Studio
[Level 4] Rank 2: MAPPA - Jujutsu Kaisen S2 Sukuna vs Mahoraga • Credit: MAPPA
[Level 5] Rank 1: ufotable - Demon Slayer Tengen vs Gyutaro Climax • Credit: ufotable

══════════════════════════════════════════
🎵 MUSIC & AUDIO CREDITS:
══════════════════════════════════════════
• Audio Bed: Tommee Profitt - In The End (Epic Orchestral Hybrid)

══════════════════════════════════════════
⚖️ COPYRIGHT & FAIR USE DISCLAIMER:
══════════════════════════════════════════
All footages, audio, edits, and characters used in this video belong to their respective anime studios, animators, and content creators.
This video is a transformative commentary and ranking compilation created under Fair Use guidelines (Section 107 of the Copyright Act 1976).
Full credit is proudly given to the talented creators, editors, and studios credited above.

#shorts #anime #studio_animation_showcases #animerecommendations #sakuga
```

---

## 5. Render, Mastering & Automated QA Commands

1. **Remotion 30 FPS Composition:**
   ```bash
   npx remotion render src/remotion/index.ts AnimeShort output/studio_animation_showcases_raw.mp4 --props=cue_sheet_studio_animation_showcases.json --overwrite
   ```
2. **EBU R128 Loudness Normalization (`-14.0 LUFS`):**
   ```bash
   ffmpeg -y -i output/studio_animation_showcases_raw.mp4 -af "loudnorm=I=-14.0:TP=-1.5:LRA=11:linear=true" -c:v copy -c:a aac -b:a 320k output/studio_animation_showcases_mastered.mp4
   ```
3. **Frame-by-Frame QA Contact Sheet (Zero Black Frames Guard):**
   ```bash
   ffmpeg -y -i output/studio_animation_showcases_mastered.mp4 -vf "fps=1,scale=260:-1,tile=6x7" -frames:v 1 -q:v 3 output/studio_animation_showcases_qa_sheet.jpg
   ```
