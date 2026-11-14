"""
Dynamic Sub-Category & Skill Synthesizer.
Allows the pipeline to dynamically create new sub-categories on the fly
matching whatever anime, character, or format is blowing up the algorithms.
Injects directly into:
- subcategory_skills/<id>.md
- src/pipeline/master_anime_registry.json
- current_anime_run_context.json
"""

import os
import sys
import json
import argparse
from typing import Dict, Any

WORKSPACE = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, WORKSPACE)
from scripts.generate_anime_skills import generate_markdown

REGISTRY_PATH = os.path.join(WORKSPACE, "src", "pipeline", "master_anime_registry.json")
SKILLS_DIR = os.path.join(WORKSPACE, "subcategory_skills")
RUN_CONTEXT_PATH = os.path.join(WORKSPACE, "current_anime_run_context.json")

def synthesize_dynamic_subcategory(
    anime_title: str,
    character_focus: str = "Spotlight",
    format_type: str = "AnimeShort"
) -> Dict[str, Any]:
    slug = f"{anime_title.lower().replace(' ', '_')}_{character_focus.lower().replace(' ', '_')}"
    slug = "".join(c for c in slug if c.isalnum() or c == '_').strip('_')
    
    sub_id = f"{slug}_viral"
    sub_name = f"{anime_title.upper()} - {character_focus.upper()}"
    
    spec = {
        "id": sub_id,
        "name": sub_name,
        "focus": f"Dynamic Algorithmic Breakout: {character_focus} in {anime_title}",
        "single_anime_only": True,
        "target_anime": anime_title,
        "format_type": format_type,
        "title": "Ranking The Best",
        "subject": f"{anime_title.upper()} MOMENTS",
        "version": f"({character_focus.title()} Edition)",
        "hook_title": f"The Greatest {character_focus} Moments In {anime_title} 🔥⚡ #shorts #anime",
        "audio_stem": f"public/audio/stems/{slug}_bed.mp3",
        "audio_source": f"Dynamic Phonk Anthem ({anime_title} Sound)",
        "audio_bg_vol": 0.12,
        "story_arc": f"Character {character_focus} introduction -> Escalating aura/speed ramp -> Final apex strike with frame freeze.",
        "requires_creator_credit": True,
        "ranks": [
            ("5", "Level 1", f"{anime_title} - {character_focus} Entrance", "Official Studio", f"{character_focus} steps onto battlefield with sound flare.", "0.0s / 4.5s", "50", "ENTRANCE IMPACT"),
            ("4", "Level 2", f"{anime_title} - {character_focus} Counter", "Official Studio", f"{character_focus} counters enemy assault with fluid parry.", "0.0s / 5.0s", "70", "FLUID PARRY"),
            ("3", "Level 3", f"{anime_title} - {character_focus} Speed Blitz", "Official Studio", f"{character_focus} accelerates into high-speed twixtor dash.", "0.0s / 5.8s", "90", "SPEED BLITZ"),
            ("2", "Level 4", f"{anime_title} - {character_focus} Domain / Power-Up", "Official Studio", f"{character_focus} unleashes ultimate technique.", "0.0s / 6.5s", "115", "ULTIMATE TECH"),
            ("1", "Level 5", f"{anime_title} - {character_focus} Pinnacle Climax", "Official Studio", f"{character_focus} delivers legendary one-shot finisher.", "0.0s / 8.0s", "140", "PINNACLE FINISHER")
        ]
    }
    
    # 1. Write Markdown Skill
    md_content = generate_markdown(spec)
    skill_file = os.path.join(SKILLS_DIR, f"{sub_id}.md")
    with open(skill_file, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"[Synthesizer] Generated dynamic skill file: {skill_file}")
    
    # 2. Inject into master_anime_registry.json
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        registry_data = json.load(f)
        
    registry_entry = {
        "id": sub_id,
        "name": sub_name,
        "focus": spec["focus"],
        "single_anime_only": True,
        "target_anime": anime_title,
        "format_type": format_type,
        "banner_title": spec["title"],
        "banner_subject": spec["subject"],
        "banner_version": spec["version"],
        "hook_title": spec["hook_title"],
        "description_tags": ["#shorts", "#anime", f"#{slug}", "#sakuga", "#viral"],
        "requires_creator_credit": True,
        "audio_track": spec["audio_stem"],
        "audio_genre": "Dynamic High-Energy Phonk / Bass Drop",
        "bpm": 138,
        "harvester": {
            "platforms": ["youtube", "tiktok", "reddit"],
            "primary_queries": [
                f"{anime_title} {character_focus} edit 4k shorts",
                f"{character_focus} {anime_title} viral phonk",
                f"{anime_title} best moments 1080p shorts"
            ],
            "min_duration": 4.0,
            "max_duration": 30.0
        }
    }
    
    registry_data["subcategories"][sub_id] = registry_entry
    registry_data["total_subcategories"] = len(registry_data["subcategories"])
    
    with open(REGISTRY_PATH, "w", encoding="utf-8") as f:
        json.dump(registry_data, f, indent=2)
    print(f"[Synthesizer] Injected into master registry: {sub_id} (Total: {registry_data['total_subcategories']})")
    
    # 3. Lock run context
    context = {
        "run_id": f"dyn_{int(time.time())}",
        "locked_at": datetime.utcnow().isoformat() + "Z",
        "sub_category_id": sub_id,
        "sub_category_name": sub_name,
        "target_anime": anime_title,
        "character_focus": character_focus,
        "format_type": format_type,
        "requires_creator_credit": True
    }
    with open(RUN_CONTEXT_PATH, "w", encoding="utf-8") as f:
        json.dump(context, f, indent=2)
    print(f"[Synthesizer] Locked dynamic run context: {RUN_CONTEXT_PATH}")
    
    return registry_entry

if __name__ == "__main__":
    import time
    from datetime import datetime
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--anime", type=str, default="Solo Leveling")
    parser.add_argument("--character", type=str, default="Sung Jinwoo")
    parser.add_argument("--format", type=str, default="AnimeShort")
    args = parser.parse_args()
    
    synthesize_dynamic_subcategory(args.anime, args.character, args.format)
