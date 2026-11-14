---
sub_category_id: best_anime_by_genre
sub_category_name: BEST ANIME IN EVERY GENRE
niche: whole_anime
focus: "Definitive Champions Across Shonen, Seinen, Romance, Isekai & Dark Fantasy"
audio_track: public/audio/stems/best_anime_by_genre_bed.mp3
audio_source: "Hiroyuki Sawano - YouSeeBIGGIRL/T:T (Epic Hybrid Remaster)"
audio_bg_volume: 0.14
compositor: src/remotion/AnimeShort.tsx
cue_sheet: cue_sheet_best_anime_by_genre.json
---

# Sub-Category Skill: `best_anime_by_genre` ("BEST ANIME IN EVERY GENRE")

> **MANDATORY FOR AI PIPELINE:** This skill defines the production rules, multi-platform search queries, 5-clip escalation ladder, Remotion compositing, Earshot broadcast audio mastering, and automated description credit formatting for **BEST ANIME IN EVERY GENRE**.

---

## 1. Core Production Rules
1. **Header & Composition Props (`AnimeShort`):**
   - `titleHeader`: `"Ranking The Best Anime"`
   - `subjectHeader`: `"IN EVERY SINGLE GENRE"`
   - `versionTag`: `"(Ultimate Tier)"`
   - `subCategoryId`: `"best_anime_by_genre"`
   - `subCategoryName`: `"BEST ANIME IN EVERY GENRE"`
   - `globalAudioPath`: `"public/audio/stems/best_anime_by_genre_bed.mp3"`
2. **Escalating Narrative Arc:**
   - **Arc Formula:** Establishment of the genre titan -> Signature emotional or combat climax -> Crowd-agreed supremacy badge.
   - Each clip strictly escalates from **Rank 5 [Level 1]** to **Rank 1 [Level 5]** (the pinnacle climax).
   - Rank 1 features a mysterious locked badge (`[ 🔒 LOCKED ? ]`) on the left ladder until its reveal.
3. **Audio Architecture (Earshot Standard):**
   - Uses **Hiroyuki Sawano - YouSeeBIGGIRL/T:T (Epic Hybrid Remaster)** mixed at `volume: 0.14` ducked by `-14.0 dB` under character Japanese voice lines and screams.
   - Mastered to YouTube Shorts broadcast standards: **`-14.0 LUFS ± 1.0`**, True Peak `≤ -1.5 dBTP`.
4. **Mandatory Credit Attribution in Description:**
   - Requires Creator / Studio Credit: **YES (Studio & Official Attribution)**
   - Automatically populates the video description with author handles, source URLs, anime titles, studios, and legal fair-use disclaimers.

---

## 2. Multi-Platform Sourcing Queries

- **YouTube Shorts (`yt-dlp` reverse-engineered search):**
  - `"in every single genre clips 1080p #shorts"`
  - `"ranking the best anime in every single genre anime"`
  - `"best anime best anime by genre moments 60fps"`
- **TikTok & Instagram Reels (Reverse-Engineered Tags):**
  - `#animeedit #animetrend #best_anime_by_genre #sakuga #animefyp`
- **Reddit JSON API (`/r/AnimeEdits`, `/r/sakuga`, `/r/anime`):**
  - `"site:v.redd.it best anime by genre"`
- **SakugaBooru REST API (`/post.json`):**
  - `tags=fighting order:score limit=15`

### Universal Negative Filters (Instant Disqualification):
- Low quality (<720p / 480p rips), screen recordings with battery icons, facecam reactions, watermarks covering the center action, and foreign sub clashing.

---

## 3. Verified 5-Clip Benchmark Ladder (Rank 5 -> Rank 1)

