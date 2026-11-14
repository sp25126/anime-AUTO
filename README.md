# 🎬 Anime-AUTO: Autonomous Anime Compilation & Shorts Engine

An end-to-end, headless production engine that automatically harvests, evaluates, composites, and masters viral anime shorts (1080x1920 @ 30 FPS) across **20 curated sub-categories** with full multi-platform creator attribution and fair-use compliance.

[![TypeScript](https://img.shields.io/badge/TypeScript-5.4-blue.svg)](https://www.typescriptlang.org/)
[![Remotion](https://img.shields.io/badge/Remotion-4.0-red.svg)](https://www.remotion.dev/)
[![Python](https://img.shields.io/badge/Python-3.11-green.svg)](https://www.python.org/)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-7.1-orange.svg)](https://ffmpeg.org/)
[![EBU R128](https://img.shields.io/badge/Audio-EBU%20R128%20(-14%20LUFS)-purple.svg)]()

---

## 🚀 Key Features

* **Whole Anime Niche (20 Sub-Categories):** From trending velocity edits, sakuga compilations, and legendary openings to coldest antagonist moments and 200 IQ mind games.
* **Reverse-Engineered Multi-Platform Ingestion:**
  * **YouTube Shorts & Videos:** `yt-dlp` query engine with resolution ($\ge 1080\text{p}$) and duration ($4\text{s} - 60\text{s}$) validation.
  * **TikTok & Instagram Reels:** Tag-based discovery preserving author handles, original URLs, and sound metadata.
  * **Reddit Direct JSON API:** Crawls `/r/AnimeEdits`, `/r/sakuga`, `/r/anime` and muxes `v.redd.it` direct streams.
  * **SakugaBooru REST API:** Pristine, watermark-free, 60 FPS keyframe cuts with animator and source tags.
  * **Jikan API v4 (MyAnimeList):** Canonical scores, English/Japanese titles, release years, and studio credits.
* **Automated Attribution & Credits Engine:** Formats full YouTube descriptions crediting every editor (`@creator`), anime title, studio name, music track, and legal Section 107 Fair Use disclaimers.
* **Signal-Processing Apex Calibration:**
  * Laplacian motion jerk $d(\text{Var})/dt$ at 6 FPS.
  * Scene-cut guard (`gt(scene, 0.40)`) preventing false triggers on cut boundaries.
  * Acoustic transient spike detection for bass drops, screams, and sword clashes.
  * Frame-accurate freeze-frame baking with micro-silence gating.
* **Remotion Neo-Tokyo Visual Engine:** 1080x1920 9:16 vertical layout featuring dynamic top headers, left rank ladder (Level 1 $\rightarrow$ Level 5 with mystery locked Rank 1 badge), ambient blurred background, and animated kinetic typography.
* **Forensic Earshot Audio Pipeline:** Dynamic $-14\text{ dB}$ sidechain ducking under dialogue, punchline bed muting, and two-pass EBU R128 mastering (`-14.0 LUFS ± 1.0`, True Peak $\le -1.5\text{ dBTP}$).

---

## 🗂️ The 20 Curated Anime Sub-Categories

| # | Sub-Category ID | Name | Focus | Specification |
| :---: | :--- | :--- | :--- | :--- |
| **1** | `trending_anime_edits` | Trending Viral Anime Edits | Velocity, Twixtor flow & phonk transitions | [Skill](subcategory_skills/trending_anime_edits.md) |
| **2** | `best_anime_by_genre` | Best Anime By Genre | Top 5 champions across Shonen, Seinen, Isekai, Romance | [Skill](subcategory_skills/best_anime_by_genre.md) |
| **3** | `anime_by_year_all_time` | Anime By Year (2015-2025) | Landmark show of each calendar year | [Skill](subcategory_skills/anime_by_year_all_time.md) |
| **4** | `underrated_hidden_gems` | Underrated Hidden Gems | High score ($\ge 8.1$) slept-on masterpieces | [Skill](subcategory_skills/underrated_hidden_gems.md) |
| **5** | `genre_by_year_cross_axis` | Genre By Year Evolution | Best of single genre across years (e.g. Isekai) | [Skill](subcategory_skills/genre_by_year_cross_axis.md) |
| **6** | `anime_edits_sakuga_compilation` | Peak Sakuga Animation | Fluid keyframe combat & smear frame sakuga | [Skill](subcategory_skills/anime_edits_sakuga_compilation.md) |
| **7** | `best_upcoming_anime_hype` | Best Upcoming Anime | Most anticipated seasonal premieres & trailer cuts | [Skill](subcategory_skills/best_upcoming_anime_hype.md) |
| **8** | `best_anime_openings_ost` | Best Anime Openings & OST | 10/10 legendary opening song drops & chorus peaks | [Skill](subcategory_skills/best_anime_openings_ost.md) |
| **9** | `iconic_transformations` | Iconic Transformations | Internet-breaking God-form awakenings | [Skill](subcategory_skills/iconic_transformations.md) |
| **10** | `coldest_antagonist_moments` | Coldest Antagonist Moments | Infinite negative aura & humiliation of heroes | [Skill](subcategory_skills/coldest_antagonist_moments.md) |
| **11** | `overpowered_mc_flexes` | Overpowered MC Flexes | Zero-damage taken & instant nonchalant counters | [Skill](subcategory_skills/overpowered_mc_flexes.md) |
| **12** | `mind_game_tactical_battles` | 200 IQ Tactical Battles | Psychological mind games where brute force meant nothing | [Skill](subcategory_skills/mind_game_tactical_battles.md) |
| **13** | `saddest_backstories_tearjerkers`| Saddest Tearjerker Moments | Tragic pasts & emotional damage | [Skill](subcategory_skills/saddest_backstories_tearjerkers.md) |
| **14** | `insane_plot_twists` | Insane Plot Twists | Traitor reveals & narrative shockers | [Skill](subcategory_skills/insane_plot_twists.md) |
| **15** | `best_anime_duos_rivalries` | Legendary Duos & Rivalries | Generational brotherhood & clashing wills | [Skill](subcategory_skills/best_anime_duos_rivalries.md) |
| **16** | `studio_animation_showcases` | Studio Showcase | MAPPA vs. ufotable vs. Wit Studio vs. Bones | [Skill](subcategory_skills/studio_animation_showcases.md) |
| **17** | `first_season_peak_vs_continuous`| Season 1 Peak vs Continual Climb| Trajectory: One-season wonders vs compounding mastery | [Skill](subcategory_skills/first_season_peak_vs_continuous.md) |
| **18** | `brutal_dark_psychological` | Brutal Dark Psychological | Grimdark & high-tension horror anime | [Skill](subcategory_skills/brutal_dark_psychological.md) |
| **19** | `most_satisfying_beatdowns` | Most Satisfying Beatdowns | Arrogant bullies getting humbled & instant karma | [Skill](subcategory_skills/most_satisfying_beatdowns.md) |
| **20** | `legendary_speeches_quotes` | Legendary Speeches & Quotes | Chills & goosebumps philosophy monologues | [Skill](subcategory_skills/legendary_speeches_quotes.md) |

---

## 🛠️ Project Structure

```
anime-compilation-engine/
├── scripts/
│   ├── anime_harvester.py       # Multi-platform reverse-engineered harvester (YT, TikTok, IG, Reddit, SakugaBooru)
│   ├── jikan_client.py          # Jikan API v4 & AniList metadata client with local disk cache
│   ├── description_builder.py   # Formats compliant descriptions with timestamped credits & fair use
│   ├── anime_evaluator.py       # Laplacian motion jerk & audio transient apex detector
│   ├── master_and_qa.py         # Two-pass EBU R128 loudness mastering & 30fps QA frame check
│   └── generate_anime_skills.py # Automated subcategory skills generator
├── src/
│   ├── pipeline/
│   │   ├── master_anime_registry.json # Comprehensive 20 sub-category schema & queries
│   │   └── AnimeGraph.ts              # Round-robin state cycler & context locking
│   └── remotion/
│       ├── AnimeShort.tsx       # Neo-Tokyo 1080x1920 30fps vertical composition
│       ├── Root.tsx             # Remotion composition root & duration calculator
│       └── index.ts             # Entry point
├── subcategory_skills/          # 20 Reusable production-grade subcategory skills (.md)
├── used_anime_registry.json     # Strict deduplication state file
├── package.json
└── tsconfig.json
```

---

## ⚡ Quick Start

### 1. Requirements
* Node.js $\ge 18$
* Python $\ge 3.10$ with `requests`, `numpy`, and `yt-dlp`
* FFmpeg $\ge 6.0$ & FFprobe on system PATH

### 2. Build TypeScript
```bash
npm install
npm run build
```

### 3. Cycle Next Sub-Category
```bash
npx ts-node src/pipeline/AnimeGraph.ts
```

### 4. Harvest Candidates
```bash
python scripts/anime_harvester.py --subcategory trending_anime_edits --count 5
```

### 5. Render & Master
```bash
npx remotion render src/remotion/index.ts AnimeShort output/short_raw.mp4 --overwrite
python scripts/master_and_qa.py output/short_raw.mp4 output/short_mastered.mp4
```

---

## ⚖️ Legal & Fair Use
This engine is built to enforce transformative content creation under Section 107 of the U.S. Copyright Act 1976. All harvested media automatically credits original creators, production studios, and music producers in every generated video description.
