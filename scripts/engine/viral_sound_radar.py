"""
Autonomous Dynamic Viral Audio & Trend Radar (Zero Hardcoding & Anti-Pollution Gate)
Ported from Otaku Production Standards:
1. Queries live Apple Music / iTunes RSS charts (India + Global/US).
2. Cleans titles and filters out non-anime/devotional noise (e.g. Bhajans, Aarti, film dialogue).
3. Evaluates genuine anime edit adoption velocity across YouTube Shorts & TikTok.
4. Validates that actual anime edits exist for the sound before selecting it.
"""

import os
import sys
import json
import urllib.request
import subprocess
import re
from typing import Dict, Any, List, Optional

ENGINE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ENGINE_DIR)

try:
    from proxy_harvester import is_valid_anime_clip, scout_youtube_anime_edits, scout_tiktok_anime_edits
except ImportError:
    pass

NON_ANIME_MUSIC_KEYWORDS = [
    "bhajan", "aarti", "chalisa", "ramayana", "hanuman", "krishna", "sitaram",
    "shree ram", "mantra", "katha", "stotra", "devotional", "movie scene", "trailer",
    "dialogue", "speech", "interview", "podcast", "vlog", "prank", "news"
]

class ViralSoundRadar:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    def is_clean_sound_candidate(self, title: str, artist: str = "") -> bool:
        """Filters out non-musical or devotional audio that doesn't fit anime edits."""
        combined = f"{title} {artist}".lower()
        if any(w in combined for w in NON_ANIME_MUSIC_KEYWORDS):
            return False
        # Must be at least 3 chars
        return len(title.strip()) >= 3

    def fetch_live_itunes_viral_songs(self, country: str = "in", limit: int = 30) -> List[Dict[str, Any]]:
        """
        Fetches official real-time top viral songs from Apple Music / iTunes RSS.
        Filters out devotional/spoken tracks.
        """
        url = f"https://itunes.apple.com/{country}/rss/topsongs/limit={limit}/json"
        songs = []
        try:
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                entries = data.get("feed", {}).get("entry", [])
                for e in entries:
                    raw_title = e.get("im:name", {}).get("label", "")
                    artist = e.get("im:artist", {}).get("label", "")
                    clean_name = re.sub(r"\(From [^\)]+\)", "", raw_title, flags=re.IGNORECASE).strip()
                    clean_name = re.sub(r"\[From [^\]]+\]", "", clean_name, flags=re.IGNORECASE).strip()
                    clean_name = re.sub(r"\(feat\.[^\)]+\)", "", clean_name, flags=re.IGNORECASE).strip()
                    clean_name = re.sub(r"\[feat\.[^\]]+\]", "", clean_name, flags=re.IGNORECASE).strip()
                    clean_name = clean_name.strip(" -")
                    
                    if self.is_clean_sound_candidate(clean_name, artist):
                        songs.append({
                            "sound_name": clean_name,
                            "artist": artist,
                            "source": f"itunes_{country}",
                            "tagline": f"{clean_name.upper()} VIRAL EDITS",
                            "search_keywords": [clean_name, f"{clean_name} {artist}".strip()]
                        })
        except Exception as e:
            print(f"[Sound Radar] iTunes RSS notice for {country}: {e}")
        return songs

    def fetch_live_trending_phonk_and_reels(self) -> List[Dict[str, Any]]:
        """
        Dynamically searches live YouTube Shorts trends for top trending anime phonk / edit audios.
        """
        discovered = []
        queries = [
            "trending anime phonk audio edit shorts",
            "viral anime edit song shorts 2026",
            "hottest anime audio edit trend"
        ]
        for q in queries:
            cmd = [
                sys.executable, "-m", "yt_dlp",
                f"ytsearch5:{q}",
                "--dump-json",
                "--flat-playlist",
                "--no-warnings"
            ]
            try:
                res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
                for line in res.stdout.strip().split("\n"):
                    if not line:
                        continue
                    d = json.loads(line)
                    title = d.get("title") or ""
                    cleaned = re.sub(r"[\(\[\{].*?[\)\]\}]", "", title)
                    cleaned = re.sub(r"(amv|edit|4k|60fps|shorts|status|tiktok|reels|anime)", "", cleaned, flags=re.IGNORECASE).strip(" -|#")
                    if len(cleaned) >= 3 and self.is_clean_sound_candidate(cleaned):
                        discovered.append({
                            "sound_name": cleaned,
                            "artist": d.get("uploader") or "Phonk Creator",
                            "source": "live_yt_shorts",
                            "tagline": f"{cleaned.upper()} VIRAL EDITS",
                            "search_keywords": [cleaned, f"{cleaned} anime edit"]
                        })
            except Exception as e:
                print(f"[Sound Radar] Live probe notice: {e}")
        return discovered

    def probe_anime_velocity_for_sound(self, sound_name: str) -> Dict[str, Any]:
        """
        Probes how actively viral the anime editing community is using this sound right now.
        STRICT REQUIREMENT: At least 2 candidate clips must pass genuine anime verification.
        """
        query = f"{sound_name} anime edit"
        cmd = [
            sys.executable, "-m", "yt_dlp",
            f"ytsearch8:{query}",
            "--dump-json",
            "--flat-playlist",
            "--no-warnings"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
        total_views = 0
        edits_count = 0
        top_candidates = []

        for line in res.stdout.strip().split("\n"):
            if not line:
                continue
            try:
                d = json.loads(line)
                dur = d.get("duration") or 0
                views = d.get("view_count") or 0
                title = d.get("title") or ""
                uploader = d.get("uploader") or ""
                
                # Enforce strict anime filter: reject non-anime or devotional clips
                if not is_valid_anime_clip(title, uploader):
                    continue

                if dur <= 90:
                    total_views += views
                    edits_count += 1
                    top_candidates.append({
                        "id": d.get("id"),
                        "title": title,
                        "uploader": uploader,
                        "views": views,
                        "duration": dur,
                        "url": f"https://www.youtube.com/watch?v={d.get('id')}"
                    })
            except Exception:
                pass

        avg_velocity = float(total_views / max(1, edits_count)) if edits_count > 0 else 0.0
        return {
            "sound_name": sound_name,
            "edits_count": edits_count,
            "total_views": total_views,
            "velocity": avg_velocity,
            "candidates": top_candidates
        }

    def discover_hottest_viral_sound(self, history: List[str] = None) -> Optional[Dict[str, Any]]:
        """
        Main Sound-First discovery:
        Scans charts and requires genuine anime edits to exist before selecting.
        """
        history = [h.lower() for h in (history or [])]
        print("\n==================================================================")
        print("🎵 VIRAL SOUND RADAR: SCANNING LIVE INTERNET CHARTS & ANIME BUZZ")
        print("==================================================================")

        raw_candidates = []
        itunes_in = self.fetch_live_itunes_viral_songs(country="in", limit=20)
        itunes_us = self.fetch_live_itunes_viral_songs(country="us", limit=15)
        shorts_trends = self.fetch_live_trending_phonk_and_reels()

        for pool in [shorts_trends, itunes_us, itunes_in]:
            for s in pool:
                name = s["sound_name"].strip()
                if not any(c["sound_name"].lower() == name.lower() for c in raw_candidates):
                    raw_candidates.append(s)

        print(f"[Sound Radar] Gathered {len(raw_candidates)} clean candidate tracks.")

        unvisited = [s for s in raw_candidates if s["sound_name"].lower() not in history][:8]
        if not unvisited and raw_candidates:
            unvisited = raw_candidates[:5]

        scored_sounds = []
        for sound in unvisited:
            name = sound["sound_name"]
            print(f"  • Probing anime adoption for: '{name}' ({sound.get('artist', 'Viral')})...")
            probe = self.probe_anime_velocity_for_sound(name)
            # ONLY consider sounds that have authentic anime edits
            if probe["edits_count"] >= 2:
                score = probe["velocity"] + (probe["edits_count"] * 5000)
                print(f"    -> Authentic anime edits found: {probe['edits_count']} | Velocity: {int(probe['velocity']):,} views | Score: {int(score):,}")
                scored_sounds.append({
                    "sound": sound,
                    "metrics": probe,
                    "score": score
                })
            else:
                print(f"    -> Skipped (insufficient authentic anime edits: {probe['edits_count']})")

        # Sort descending by score
        scored_sounds.sort(key=lambda x: x["score"], reverse=True)

        if scored_sounds:
            winner = scored_sounds[0]
            w_sound = winner["sound"]
            w_metrics = winner["metrics"]
            print(f"  ✓ WINNING LIVE VIRAL AUDIO: '{w_sound['sound_name']}' (Score: {int(winner['score']):,})")
            return {
                "sound_name": w_sound["sound_name"],
                "artist": w_sound.get("artist", "Viral Music"),
                "velocity": w_metrics["velocity"],
                "edits_count": w_metrics["edits_count"],
                "candidates": w_metrics["candidates"]
            }

        print("[Sound Radar] Notice: No trending music tracks passed strict anime verification; delegating to anime show discovery.")
        return None

if __name__ == "__main__":
    radar = ViralSoundRadar()
    winner = radar.discover_hottest_viral_sound()
    print("Winner:", json.dumps(winner, indent=2))
