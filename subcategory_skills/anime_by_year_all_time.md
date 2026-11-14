---
sub_category_id: anime_by_year_all_time
sub_category_name: ANIME BY YEAR (GOLDEN ERA)
niche: whole_anime
focus: "Landmark Show of Each Year (2015-2025)"
audio_track: public/audio/stems/anime_by_year_bed.mp3
audio_source: "Kavinsky & The Weeknd - Odd Look (Cyberpunk Riser Edit)"
audio_bg_volume: 0.13
compositor: src/remotion/AnimeShort.tsx
cue_sheet: cue_sheet_anime_by_year_all_time.json
---

# Sub-Category Skill: `anime_by_year_all_time` ("ANIME BY YEAR (GOLDEN ERA)")

> **MANDATORY FOR AI PIPELINE:** This skill defines the production rules, multi-platform search queries, 5-clip escalation ladder, Remotion compositing, Earshot broadcast audio mastering, and automated description credit formatting for **ANIME BY YEAR (GOLDEN ERA)**.

---

## 1. Core Production Rules
1. **Header & Composition Props (`AnimeShort`):**
   - `titleHeader`: `"The #1 Anime From"`
   - `subjectHeader`: `"EVERY SINGLE YEAR"`
   - `versionTag`: `"(2015 - 2025)"`
   - `subCategoryId`: `"anime_by_year_all_time"`
   - `subCategoryName`: `"ANIME BY YEAR (GOLDEN ERA)"`
   - `globalAudioPath`: `"public/audio/stems/anime_by_year_bed.mp3"`
2. **Escalating Narrative Arc:**
   - **Arc Formula:** Chronological year jump -> Visual signature representing that calendar year -> Landmark cultural impact.
   - Each clip strictly escalates from **Rank 5 [Level 1]** to **Rank 1 [Level 5]** (the pinnacle climax).
   - Rank 1 features a mysterious locked badge (`[ 🔒 LOCKED ? ]`) on the left ladder until its reveal.
3. **Audio Architecture (Earshot Standard):**
   - Uses **Kavinsky & The Weeknd - Odd Look (Cyberpunk Riser Edit)** mixed at `volume: 0.13` ducked by `-14.0 dB` under character Japanese voice lines and screams.
   - Mastered to YouTube Shorts broadcast standards: **`-14.0 LUFS ± 1.0`**, True Peak `≤ -1.5 dBTP`.
4. **Mandatory Credit Attribution in Description:**
   - Requires Creator / Studio Credit: **YES (Studio & Official Attribution)**
   - Automatically populates the video description with author handles, source URLs, anime titles, studios, and legal fair-use disclaimers.

---

## 2. Multi-Platform Sourcing Queries

- **YouTube Shorts (`yt-dlp` reverse-engineered search):**
  - `"every single year clips 1080p #shorts"`
  - `"the #1 anime from every single year anime"`
  - `"best anime anime by year all time moments 60fps"`
- **TikTok & Instagram Reels (Reverse-Engineered Tags):**
  - `#animeedit #animetrend #anime_by_year_all_time #sakuga #animefyp`
- **Reddit JSON API (`/r/AnimeEdits`, `/r/sakuga`, `/r/anime`):**
  - `"site:v.redd.it anime by year all time"`
- **SakugaBooru REST API (`/post.json`):**
  - `tags=fighting order:score limit=15`

### Universal Negative Filters (Instant Disqualification):
- Low quality (<720p / 480p rips), screen recordings with battery icons, facecam reactions, watermarks covering the center action, and foreign sub clashing.

---

## 3. Verified 5-Clip Benchmark Ladder (Rank 5 -> Rank 1)

