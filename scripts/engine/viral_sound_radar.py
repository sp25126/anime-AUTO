"""
Autonomous Dynamic Viral Audio & Trend Radar (Zero Hardcoding)
Discovers real-time breakout songs and viral audio tracks:
1. Queries live Apple Music / iTunes RSS charts (India + Global/US).
2. Probes live YouTube Shorts & Instagram Reels trending audio compilations dynamically.
3. Automatically evaluates anime edit adoption velocity.
4. Dynamically scores and picks the hottest viral sound with ZERO hardcoded sound names or artists.
"""

import os
import sys
import json
import urllib.request
import subprocess
import re
from typing import Dict, Any, List, Optional

class ViralSoundRadar:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    def fetch_live_itunes_viral_songs(self, country: str = "in", limit: int = 30) -> List[Dict[str, Any]]:
        """
        Fetches official real-time top viral songs from Apple Music / iTunes RSS.
        100% dynamic - no hardcoded track lists.
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
                    # Clean title of movie/soundtrack parenthetical noise
                    clean_name = re.sub(r"\(From [^\)]+\)", "", raw_title, flags=re.IGNORECASE).strip()
                    clean_name = re.sub(r"\[From [^\]]+\]", "", clean_name, flags=re.IGNORECASE).strip()
                    clean_name = re.sub(r"\(feat\.[^\)]+\)", "", clean_name, flags=re.IGNORECASE).strip()
                    clean_name = re.sub(r"\[feat\.[^\]]+\]", "", clean_name, flags=re.IGNORECASE).strip()
                    clean_name = clean_name.strip(" -")
                    if clean_name and len(clean_name) >= 2:
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
        Dynamically searches live YouTube Shorts trends for top trending background audio / phonk / reels tracks.
        """
        discovered = []
        queries = [
            "trending reels audio viral shorts",
            "trending anime phonk audio edit shorts",
            "viral tiktok sound anime edit shorts"
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
                    # Extract song or phonk title candidate using regex patterns
                    # e.g. "Song Name - Artist", "Montagem ...", "... (Phonk Remix)"
                    cleaned = re.sub(r"[\(\[\{].*?[\)\]\}]", "", title)
                    cleaned = re.sub(r"(amv|edit|4k|60fps|shorts|status|tiktok|reels)", "", cleaned, flags=re.IGNORECASE).strip(" -|#")
                    if len(cleaned) >= 3 and not any(w in cleaned.lower() for w in ["top", "best", "compilation", "episode", "season"]):
                        discovered.append({
                            "sound_name": cleaned,
                            "artist": d.get("uploader") or "Viral Sound",
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
        Returns total views, candidate anime edits, and average velocity.
        """
        query = f"{sound_name} anime edit"
        cmd = [
            sys.executable, "-m", "yt_dlp",
            f"ytsearch5:{query}",
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
                
                # Check for genuine anime edit markers
                if any(w in title.lower() for w in ["edit", "amv", "anime", "4k", "status", "shorts"]):
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
        Main 100% Zero-Hardcoding Sound-First discovery:
        1. Aggregates live music charts (iTunes India + Global/US).
        2. Aggregates live YouTube Shorts trending audio.
        3. Dynamically probes anime adoption velocity.
        4. Returns the winning live sound with verified candidate clips.
        """
        history = [h.lower() for h in (history or [])]
        print("\n==================================================================")
        print("🎵 ZERO-HARDCODING SOUND RADAR: SCANNING LIVE INTERNET CHARTS & REELS")
        print("==================================================================")

        # 1. Harvest live songs from charts
        raw_candidates = []
        itunes_in = self.fetch_live_itunes_viral_songs(country="in", limit=25)
        itunes_us = self.fetch_live_itunes_viral_songs(country="us", limit=15)
        shorts_trends = self.fetch_live_trending_phonk_and_reels()

        for pool in [itunes_in, itunes_us, shorts_trends]:
            for s in pool:
                name = s["sound_name"].strip()
                if not any(c["sound_name"].lower() == name.lower() for c in raw_candidates):
                    raw_candidates.append(s)

        print(f"[Sound Radar] Gathered {len(raw_candidates)} live sound candidates from real-time charts.")

        # Filter out recently used songs
        unvisited = [s for s in raw_candidates if s["sound_name"].lower() not in history][:8]
        if not unvisited and raw_candidates:
            unvisited = raw_candidates[:5]

        scored_sounds = []
        for sound in unvisited:
            name = sound["sound_name"]
            print(f"  • Probing anime adoption for: '{name}' ({sound.get('artist', 'Viral')})...")
            probe = self.probe_anime_velocity_for_sound(name)
            # Velocity score weighted by number of authentic edits found
            score = probe["velocity"] + (probe["edits_count"] * 2500)
            print(f"    -> Edits found: {probe['edits_count']} | Velocity: {int(probe['velocity']):,} views | Score: {int(score):,}")

            if probe["edits_count"] > 0:
                scored_sounds.append({
                    "sound": sound,
                    "metrics": probe,
                    "score": score
                })

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

        print("[Sound Radar] Notice: No strong anime adoption found in current music charts; falling back to visual trend discovery.")
        return None

if __name__ == "__main__":
    radar = ViralSoundRadar()
    winner = radar.discover_hottest_viral_sound()
    print("Winner:", json.dumps(winner, indent=2))
