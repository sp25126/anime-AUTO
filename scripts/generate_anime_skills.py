"""
Auto-generate subcategory skills based on master_anime_registry.json
for the 2 Core Niches:
1. Ranking Edits & Moments (10 subcategories)
2. Aesthetic Anime Moments (10 subcategories)
"""

import os
import json

WORKSPACE = os.path.dirname(os.path.dirname(__file__))
REGISTRY_PATH = os.path.join(WORKSPACE, "src", "pipeline", "master_anime_registry.json")
SKILLS_DIR = os.path.join(WORKSPACE, "subcategory_skills")
os.makedirs(SKILLS_DIR, exist_ok=True)

def generate_all_skills():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        registry = json.load(f)

    subcategories = registry.get("subcategories", {})
    niches = registry.get("core_niches", {})

    for sub_id, data in subcategories.items():
        niche_key = data.get("niche")
        niche_info = niches.get(niche_key, {})
        composition = niche_info.get("composition", "RankingShort")

        skill_content = f"""---
name: {sub_id}
description: Reusable production skill for {data.get('name')} in {niche_info.get('name', 'Anime Edits')}.
format: {composition}
niche: {niche_key}
---

# 🎬 Production Skill: {data.get('name')}

## 1. Niche & Positioning
* **Core Niche:** {niche_info.get('name')}
* **Target Remotion Composition:** `{composition}`
* **Target Duration:** {niche_info.get('pacing', '30-45s')} @ 30 FPS
* **Franchise Scope:** {data.get('franchise_isolation', 'Open / Multi-anime')}

## 2. Visual Rules & Typography
"""
        if composition == "RankingShort":
            skill_content += f"""* **Top Pinned Title:**
  * Line 1: `"{data.get('title_line1')}"` (White Impact, 78px)
  * Line 2: `"{data.get('title_line2')}"` (Accent word: `{data.get('accent_word')}` colored `{data.get('accent_color')}`)
* **Left Sidebar:** 5-to-1 rank countdown stack. Gold (#1), Orange (#2), Red (#3), Silver (#4), Yellow (#5).
* **Landscape to Portrait Conversion:**
  * Uses **Blur-Clone Background**: Scale 2.2x, Gaussian blur 45px, brightness 0.65, sat 0.8.
  * Foreground: Centered 16:9 with drop shadow `0 0 50px rgba(0,0,0,0.85)`.
* **Bottom Commentary:** Reaction punchline in Neon Green (`#39FF14`) (e.g. "TS AHH 🙏", "PEAK FICTION 👑").
* **Credit Tag:** Mandatory `CC:@creator` in Cyan (`#00F0FF`).
"""
        else:
            skill_content += f"""* **Visual Mode:** Clean full bleed or centered anime moment with **Painterly Anime Art Background**.
* **Background Theme:** `{data.get('background_theme', 'warm-sunset')}`
* **Audio Vibe:** `{data.get('audio_vibe', 'lofi-ambient')}` (No voiceover, music bed only).
* **Captions:** Minimal floating kinetic subtitles in `{data.get('captions_color', '#FF69B4')}`.
* **Watermark:** Minimal channel tag at bottom center.
"""

        skill_content += f"""
## 3. Recommended Search Queries
"""
        for q in data.get("search_queries", []):
            skill_content += f"* `{q}`\n"

        skill_file = os.path.join(SKILLS_DIR, f"{sub_id}.md")
        with open(skill_file, "w", encoding="utf-8") as sf:
            sf.write(skill_content)
        print(f"Generated skill: {sub_id}.md")

    print(f"\n[Done] Successfully generated all {len(subcategories)} subcategory skills!")

if __name__ == "__main__":
    generate_all_skills()