| Rank | Level | Anime & Scene | Studio / Creator | Story (Cause -> Payoff -> Reaction) | Trim (`ss` / `t`) | Impact Frame Offset | Kinetic Punchline Text |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **5** | Level 1 | 2016: Re:Zero / Your Name | White Fox / CoMix Wave | Rem's confession under sunset / Comet split across Tokyo night sky. | `0.0s / 4.0s` | `45` | `2016 LANDMARK` |
| **4** | Level 2 | 2019: Demon Slayer (Ep 19 Hinokami) | ufotable | Tanjiro ignites Hinokami Kagura dance -> Nezuko Blood Demon Art triggers. | `0.0s / 5.0s` | `65` | `2019 INTERNET BREAK` |
| **3** | Level 3 | 2021: Attack on Titan Final Season | MAPPA | Eren transforms underneath Willy Tybur's stage in Liberio. | `0.0s / 5.5s` | `85` | `2021 DECLARATION OF WAR` |
| **2** | Level 4 | 2023: Jujutsu Kaisen S2 (Shibuya Arc) | MAPPA | Sukuna Malevolent Shrine domain expansion unfolds over Shibuya. | `0.5s / 6.2s` | `110` | `2023 SHIBUYA INCIDENT` |
| **1** | Level 5 | 2024: Frieren: Beyond Journey's End | Madhouse | Frieren reveals mana restriction against Aura the Guillotine -> 'Aura, kill yourself'. | `0.0s / 7.8s` | `130` | `2024 SUPREME MASTERPIECE` |

---

## 4. Automated Description & Attribution Template

```text
🏆 ANIME BY YEAR (GOLDEN ERA) — Landmark Show of Each Year (2015-2025)
Which anime took the #1 spot? Drop your personal ranking in the comments! 👇🔥

══════════════════════════════════════════
🎬 FEATURED CLIPS & CREATOR CREDITS:
══════════════════════════════════════════
[Level 1] Rank 5: 2016: Re:Zero / Your Name • Credit: White Fox / CoMix Wave
[Level 2] Rank 4: 2019: Demon Slayer (Ep 19 Hinokami) • Credit: ufotable
[Level 3] Rank 3: 2021: Attack on Titan Final Season • Credit: MAPPA
[Level 4] Rank 2: 2023: Jujutsu Kaisen S2 (Shibuya Arc) • Credit: MAPPA
[Level 5] Rank 1: 2024: Frieren: Beyond Journey's End • Credit: Madhouse

══════════════════════════════════════════
🎵 MUSIC & AUDIO CREDITS:
══════════════════════════════════════════
• Audio Bed: Kavinsky & The Weeknd - Odd Look (Cyberpunk Riser Edit)

══════════════════════════════════════════
⚖️ COPYRIGHT & FAIR USE DISCLAIMER:
══════════════════════════════════════════
All footages, audio, edits, and characters used in this video belong to their respective anime studios, animators, and content creators.
This video is a transformative commentary and ranking compilation created under Fair Use guidelines (Section 107 of the Copyright Act 1976).
Full credit is proudly given to the talented creators, editors, and studios credited above.

#shorts #anime #anime_by_year_all_time #animerecommendations #sakuga
```

---

## 5. Render, Mastering & Automated QA Commands

1. **Remotion 30 FPS Composition:**
   ```bash
   npx remotion render src/remotion/index.ts AnimeShort output/anime_by_year_all_time_raw.mp4 --props=cue_sheet_anime_by_year_all_time.json --overwrite
   ```
2. **EBU R128 Loudness Normalization (`-14.0 LUFS`):**
   ```bash
   ffmpeg -y -i output/anime_by_year_all_time_raw.mp4 -af "loudnorm=I=-14.0:TP=-1.5:LRA=11:linear=true" -c:v copy -c:a aac -b:a 320k output/anime_by_year_all_time_mastered.mp4
   ```
3. **Frame-by-Frame QA Contact Sheet (Zero Black Frames Guard):**
   ```bash
   ffmpeg -y -i output/anime_by_year_all_time_mastered.mp4 -vf "fps=1,scale=260:-1,tile=6x7" -frames:v 1 -q:v 3 output/anime_by_year_all_time_qa_sheet.jpg
   ```
