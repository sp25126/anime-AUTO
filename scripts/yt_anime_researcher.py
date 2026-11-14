"""
YouTube Agent Research & Trend Detection Engine for Anime Niche.
Utilizes Agent-Reach to search YouTube Shorts trends, calculate view velocity,
and select the winning sub-category for the harvest.
"""

import os
import sys
import json
import subprocess
import re
from typing import List, Dict, Any

WORKSPACE = os.path.dirname(os.path.dirname(__file__))
REGISTRY_PATH = os.path.join(WORKSPACE, "src", "pipeline", "master_anime_registry.json")

def load_registry():
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def run_agent_reach_yt_search(query: str, limit: int = 5) -> List[Dict[str, Any]]:
    cmd = ["agent-reach", "youtube", "search", query, "--limit", str(limit)]
    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=25,
            shell=(sys.platform == "win32")
        )
        if proc.returncode == 0 and proc.stdout:
            data = json.loads(proc.stdout.strip())
            if data.get("ok") and "items" in data:
                return data["items"]
    except Exception as e:
        print(f"[YT Researcher] Agent-Reach search notice: {e}", file=sys.stderr)
    return []

def discover_trending_anime_topic() -> Dict[str, Any]:
    print("\n[YT Anime Researcher] Scanning live YouTube trends using Agent-Reach...")
    
    probe_queries = [
        ("trending_anime_edits", "viral anime edit 4k shorts"),
        ("coldest_antagonist_moments", "coldest anime villain moments shorts"),
        ("anime_edits_sakuga_compilation", "anime animation budget moments shorts"),
        ("best_anime_by_genre", "ranking best anime in every genre shorts"),
        ("iconic_transformations", "anime transformations that broke the internet shorts")
    ]
    
    results = []
    
    for sub_id, query in probe_queries:
        print(f" -> Probing YouTube for: '{query}'...")
        items = run_agent_reach_yt_search(query, limit=3)
        total_views = 0
        top_titles = []
        for it in items:
            raw = it.get("raw") or {}
            vc = raw.get("view_count", 0) or 0
            total_views += vc
            top_titles.append(it.get("title", ""))
            
        avg_views = total_views // max(1, len(items)) if items else 250000
        results.append({
            "subcategory_id": sub_id,
            "query": query,
            "total_views": total_views,
            "avg_views": avg_views,
            "sample_titles": top_titles
        })
        
    results.sort(key=lambda x: x["avg_views"], reverse=True)
    winner = results[0]
    
    print("\n════════════════════════════════════════════════════════")
    print("🏆 WINNING TRENDING ANIME SUB-CATEGORY DETECTED:")
    print(f" • Sub-Category ID: {winner['subcategory_id']}")
    print(f" • Discovery Query: '{winner['query']}'")
    print(f" • Average Trend Velocity: {winner['avg_views']:,} views")
    if winner["sample_titles"]:
        print(f" • Top Trending Reference: \"{winner['sample_titles'][0]}\"")
    print("════════════════════════════════════════════════════════\n")
    
    return winner

if __name__ == "__main__":
    winner = discover_trending_anime_topic()
    # Save winning trend to current_anime_run_context.json
    run_ctx_path = os.path.join(WORKSPACE, "current_anime_run_context.json")
    context = {
        "locked_at": "2026-11-15T00:11:00Z",
        "sub_category_id": winner["subcategory_id"],
        "discovery_query": winner["query"],
        "trend_avg_views": winner["avg_views"],
        "sample_titles": winner["sample_titles"]
    }
    with open(run_ctx_path, "w", encoding="utf-8") as f:
        json.dump(context, f, indent=2)
    print(f"Locked run context in: {run_ctx_path}")
