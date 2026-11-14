"""
Autonomous Single-Anime Dynamic Isolation & Virality Pipeline.
Flow:
1. Scans YouTube trends to discover which single anime franchise is exploding right now (e.g. JJK, Solo Leveling, Dandadan, Blue Lock, Sakamoto Days, Kaiju No. 8).
2. Dynamically isolates that anime franchise.
3. Automatically synthesizes a dedicated skill & registry entry if not already present.
4. Searches and harvests top-tier viral edits ONLY for that specific anime.
5. Builds cue sheet with on-screen credit tags (CC:@creator) and full description attribution.
"""

import os
import sys
import json
import re
from typing import Dict, Any, List

WORKSPACE = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, WORKSPACE)

from scripts.virality_engine import run_virality_scan
from scripts.anime_harvester import AnimeHarvester
from scripts.dynamic_skill_synthesizer import synthesize_anime_skill
from scripts.description_builder import build_youtube_description

REGISTRY_PATH = os.path.join(WORKSPACE, "src", "pipeline", "master_anime_registry.json")

def pick_accent_color(franchise_name: str) -> str:
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
    return palette.get(franchise_name.lower(), "#FF0055")

def run_dynamic_single_anime_pipeline(force_franchise: str = None) -> Dict[str, Any]:
    print("═══════════════════════════════════════════════════════════════")
    print("🔥 DYNAMIC SINGLE-ANIME RANKING PIPELINE")
    print("═══════════════════════════════════════════════════════════════")

    # Step 1: Discover Winning Franchise via live virality engine
    if force_franchise:
        winning_franchise = force_franchise
        print(f"[DynamicEngine] Franchise specified: '{winning_franchise}'")
    else:
        print("[DynamicEngine] Scanning YouTube virality to discover the #1 trending anime...")
        scan_report = run_virality_scan(max_queries=4)
        winning_franchise = scan_report.get("winning_franchise", "Jujutsu Kaisen")
        print(f"[DynamicEngine] Algorithm winner detected: '{winning_franchise}' 🚀")

    sub_id = f"ranking_{winning_franchise.lower().replace(' ', '_')}_edits"
    accent_color = pick_accent_color(winning_franchise)

    # Step 2: Ensure skill and registry are synthesized dynamically
    synthesize_anime_skill(
        anime_title=winning_franchise,
        trending_reason=f"Detected as #1 breakout anime in real-time virality scan",
        notable_characters=[winning_franchise]
    )

    # Step 3: Harvest strictly for this single anime using AnimeHarvester
    harvester = AnimeHarvester(subcategory_id=sub_id)
    print(f"\n[DynamicEngine] Harvesting edits strictly isolated to: {winning_franchise}")
    
    # Run YouTube harvest with single-anime franchise isolation
    yt_clips = harvester.harvest_youtube(count=5)

    # Sort descending by view count to create rank 5 -> 1 countdown
    yt_clips.sort(key=lambda x: x.get("views", 0), reverse=True)
    top_5 = yt_clips[:5]

    # In Remotion countdown, Rank 5 plays first, Rank 1 plays last as the climax
    ranked_clips = []
    commentary_pool = ["TS AHH 🙏", "CLEAN FLOW ⚡", "WATERMARK SO PEAK 🙏", "CHILLS 🥶", "PEAK FICTION 👑"]

    for i, c in enumerate(reversed(top_5)):
        rank_num = 5 - i # 5, 4, 3, 2, 1
        creator = c.get("creator", "Unknown Creator")
        views = c.get("views", 0)
        view_text = f"{views / 1_000_000:.1f}M" if views >= 1_000_000 else f"{views / 1_000:.0f}K"

        clean_creator = creator.replace(" ", "").replace("@", "")
        ranked_clips.append({
            "rankNumber": rank_num,
            "label": c.get("title", f"{winning_franchise} Moment")[:30],
            "viewCountText": view_text,
            "commentaryText": commentary_pool[i % len(commentary_pool)],
            "creatorCredit": f"@{clean_creator}",
            "original_creator": creator,
            "platform": "YouTube",
            "source_url": c.get("source_url", ""),
            "anime_title": winning_franchise,
            "studio": c.get("studio", "Respective Studio"),
            "videoPath": c.get("local_path", f"public/clips/{c.get('id', 'clip')}.mp4"),
            "durationInFrames": 120 + (i * 15) # 4s up to 6s climax
        })

    # Step 4: Build Cue Sheet for RankingShort Remotion composition
    cue_sheet = {
        "topTitleLine1": "RANKING THE BEST",
        "topTitleLine2": f"{winning_franchise.upper()} EDITS",
        "accentWord": winning_franchise.upper(),
        "accentColor": accent_color,
        "backgroundMode": "blur-clone",
        "audioPath": "public/audio/stems/versus_phonk_bed.mp3",
        "clips": ranked_clips
    }

    cue_sheet_path = os.path.join(WORKSPACE, f"cue_sheet_{sub_id}.json")
    with open(cue_sheet_path, "w", encoding="utf-8") as f:
        json.dump(cue_sheet, f, indent=2)
    print(f"\n[DynamicEngine] Cue Sheet Generated: {cue_sheet_path}")

    # Step 5: Build compliant YouTube description with full credits
    desc_meta = {
        "name": f"Ranking The Best {winning_franchise} Edits",
        "focus": f"Top 5 Most Viral {winning_franchise} Edits Ranked",
        "description_tags": ["#shorts", "#anime", f"#{winning_franchise.lower().replace(' ', '')}", "#animeedits"]
    }
    desc_text = build_youtube_description(desc_meta, [
        {
            "rank": c["rankNumber"],
            "anime_title": c["anime_title"],
            "studio": c["studio"],
            "original_creator": c["original_creator"],
            "platform": c["platform"],
            "source_url": c["source_url"]
        } for c in ranked_clips
    ])

    desc_path = os.path.join(WORKSPACE, "output", f"{sub_id}_description.txt")
    with open(desc_path, "w", encoding="utf-8") as f:
        f.write(desc_text)
    print(f"[DynamicEngine] Attribution Description Generated: {desc_path}")

    return {
        "winning_franchise": winning_franchise,
        "sub_id": sub_id,
        "cue_sheet_path": cue_sheet_path,
        "description_path": desc_path,
        "clips": ranked_clips
    }

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--franchise", type=str, default=None, help="Force specific anime franchise")
    args = parser.parse_args()
    run_dynamic_single_anime_pipeline(force_franchise=args.franchise)
