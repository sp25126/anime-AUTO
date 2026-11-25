"""
Autonomous Viral Sound & Trend Radar (Instagram Reels / TikTok / YouTube Shorts)
Discovers real-time breakout songs and viral audio tracks:
1. Queries live global and regional music charts (Apple Music / iTunes Viral India & Global RSS).
2. Probes Instagram Reels trending audio playlists on YouTube.
3. Calculates velocity and determines if anime edit communities have adopted the sound.
4. Outputs the top breakout viral sound with search seeds for anime harvester.
"""

import sys
import json
import urllib.request
import subprocess
import re
from typing import Dict, Any, List, Optional

class ViralSoundRadar:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        
        # Curated evergreen breakout songs that frequently fuel viral anime edits
        self.fallback_trending_sounds = [
            {
                "sound_name": "Dilruba Dilnasheen",
                "artist": "Rito Riba",
                "vibe": "aesthetic_emotional",
                "tagline": "DILRUBA DILNASHEEN VIRAL EDITS",
                "search_keywords": ["Dilruba Dilnasheen", "Dilruba Rito Riba"]
            },
            {
                "sound_name": "Stateside x Zara Larsson",
                "artist": "Zara Larsson Remix",
                "vibe": "phonk_velocity",
                "tagline": "STATESIDE VIRAL ANIME EDITS",
                "search_keywords": ["Stateside Zara Larsson", "Stateside anime edit"]
            },
            {
                "sound_name": "Drums of Liberation / JoyBoy Phonk",
                "artist": "One Piece Soundtrack",
                "vibe": "climax_battle",
                "tagline": "DRUMS OF LIBERATION PHONK",
                "search_keywords": ["Drums of Liberation Phonk", "JoyBoy phonk 4k"]
            },
            {
                "sound_name": "Slava Phonk (Velocity Remix)",
                "artist": "Slava Funk",
                "vibe": "velocity_beatdrop",
                "tagline": "SLAVA PHONK VELOCITY EDITS",
                "search_keywords": ["Slava phonk edit 4k", "Slava anime velocity"]
            },
            {
                "sound_name": "Montagem Diamante Rosa",
                "artist": "Brazilian Phonk",
                "vibe": "hype_aura",
                "tagline": "MONTAGEM DIAMANTE ROSA EDITS",
                "search_keywords": ["Montagem Diamante Rosa anime", "Montagem anime edit 4k"]
            },
            {
                "sound_name": "Judas x Bloody Mary Phonk",
                "artist": "Lady Gaga Phonk Remix",
                "vibe": "cold_villain_aura",
                "tagline": "JUDAS PHONK COLD AURA",
                "search_keywords": ["Judas phonk anime edit", "Bloody Mary anime edit 4k"]
            }
        ]

    def fetch_live_itunes_viral_songs(self, country: str = "in") -> List[Dict[str, str]]:
        """
        Fetches official real-time top viral songs from Apple Music / iTunes RSS.
        """
        url = f"https://itunes.apple.com/{country}/rss/topsongs/limit=30/json"
        songs = []
        try:
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read().decode())
                entries = data.get("feed", {}).get("entry", [])
                for e in entries:
                    raw_title = e.get("im:name", {}).get("label", "")
                    artist = e.get("im:artist", {}).get("label", "")
                    # Clean title of movie/soundtrack noise
                    clean_name = re.sub(r"\(From [^\)]+\)", "", raw_title).strip()
                    clean_name = re.sub(r"\[From [^\]]+\]", "", clean_name).strip()
                    if clean_name and len(clean_name) > 2:
                        songs.append({
                            "sound_name": clean_name,
                            "artist": artist,
                            "vibe": "trending_commercial",
                            "tagline": f"{clean_name.upper()} VIRAL EDITS",
                            "search_keywords": [clean_name, f"{clean_name} {artist}"]
                        })
        except Exception as e:
            print(f"[Sound Radar] Notice: iTunes RSS unreachable ({e}). Using multi-platform YouTube/Reel signals.")
        return songs

    def fetch_reels_compilation_tracks(self) -> List[Dict[str, str]]:
        """
        Scrapes real-time trending Instagram Reels / TikTok track compilations from YouTube.
        """
        songs = []
        cmd = [
            sys.executable, "-m", "yt_dlp",
            "ytsearch4:trending reels audio instagram 2026",
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
                vid_id = d.get("id")
                # Sample individual compilation description/chapters
                if vid_id:
                    detail_cmd = [
                        sys.executable, "-m", "yt_dlp",
                        f"https://www.youtube.com/watch?v={vid_id}",
                        "--dump-json",
                        "--no-warnings"
                    ]
                    det_res = subprocess.run(detail_cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
                    if det_res.stdout:
                        try:
                            det_d = json.loads(det_res.stdout)
                            chapters = det_d.get("chapters") or []
                            for ch in chapters[:8]:
                                title = ch.get("title", "").strip()
                                # Clean chapter title
                                title = re.sub(r"^\d+[\.\s\-]+", "", title).strip()
                                if title and len(title) > 2 and not any(w in title.lower() for w in ["intro", "outro", "subscribe"]):
                                    songs.append({
                                        "sound_name": title,
                                        "artist": "Reels Trending",
                                        "vibe": "viral_reels",
                                        "tagline": f"{title.upper()} VIRAL EDITS",
                                        "search_keywords": [title]
                                    })
                        except Exception:
                            pass
                if len(songs) >= 10:
                    break
        except Exception as e:
            print(f"[Sound Radar] Compilation scan note: {e}")
        return songs

    def probe_anime_velocity_for_sound(self, sound_name: str) -> Dict[str, Any]:
        """
        Probes how active and viral the anime editing community is for this specific sound.
        Calculates:
        - Total views across top anime edits
        - Number of authentic anime edits available
        - Average view velocity
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
                
                # Check for anime edit markers
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

    def discover_hottest_viral_sound(self, history: List[str] = None) -> Dict[str, Any]:
        """
        Main Sound-First discovery function:
        1. Aggregates top songs from live charts & viral pool.
        2. Probes anime adoption velocity for top candidates.
        3. Returns the highest velocity winning sound with candidates.
        """
        history = [h.lower() for h in (history or [])]
        print("\n==================================================================")
        print("🎵 SOUND-FIRST VIRALITY RADAR: SCANNING TRENDING INSTAGRAM & TIKTOK AUDIO")
        print("==================================================================")

        # 1. Gather sound candidates
        candidate_sounds = []
        
        # iTunes / Apple Music (India + US)
        itunes_in = self.fetch_live_itunes_viral_songs(country="in")
        itunes_us = self.fetch_live_itunes_viral_songs(country="us")
        for s in itunes_in[:8] + itunes_us[:4]:
            if not any(c["sound_name"].lower() == s["sound_name"].lower() for c in candidate_sounds):
                candidate_sounds.append(s)

        # Curated evergreen viral tracks
        for s in self.fallback_trending_sounds:
            if not any(c["sound_name"].lower() == s["sound_name"].lower() for c in candidate_sounds):
                candidate_sounds.append(s)

        scored_sounds = []

        # Probe only the top 6 unvisited candidates to keep discovery lightning fast
        unvisited = [s for s in candidate_sounds if s["sound_name"].lower() not in history][:6]

        for sound in unvisited:
            name = sound["sound_name"]
            print(f"  • Probing anime edit adoption for: '{name}' ({sound.get('artist', 'Viral')})...")
            probe = self.probe_anime_velocity_for_sound(name)
            score = probe["velocity"] + (probe["edits_count"] * 1000)
            print(f"    -> Edits found: {probe['edits_count']} | Velocity: {int(probe['velocity']):,} views | Score: {int(score):,}")

            scored_sounds.append({
                "sound": sound,
                "metrics": probe,
                "score": score
            })

        # Sort descending by score
        scored_sounds.sort(key=lambda x: x["score"], reverse=True)

        if not scored_sounds or scored_sounds[0]["metrics"]["edits_count"] == 0:
            # Pick a trending sound that has verified anime edits
            for s in self.fallback_trending_sounds:
                if s["sound_name"].lower() not in history:
                    probe = self.probe_anime_velocity_for_sound(s["sound_name"])
                    if probe["edits_count"] > 0:
                        print(f"  ✓ Using verified breakout anime edit sound: '{s['sound_name']}'")
                        return {
                            "sound_name": s["sound_name"],
                            "artist": s.get("artist", "Viral"),
                            "tagline": s.get("tagline", f"{s['sound_name'].upper()} EDITS"),
                            "candidates": probe["candidates"]
                        }

        winner = scored_sounds[0]
        w_sound = winner["sound"]
        print("------------------------------------------------------------------")
        print(f"🔥 BREAKOUT VIRAL SOUND SELECTED: '{w_sound['sound_name']}'")
        print(f"   Artist: {w_sound.get('artist', 'Viral Trending')}")
        print(f"   Velocity Score: {int(winner['score']):,}")
        print("==================================================================\n")

        return {
            "sound_name": w_sound["sound_name"],
            "artist": w_sound.get("artist", "Viral"),
            "tagline": w_sound.get("tagline", f"{w_sound['sound_name'].upper()} EDITS"),
            "candidates": winner["metrics"]["candidates"]
        }

if __name__ == "__main__":
    radar = ViralSoundRadar()
    winner = radar.discover_hottest_viral_sound()
    print("Radar Winner:", json.dumps(winner, indent=2))
