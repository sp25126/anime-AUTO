"""
Dynamic Skill Synthesizer for Anime Compilation Engine.
Synthesizes a production skill file whenever a new viral anime is discovered,
updating master_anime_registry.json automatically.
"""

import os
import sys
import json
import re
from typing import Dict, Any, List

WORKSPACE = os.path.dirname(os.path.dirname(__file__))
REGISTRY_PATH = os.path.join(WORKSPACE, "src", "pipeline", "master_anime_registry.json")
SKILLS_DIR = os.path.join(WORKSPACE, "subcategory_skills")
os.makedirs(SKILLS_DIR, exist_ok=True)

def pick_color(title: str) -> str:
    palette = {
        "jujutsu kaisen": "#FF0000",
        "demon slayer": "#FF8C00",
        "attack on titan": "#00F0FF",
        "one piece": "#FFE600",
        "bleach": "#FF2A85",
        "chainsaw man": "#FF3300",
        "solo leveling": "#00C9FF",
        "naruto": "#FF8C00",
        "dragon ball": "#00E5FF",
        "blue lock": "#0055FF",
        "dandadan": "#39FF14",
        "kaiju no. 8": "#00FF99",
        "sakamoto days": "#FFCC00"
    }
    return palette.get(title.lower(), "#FF0055")

def synthesize_anime_skill(
    anime_title: str,
    trending_reason: str = "High algorithmic search spike on YouTube Shorts",
    notable_characters: List[str] = None
) -> str:
    clean_id = f"ranking_{re.sub(r'[^a-zA-Z0-9]+', '_', anime_title).lower().strip('_')}_edits"
    accent_color = pick_color(anime_title)
    
    # 1. Update master_anime_registry.json if not present
    if os.path.exists(REGISTRY_PATH):
        try:
            with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
                registry = json.load(f)
        except Exception:
            registry = {"subcategories": {}}
    else:
        registry = {"subcategories": {}}

    subcategories = registry.setdefault("subcategories", {})
    if clean_id not in subcategories:
        subcategories[clean_id] = {
            "niche": "ranking_edits_and_moments",
            "name": f"Ranking The Best {anime_title} Edits",
            "category_type": "single_anime_edits",
            "search_queries": [
                f"ranking best {anime_title.lower()} edits shorts",
                f"{anime_title.lower()} viral edits ranking shorts",
                f"best {anime_title.lower()} edits 4k shorts"
            ],
            "title_line1": "RANKING THE BEST",
            "title_line2": f"{anime_title.upper()} EDITS",
            "accent_word": anime_title.upper(),
            "accent_color": accent_color,
            "franchise_isolation": anime_title
        }
        with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
            json.dump(registry, f, indent=2)
        print(f"[Synthesizer] Added '{clean_id}' to master_anime_registry.json")

    # 2. Write the skill markdown file
    skill_file = os.path.join(SKILLS_DIR, f"{clean_id}.md")
    chars_str = ", ".join(notable_characters) if notable_characters else anime_title
    
    content = f"""---
name: {clean_id}
description: Autonomous single-anime isolation skill for Ranking The Best {anime_title} Edits.
format: RankingShort
niche: ranking_edits_and_moments
---

# 🎬 Dynamic Skill: Ranking The Best {anime_title} Edits

## 1. Algorithmic Intelligence
* **Detected Anime:** {anime_title}
* **Trend Trigger:** {trending_reason}
* **Key Entities:** {chars_str}
* **Franchise Scope:** Strictly isolated to **{anime_title}** only.

## 2. Visual Rules & Typography
* **Target Remotion Composition:** `RankingShort`
* **Top Title:**
  * Line 1: `"RANKING THE BEST"`
  * Line 2: `"{anime_title.upper()} EDITS"`
  * Accent Word: `{anime_title.upper()}` (Colored `{accent_color}`)
* **Left Sidebar:** Vertical 5-to-1 rank countdown with view-count reveals.
* **Background Mode:** `blur-clone` (Scale 2.2x, Gaussian blur 45px, desaturated 20%).
* **Credit Policy:** Mandatory on-screen tag `CC: @creator` in Cyan (`#00F0FF`).

## 3. Search Queries
* `ranking best {anime_title.lower()} edits shorts`
* `{anime_title.lower()} viral edits ranking shorts`
* `best {anime_title.lower()} edits 4k shorts`
"""

    with open(skill_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[Synthesizer] Synthesized skill: {clean_id}.md")
    return skill_file

if __name__ == "__main__":
    synthesize_anime_skill("Solo Leveling", "Season 2 hype", ["Sung Jinwoo", "Beru"])
