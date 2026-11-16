---
name: anime-multi-horizon-radar
description: Multi-horizon data engine for @animefandom0_0. Ingests Daily (24h), Weekly (7d), and Monthly (30d) anime engagement signals, ranks moments for alternate-day releases (Group A Edit Rankings vs Group C Micro-Moments), and interfaces with reverse stream APIs and lossless HLS clippers.
---

# Anime Multi-Horizon Trend Radar & Reverse Stream Harvesting Engine

Master operational specification for [@animefandom0_0](https://www.youtube.com/@animefandom0_0) to automate alternate-day viral production runs.

## 1. Alternate-Day Release Blueprint
Publishing daily at **7:30 PM IST (14:00 UTC)** strictly alternating between two formats:
- **Day 1 (Group A - Edit Ranking / Sakuga Compilations):**
  - High-energy 10-15s causal climax battle cutdowns.
  - Bass-heavy narrative foley, impact HUD countdown stack.
  - Targets high shares, saves, and debate in comments (*"Who had the coldest aura?"*).
- **Day 2 (Group C - Micro-Moments / Accidental Rizz / Reality Checks):**
  - Centered uncropped 16:9 native video (`y=656 to 1264`) with 1080×200 flush brand header card (`y=456`).
  - Animated 5-genre wallpaper parallax (`zoompan` 1.0 to 1.05 without `-loop 1`).
  - Forensic Earshot audio design (dynamic sidechain ducking `-15dB` + deadpan punchline mute).
  - Targets high APV (>95%) and immediate second loops.

---

## 2. Multi-Horizon Comparative Scoring Formula
The engine evaluates candidates across three time horizons:
1. **Daily Horizon (24h):** Airing episode velocity and immediate search spikes ($V_{24h}$).
2. **Weekly Horizon (7d):** Episodic consistency, weekly karma, and top compilation views ($P_{7d}$).
3. **Monthly Horizon (30d):** Evergreen franchise authority and MAL/AniList baseline score ($S_{30d}$).

$$\text{Final Score} = (w_1 \cdot V_{24h}) + (w_2 \cdot P_{7d}) + (w_3 \cdot S_{30d}) + \text{GenreBonus} - \text{SaturationPenalty}$$

- **For Group C:** $w_1 = 0.50, w_2 = 0.35, w_3 = 0.15$ + 20 Romance/Comedy/Slice-of-Life Bonus.
- **For Group A:** $w_1 = 0.45, w_2 = 0.40, w_3 = 0.15$ + 20 Action/Fantasy/Sakuga Bonus.

---

## 3. Reverse Stream API & Clipping Pipeline
To source pristine 1080p clips without downloading full 500MB episode files:
1. **Endpoint Resolution:** Query anime streaming APIs (Consumet / HiAnime / AnimePahe extractors) to obtain the decrypted `.m3u8` master manifest.
2. **Lossless HLS Seek & Cut:** Execute FFmpeg with stream seek:
   ```bash
   ffmpeg -ss [start] -i [m3u8_url] -t [duration] -c:v libx264 -preset ultrafast -crf 18 -c:a aac input/raw_clip.mp4
   ```
3. **Zero-Latency Fallback:** Use `scripts/harvester/anime_stream_harvester.py` with `yt-dlp` `--download-sections` to pull only the exact 12-18 second timecode.

---

## 4. Execution Workflow
1. **Run Comparator:**
   ```bash
   python scripts/radar/multi_horizon_comparator.py [GROUP_A | GROUP_C]
   ```
2. **Harvest Winning Clip:**
   ```bash
   python scripts/harvester/anime_stream_harvester.py
   ```
3. **Render Master & Gatekeeper QA:**
   ```bash
   python scripts/render_animated_bg_short.py
   python scripts/qc/gatekeeper.py
   ```
4. **Schedule Release:**
   Deploy `scripts/scheduler/youtube_scheduler.py` to schedule upload on YouTube Data API v3.
