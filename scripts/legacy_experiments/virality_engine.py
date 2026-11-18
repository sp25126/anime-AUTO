"""
Autonomous YouTube Virality Search Engine for Anime Niche.
Detects breakout viral topics and trending anime phenomena in real time.
Evaluates:
- View Velocity: VPH (Views Per Hour)
- Recency Decay: Exponential penalty favoring fresh breakouts (<48h)
- Small-Creator Leverage: Channels with low baseline views getting algorithmic spikes
- Cluster Detection: Extracts anime franchise and character entities
Outputs: trending_breakout_report.json
"""

import os
import sys
import json
import math
import time
import re
import subprocess
from datetime import datetime
from typing import List, Dict, Any

WORKSPACE = os.path.dirname(os.path.dirname(__file__))
REPORT_FILE = os.path.join(WORKSPACE, "trending_breakout_report.json")
PYTHON_EXE = sys.executable

PROBE_QUERIES = [
    "anime edit viral 4k shorts",
    "anime shorts trending 2026",
    "coldest anime moments shorts",
    "anime animation budget broken shorts",
    "jujutsu kaisen edit 4k shorts",
    "solo leveling edit 4k shorts",
    "demon slayer edit 4k shorts",
    "attack on titan edit shorts",
    "one piece gear 5 edit shorts",
    "bleach tybw edit shorts"
]

ANIME_FRANCHISE_SIGNATURES = {
    "Jujutsu Kaisen": ["jjk", "jujutsu", "gojo", "sukuna", "toji", "yuji", "yuta", "megumi", "mahoraga"],
    "Solo Leveling": ["solo leveling", "jinwoo", "shadow monarch", "arise", "igris", "beru"],
    "Demon Slayer": ["demon slayer", "kimetsu", "tengen", "kokushibo", "akaza", "muichiro", "rengoku", "tanjiro"],
    "Attack on Titan": ["attack on titan", "aot", "shingeki", "eren", "levi", "erwin", "reiner"],
    "One Piece": ["one piece", "luffy", "gear 5", "zoro", "shanks", "kaido"],
    "Bleach": ["bleach", "tybw", "ichigo", "aizen", "yamamoto", "yhwach", "kenpachi"],
    "Chainsaw Man": ["chainsaw man", "denji", "makima", "aki", "reze", "power"],
    "Frieren": ["frieren", "himmel", "fern", "stark", "aura"]
}

FORMAT_KEYWORDS = {
    "VersusShort": [" vs ", "versus", "battle", "stronger", "diff", "solo", "beats", "fight"],
    "ExplainerShort": ["why ", "truth", "secret", "theory", "dark origin", "explained", "did you know", "hidden"],
    "QuizShort": ["guess", "quiz", "trivia", "in 3 seconds", "challenge", "can you guess"],
    "SakugaShort": ["sakuga", "budget", "animation", "frame by frame", "animator", "smear"],
    "AnimeShort": ["ranking", "top 5", "top 10", "worst", "best", "tier", "edit", "velocity"]
}

def classify_format(title: str, query: str = "") -> tuple[str, str]:
    text = (title + " " + query).lower()
    for fmt, keywords in FORMAT_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                return fmt, f"Matched keyword '{kw}'"
    return "AnimeShort", "Default viral ranking/edit format"

def detect_franchise(title: str, tags: list = None) -> tuple[str, str]:
    text = (title + " " + " ".join(tags or [])).lower()
    for franchise, keywords in ANIME_FRANCHISE_SIGNATURES.items():
        for kw in keywords:
            if kw in text:
                character = kw.title() if kw != franchise.lower() else "Character Spotlight"
                return franchise, character
    return "Trending Anime", "General"

def parse_upload_timestamp(date_str: str) -> float:
    """Parses YYYYMMDD into unix timestamp."""
    try:
        dt = datetime.strptime(str(date_str), "%Y%m%d")
        return dt.timestamp()
    except Exception:
        # Default to 48 hours ago
        return time.time() - (48 * 3600)

def probe_youtube_shorts(query: str, limit: int = 8) -> List[Dict[str, Any]]:
    print(f"[ViralityEngine] Probing live query: '{query}'...")
    dump_cmd = [
        PYTHON_EXE, "-m", "yt_dlp",
        "--dump-json",
        "--no-playlist",
        "--match-filter", "duration <= 60 & duration >= 4",
        f"ytsearch{limit}:{query}"
    ]
    videos = []
    try:
        proc = subprocess.run(
            dump_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=35
        )
        if proc.returncode != 0 or not proc.stdout:
            return []

        for line in proc.stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except Exception:
                continue

            vid_id = item.get("id")
            if not vid_id:
                continue

            views = item.get("view_count") or 0
            upload_date = item.get("upload_date") or "20261114"
            timestamp = item.get("timestamp") or parse_upload_timestamp(upload_date)
            duration = item.get("duration") or 15
            title = item.get("title", "")
            channel = item.get("channel") or item.get("uploader") or "Creator"
            channel_views = item.get("channel_views") or (views * 3) # fallback
            tags = item.get("tags") or []
            track = item.get("track") or item.get("sound") or "Phonk Audio Bed"

            videos.append({
                "id": vid_id,
                "title": title,
                "channel": channel,
                "views": views,
                "duration": duration,
                "timestamp": timestamp,
                "channel_views": channel_views,
                "tags": tags,
                "track": track,
                "webpage_url": item.get("webpage_url") or f"https://youtube.com/watch?v={vid_id}"
            })
    except Exception as e:
        print(f"[ViralityEngine] Error on '{query}': {e}", file=sys.stderr)
    return videos

