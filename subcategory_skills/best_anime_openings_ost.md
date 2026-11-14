---
sub_category_id: best_anime_openings_ost
sub_category_name: BEST ANIME OPENINGS & OST
niche: whole_anime
focus: "10/10 Legendary Song Drops & Chorus Peaks"
audio_track: public/audio/stems/openings_ost_bed.mp3
audio_source: "TK from Ling Tosite Sigure - Unravel / Kenshi Yonezu - Kick Back"
audio_bg_volume: 0.2
compositor: src/remotion/AnimeShort.tsx
cue_sheet: cue_sheet_best_anime_openings_ost.json
---

# Sub-Category Skill: `best_anime_openings_ost` ("BEST ANIME OPENINGS & OST")

> **MANDATORY FOR AI PIPELINE:** This skill defines the production rules, multi-platform search queries, 5-clip escalation ladder, Remotion compositing, Earshot broadcast audio mastering, and automated description credit formatting for **BEST ANIME OPENINGS & OST**.

---

## 1. Core Production Rules
1. **Header & Composition Props (`AnimeShort`):**
   - `titleHeader`: `"Anime Openings That"`
   - `subjectHeader`: `"ARE AN ABSOLUTE 10/10"`
   - `versionTag`: `"(Never Skip)"`
   - `subCategoryId`: `"best_anime_openings_ost"`
   - `subCategoryName`: `"BEST ANIME OPENINGS & OST"`
   - `globalAudioPath`: `"public/audio/stems/openings_ost_bed.mp3"`
2. **Escalating Narrative Arc:**
   - **Arc Formula:** Iconic opening guitar riff / vocal intro -> Visual countdown -> Chorus drop with bass slam.
   - Each clip strictly escalates from **Rank 5 [Level 1]** to **Rank 1 [Level 5]** (the pinnacle climax).
   - Rank 1 features a mysterious locked badge (`[ 🔒 LOCKED ? ]`) on the left ladder until its reveal.
3. **Audio Architecture (Earshot Standard):**
   - Uses **TK from Ling Tosite Sigure - Unravel / Kenshi Yonezu - Kick Back** mixed at `volume: 0.2` ducked by `-14.0 dB` under character Japanese voice lines and screams.
   - Mastered to YouTube Shorts broadcast standards: **`-14.0 LUFS ± 1.0`**, True Peak `≤ -1.5 dBTP`.
4. **Mandatory Credit Attribution in Description:**
   - Requires Creator / Studio Credit: **YES (Mandatory Creator Attribution)**
   - Automatically populates the video description with author handles, source URLs, anime titles, studios, and legal fair-use disclaimers.

---

## 2. Multi-Platform Sourcing Queries

- **YouTube Shorts (`yt-dlp` reverse-engineered search):**
  - `"are an absolute 10/10 clips 1080p #shorts"`
  - `"anime openings that are an absolute 10/10 anime"`
  - `"best anime best anime openings ost moments 60fps"`
- **TikTok & Instagram Reels (Reverse-Engineered Tags):**
  - `#animeedit #animetrend #best_anime_openings_ost #sakuga #animefyp`
- **Reddit JSON API (`/r/AnimeEdits`, `/r/sakuga`, `/r/anime`):**
  - `"site:v.redd.it best anime openings ost"`
- **SakugaBooru REST API (`/post.json`):**
  - `tags=fighting order:score limit=15`

### Universal Negative Filters (Instant Disqualification):
- Low quality (<720p / 480p rips), screen recordings with battery icons, facecam reactions, watermarks covering the center action, and foreign sub clashing.

---

## 3. Verified 5-Clip Benchmark Ladder (Rank 5 -> Rank 1)

