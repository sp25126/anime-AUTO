---
sub_category_id: genre_by_year_cross_axis
sub_category_name: GENRE BY YEAR (CROSS-AXIS)
niche: whole_anime
focus: "Best of Single Genre Across Consecutive Years"
audio_track: public/audio/stems/genre_year_bed.mp3
audio_source: "Myth & Roid - VORACITY (Hyper J-Rock Remix)"
audio_bg_volume: 0.14
compositor: src/remotion/AnimeShort.tsx
cue_sheet: cue_sheet_genre_by_year_cross_axis.json
---

# Sub-Category Skill: `genre_by_year_cross_axis` ("GENRE BY YEAR (CROSS-AXIS)")

> **MANDATORY FOR AI PIPELINE:** This skill defines the production rules, multi-platform search queries, 5-clip escalation ladder, Remotion compositing, Earshot broadcast audio mastering, and automated description credit formatting for **GENRE BY YEAR (CROSS-AXIS)**.

---

## 1. Core Production Rules
1. **Header & Composition Props (`AnimeShort`):**
   - `titleHeader`: `"Best Isekai Anime"`
   - `subjectHeader`: `"BY YEAR EVOLUTION"`
   - `versionTag`: `"(2018 - 2024)"`
   - `subCategoryId`: `"genre_by_year_cross_axis"`
   - `subCategoryName`: `"GENRE BY YEAR (CROSS-AXIS)"`
   - `globalAudioPath`: `"public/audio/stems/genre_year_bed.mp3"`
2. **Escalating Narrative Arc:**
   - **Arc Formula:** Annual evolution of genre tropes -> Progression from parody to peak high fantasy -> Definitive annual champion.
   - Each clip strictly escalates from **Rank 5 [Level 1]** to **Rank 1 [Level 5]** (the pinnacle climax).
   - Rank 1 features a mysterious locked badge (`[ 🔒 LOCKED ? ]`) on the left ladder until its reveal.
3. **Audio Architecture (Earshot Standard):**
   - Uses **Myth & Roid - VORACITY (Hyper J-Rock Remix)** mixed at `volume: 0.14` ducked by `-14.0 dB` under character Japanese voice lines and screams.
   - Mastered to YouTube Shorts broadcast standards: **`-14.0 LUFS ± 1.0`**, True Peak `≤ -1.5 dBTP`.
4. **Mandatory Credit Attribution in Description:**
   - Requires Creator / Studio Credit: **YES (Studio & Official Attribution)**
   - Automatically populates the video description with author handles, source URLs, anime titles, studios, and legal fair-use disclaimers.

---

## 2. Multi-Platform Sourcing Queries

- **YouTube Shorts (`yt-dlp` reverse-engineered search):**
  - `"by year evolution clips 1080p #shorts"`
  - `"best isekai anime by year evolution anime"`
  - `"best anime genre by year cross axis moments 60fps"`
- **TikTok & Instagram Reels (Reverse-Engineered Tags):**
  - `#animeedit #animetrend #genre_by_year_cross_axis #sakuga #animefyp`
- **Reddit JSON API (`/r/AnimeEdits`, `/r/sakuga`, `/r/anime`):**
  - `"site:v.redd.it genre by year cross axis"`
- **SakugaBooru REST API (`/post.json`):**
  - `tags=fighting order:score limit=15`

### Universal Negative Filters (Instant Disqualification):
- Low quality (<720p / 480p rips), screen recordings with battery icons, facecam reactions, watermarks covering the center action, and foreign sub clashing.

---

## 3. Verified 5-Clip Benchmark Ladder (Rank 5 -> Rank 1)

| Rank | Level | Anime & Scene | Studio / Creator | Story (Cause -> Payoff -> Reaction) | Trim (`ss` / `t`) | Impact Frame Offset | Kinetic Punchline Text |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **5** | Level 1 | 2018: That Time I Got Reincarnated as a Slime | 8bit | Rimuru devours dragon Veldora -> Magicule aura awakens. | `0.0s / 4.5s` | `50` | `2018 SLIME REVOLUTION` |
| **4** | Level 2 | 2020: Re:Zero Season 2 | White Fox | Subaru confronts Echidna at tea party of greed. | `0.0s / 5.0s` | `70` | `2020 GREED TRIAL` |
| **3** | Level 3 | 2021: Mushoku Tensei: Jobless Reincarnation S1 | Studio Bind | Rudy casts water cannon under Roxy's guidance with filmic camera movement. | `0.0s / 5.5s` | `90` | `2021 PEAK PRODUCTION` |
| **2** | Level 4 | 2022: The Eminence in Shadow | Nexus | Cid atomic blast vaporizes city core with classical music. | `0.0s / 6.2s` | `110` | `2022 CHUNIBYO GOD` |
| **1** | Level 5 | 2024: Mushoku Tensei S2 Part 2 | Studio Bind | Labyrinth hydra battle with sacrificial spell casting. | `0.0s / 7.5s` | `135` | `2024 EMOTIONAL PEAK` |

---

## 4. Automated Description & Attribution Template

```text
🏆 GENRE BY YEAR (CROSS-AXIS) — Best of Single Genre Across Consecutive Years
Which anime took the #1 spot? Drop your personal ranking in the comments! 👇🔥

══════════════════════════════════════════
🎬 FEATURED CLIPS & CREATOR CREDITS:
══════════════════════════════════════════
[Level 1] Rank 5: 2018: That Time I Got Reincarnated as a Slime • Credit: 8bit
[Level 2] Rank 4: 2020: Re:Zero Season 2 • Credit: White Fox
[Level 3] Rank 3: 2021: Mushoku Tensei: Jobless Reincarnation S1 • Credit: Studio Bind
[Level 4] Rank 2: 2022: The Eminence in Shadow • Credit: Nexus
[Level 5] Rank 1: 2024: Mushoku Tensei S2 Part 2 • Credit: Studio Bind

══════════════════════════════════════════
🎵 MUSIC & AUDIO CREDITS:
══════════════════════════════════════════
• Audio Bed: Myth & Roid - VORACITY (Hyper J-Rock Remix)

══════════════════════════════════════════
⚖️ COPYRIGHT & FAIR USE DISCLAIMER:
══════════════════════════════════════════
All footages, audio, edits, and characters used in this video belong to their respective anime studios, animators, and content creators.
This video is a transformative commentary and ranking compilation created under Fair Use guidelines (Section 107 of the Copyright Act 1976).
Full credit is proudly given to the talented creators, editors, and studios credited above.

#shorts #anime #genre_by_year_cross_axis #animerecommendations #sakuga
```

---

## 5. Render, Mastering & Automated QA Commands

1. **Remotion 30 FPS Composition:**
   ```bash
   npx remotion render src/remotion/index.ts AnimeShort output/genre_by_year_cross_axis_raw.mp4 --props=cue_sheet_genre_by_year_cross_axis.json --overwrite
   ```
2. **EBU R128 Loudness Normalization (`-14.0 LUFS`):**
   ```bash
   ffmpeg -y -i output/genre_by_year_cross_axis_raw.mp4 -af "loudnorm=I=-14.0:TP=-1.5:LRA=11:linear=true" -c:v copy -c:a aac -b:a 320k output/genre_by_year_cross_axis_mastered.mp4
   ```
3. **Frame-by-Frame QA Contact Sheet (Zero Black Frames Guard):**
   ```bash
   ffmpeg -y -i output/genre_by_year_cross_axis_mastered.mp4 -vf "fps=1,scale=260:-1,tile=6x7" -frames:v 1 -q:v 3 output/genre_by_year_cross_axis_qa_sheet.jpg
   ```