| Rank | Level | Anime & Scene | Studio / Creator | Story (Cause -> Payoff -> Reaction) | Trim (`ss` / `t`) | Impact Frame Offset | Kinetic Punchline Text |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **5** | Level 1 | Romance: Kaguya-sama: Love Is War | A-1 Pictures | Miyuki & Kaguya mind games reach fever pitch -> Dual internal monologues explode with comic fireworks. | `0.0s / 4.2s` | `50` | `PEAK ROM-COM` |
| **4** | Level 2 | Isekai: Re:Zero Season 2 | White Fox | Subaru confronts the Witches of Sin -> Melancholic pledge to defy fate. | `1.0s / 5.0s` | `70` | `DESPAIR TRANSCENDED` |
| **3** | Level 3 | Dark Fantasy: Berserk (1997 / Memorial) | OLM / Studio 4°C | Guts swings Dragonslayer in pouring rain -> Blood-curdling mercenary vow. | `0.5s / 5.5s` | `90` | `STRUGGLER'S PATH` |
| **2** | Level 4 | Seinen: Vinland Saga Season 2 | MAPPA | Thorfinn takes 100 punches without striking back -> 'I have no enemies' declaration. | `0.0s / 6.5s` | `120` | `I HAVE NO ENEMIES` |
| **1** | Level 5 | Shonen: Hunter x Hunter (Chimera Ant) | Madhouse | Gon's final aura transformation in pitch black forest -> Tear falls on Nen explosion. | `0.0s / 8.0s` | `140` | `TRANSCENDENT NEN` |

---

## 4. Automated Description & Attribution Template

```text
🏆 BEST ANIME IN EVERY GENRE — Definitive Champions Across Shonen, Seinen, Romance, Isekai & Dark Fantasy
Which anime took the #1 spot? Drop your personal ranking in the comments! 👇🔥

══════════════════════════════════════════
🎬 FEATURED CLIPS & CREATOR CREDITS:
══════════════════════════════════════════
[Level 1] Rank 5: Romance: Kaguya-sama: Love Is War • Credit: A-1 Pictures
[Level 2] Rank 4: Isekai: Re:Zero Season 2 • Credit: White Fox
[Level 3] Rank 3: Dark Fantasy: Berserk (1997 / Memorial) • Credit: OLM / Studio 4°C
[Level 4] Rank 2: Seinen: Vinland Saga Season 2 • Credit: MAPPA
[Level 5] Rank 1: Shonen: Hunter x Hunter (Chimera Ant) • Credit: Madhouse

══════════════════════════════════════════
🎵 MUSIC & AUDIO CREDITS:
══════════════════════════════════════════
• Audio Bed: Hiroyuki Sawano - YouSeeBIGGIRL/T:T (Epic Hybrid Remaster)

══════════════════════════════════════════
⚖️ COPYRIGHT & FAIR USE DISCLAIMER:
══════════════════════════════════════════
All footages, audio, edits, and characters used in this video belong to their respective anime studios, animators, and content creators.
This video is a transformative commentary and ranking compilation created under Fair Use guidelines (Section 107 of the Copyright Act 1976).
Full credit is proudly given to the talented creators, editors, and studios credited above.

#shorts #anime #best_anime_by_genre #animerecommendations #sakuga
```

---

## 5. Render, Mastering & Automated QA Commands

1. **Remotion 30 FPS Composition:**
   ```bash
   npx remotion render src/remotion/index.ts AnimeShort output/best_anime_by_genre_raw.mp4 --props=cue_sheet_best_anime_by_genre.json --overwrite
   ```
2. **EBU R128 Loudness Normalization (`-14.0 LUFS`):**
   ```bash
   ffmpeg -y -i output/best_anime_by_genre_raw.mp4 -af "loudnorm=I=-14.0:TP=-1.5:LRA=11:linear=true" -c:v copy -c:a aac -b:a 320k output/best_anime_by_genre_mastered.mp4
   ```
3. **Frame-by-Frame QA Contact Sheet (Zero Black Frames Guard):**
   ```bash
   ffmpeg -y -i output/best_anime_by_genre_mastered.mp4 -vf "fps=1,scale=260:-1,tile=6x7" -frames:v 1 -q:v 3 output/best_anime_by_genre_qa_sheet.jpg
   ```