| Rank | Level | Anime & Scene | Studio / Creator | Story (Cause -> Payoff -> Reaction) | Trim (`ss` / `t`) | Impact Frame Offset | Kinetic Punchline Text |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **5** | Level 1 | Chainsaw Man: KICK BACK (Kenshi Yonezu) | MAPPA / SME | Denji pulls ripcord on chorus drop as devil hunters sprint through cinematic homage frames. | `0.0s / 4.5s` | `55` | `NEVER SKIP OP` |
| **4** | Level 2 | Jujutsu Kaisen S2: SPECIALZ (King Gnu) | MAPPA / Ariola | Red neon Shibuya streets pulse in time with bassline walkout. | `0.0s / 5.0s` | `70` | `YOU ARE MY SPECIAL` |
| **3** | Level 3 | Attack on Titan: The Rumbling (SiM) | MAPPA / Pony Canyon | Eren walks forward as Colossal Titans break through wall in metal breakdown. | `0.0s / 5.5s` | `90` | `WALL TITANS MARCH` |
| **2** | Level 4 | Demon Slayer: Gurenge (LiSA) | ufotable / SACRA MUSIC | Water breathing kata transitions into flame sword slash on chorus blast. | `0.0s / 6.2s` | `110` | `ICONIC J-ROCK CHORUS` |
| **1** | Level 5 | Tokyo Ghoul: Unravel (TK) | Studio Pierrot / Sony | Kaneki's eye turns red under shattered glass sky, unforgettable falsetto scream. | `0.0s / 7.5s` | `135` | `HISTORIC ANIME ANTHEM` |

---

## 4. Automated Description & Attribution Template

```text
🏆 BEST ANIME OPENINGS & OST — 10/10 Legendary Song Drops & Chorus Peaks
Which anime took the #1 spot? Drop your personal ranking in the comments! 👇🔥

══════════════════════════════════════════
🎬 FEATURED CLIPS & CREATOR CREDITS:
══════════════════════════════════════════
[Level 1] Rank 5: Chainsaw Man: KICK BACK (Kenshi Yonezu) • Credit: MAPPA / SME
[Level 2] Rank 4: Jujutsu Kaisen S2: SPECIALZ (King Gnu) • Credit: MAPPA / Ariola
[Level 3] Rank 3: Attack on Titan: The Rumbling (SiM) • Credit: MAPPA / Pony Canyon
[Level 4] Rank 2: Demon Slayer: Gurenge (LiSA) • Credit: ufotable / SACRA MUSIC
[Level 5] Rank 1: Tokyo Ghoul: Unravel (TK) • Credit: Studio Pierrot / Sony

══════════════════════════════════════════
🎵 MUSIC & AUDIO CREDITS:
══════════════════════════════════════════
• Audio Bed: TK from Ling Tosite Sigure - Unravel / Kenshi Yonezu - Kick Back

══════════════════════════════════════════
⚖️ COPYRIGHT & FAIR USE DISCLAIMER:
══════════════════════════════════════════
All footages, audio, edits, and characters used in this video belong to their respective anime studios, animators, and content creators.
This video is a transformative commentary and ranking compilation created under Fair Use guidelines (Section 107 of the Copyright Act 1976).
Full credit is proudly given to the talented creators, editors, and studios credited above.

#shorts #anime #best_anime_openings_ost #animerecommendations #sakuga
```

---

## 5. Render, Mastering & Automated QA Commands

1. **Remotion 30 FPS Composition:**
   ```bash
   npx remotion render src/remotion/index.ts AnimeShort output/best_anime_openings_ost_raw.mp4 --props=cue_sheet_best_anime_openings_ost.json --overwrite
   ```
2. **EBU R128 Loudness Normalization (`-14.0 LUFS`):**
   ```bash
   ffmpeg -y -i output/best_anime_openings_ost_raw.mp4 -af "loudnorm=I=-14.0:TP=-1.5:LRA=11:linear=true" -c:v copy -c:a aac -b:a 320k output/best_anime_openings_ost_mastered.mp4
   ```
3. **Frame-by-Frame QA Contact Sheet (Zero Black Frames Guard):**
   ```bash
   ffmpeg -y -i output/best_anime_openings_ost_mastered.mp4 -vf "fps=1,scale=260:-1,tile=6x7" -frames:v 1 -q:v 3 output/best_anime_openings_ost_qa_sheet.jpg
   ```