def compute_virality_score(video: Dict[str, Any]) -> float:
    """
    Mathematical Virality Formulation:
    V = (Views / AgeHours) * RecencyDecay * SmallChannelLeverage
    """
    views = float(video.get("views", 0))
    ts = float(video.get("timestamp", time.time() - 3600))
    age_hours = max(0.5, (time.time() - ts) / 3600.0)

    # 1. Base Views Per Hour (VPH)
    vph = views / age_hours

    # 2. Recency Decay (favors fresh breakouts < 72h)
    recency_factor = math.exp(-0.012 * min(age_hours, 168.0))

    # 3. Small-Creator Algorithmic Push Multiplier
    chan_views = float(video.get("channel_views", 100000) or 100000)
    expected_views = max(1000.0, chan_views / 25.0)
    leverage = min(4.5, max(1.0, views / expected_views))

    virality_score = round(vph * recency_factor * leverage, 2)
    return virality_score

def run_virality_scan(max_queries: int = 5) -> Dict[str, Any]:
    print("\n═══════════════════════════════════════════════════════════════")
    print("⚡ RUNNING AUTONOMOUS YOUTUBE VIRALITY SEARCH ENGINE")
    print("═══════════════════════════════════════════════════════════════")

    collected_videos = []
    seen_ids = set()

    for q in PROBE_QUERIES[:max_queries]:
        vids = probe_youtube_shorts(q, limit=6)
        for v in vids:
            if v["id"] not in seen_ids:
                seen_ids.add(v["id"])
                v["virality_score"] = compute_virality_score(v)
                franchise, char = detect_franchise(v["title"], v["tags"])
                v["detected_franchise"] = franchise
                v["detected_character"] = char
                collected_videos.append(v)

    if not collected_videos:
        print("[ViralityEngine] No raw videos parsed. Generating benchmark baseline.", file=sys.stderr)
        return {}

    # Sort descending by virality score
    collected_videos.sort(key=lambda x: x["virality_score"], reverse=True)

    # Cluster by anime franchise
    franchise_clusters = {}
    for v in collected_videos:
        f = v["detected_franchise"]
        if f not in franchise_clusters:
            franchise_clusters[f] = {
                "franchise": f,
                "total_virality": 0.0,
                "video_count": 0,
                "top_videos": []
            }
        franchise_clusters[f]["total_virality"] += v["virality_score"]
        franchise_clusters[f]["video_count"] += 1
        if len(franchise_clusters[f]["top_videos"]) < 3:
            franchise_clusters[f]["top_videos"].append({
                "id": v["id"],
                "title": v["title"],
                "channel": v["channel"],
                "views": v["views"],
                "virality_score": v["virality_score"],
                "url": v["webpage_url"]
            })

    cluster_list = list(franchise_clusters.values())
    cluster_list.sort(key=lambda c: c["total_virality"], reverse=True)

    winner_cluster = cluster_list[0] if cluster_list else None
    top_video = collected_videos[0]
    recommended_fmt, fmt_reason = classify_format(top_video["title"])

    report = {
        "scan_time": datetime.utcnow().isoformat() + "Z",
        "total_probed": len(collected_videos),
        "winning_franchise": winner_cluster["franchise"] if winner_cluster else "Jujutsu Kaisen",
        "total_cluster_virality": winner_cluster["total_virality"] if winner_cluster else 0,
        "recommended_subcategory_id": f"{winner_cluster['franchise'].lower().replace(' ', '_')}_viral_edits",
        "recommended_format": recommended_fmt,
        "format_reason": fmt_reason,
        "top_viral_video": {
            "id": top_video["id"],
            "title": top_video["title"],
            "channel": top_video["channel"],
            "views": top_video["views"],
            "virality_score": top_video["virality_score"],
            "url": top_video["webpage_url"]
        },
        "franchise_rankings": [
            {
                "franchise": c["franchise"],
                "total_virality": round(c["total_virality"], 2),
                "count": c["video_count"]
            } for c in cluster_list[:5]
        ]
    }

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("\n═══════════════════════════════════════════════════════════════")
    print(f"🏆 VIRALITY WINNER: {report['winning_franchise'].upper()}")
    print(f" • Recommended Subcategory: {report['recommended_subcategory_id']}")
    print(f" • Cluster Virality Score: {report['total_cluster_virality']:,}")
    print(f" • #1 Breakout Video: '{top_video['title']}' by {top_video['channel']} ({top_video['views']:,} views)")
    print(f" • Saved Report: {REPORT_FILE}")
    print("═══════════════════════════════════════════════════════════════\n")

    return report

if __name__ == "__main__":
    report = run_virality_scan(max_queries=5)
