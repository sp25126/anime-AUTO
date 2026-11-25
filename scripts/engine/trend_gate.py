"""
Intelligent Trend Scout & Multi-Scale Niche Logic Gate
Researches live internet signals to determine:
1. Is a MACRO cross-anime theme trending? (e.g. 'anime fight scenes', 'aura walks', 'rage awakenings', 'beat drops')
2. OR is a MICRO single-franchise niche trending? (e.g. 'Naruto fight scenes', 'Dandadan edits', 'Solo Leveling Jinwoo arise')
3. Calculates exact Velocity Score V_trend based on view count velocity and upload recency.
4. Outputs the winner with execution parameters:
   - mode: 'MACRO_THEME' (multi-franchise) vs 'MICRO_FRANCHISE' (single-franchise locked)
   - target_name: e.g. 'Anime Fight Scenes' vs 'Naruto'
   - queries: exact candidate queries for the harvester
   - title_template: CTR-optimized title matching the research
"""

import sys
import json
import subprocess
from typing import Dict, Any, List

class IntelligentTrendGate:
    def __init__(self):
        # Candidate research pool: Macro Tropes vs Specific Franchise Trends
        self.macro_themes = [
            {
                "id": "macro_fights",
                "name": "Anime Fight Scenes & Clashes",
                "mode": "MACRO_THEME",
                "probe_query": "anime fight scenes edit shorts",
                "harvest_queries": [
                    "top 5 anime fight scenes edit 4k",
                    "anime swordsman clash 4k short",
                    "anime hand to hand fight edit 60fps",
                    "insane anime combat sakuga edit"
                ],
                "title_template": "Top 5 Insane Anime Fight Scenes That Broke YouTube! ⚔️💥 #shorts #anime"
            },
            {
                "id": "macro_aura",
                "name": "Coldest Anime Aura Walks",
                "mode": "MACRO_THEME",
                "probe_query": "anime aura walk edit shorts",
                "harvest_queries": [
                    "anime characters with 1000000 aura edit",
                    "coldest anime villain walk phonk edit",
                    "anime walking menacingly edit 4k"
                ],
                "title_template": "Top 5 COLDEST Anime Aura Walks In History! 💀🥶 #shorts #anime"
            },
            {
                "id": "macro_rage",
                "name": "Pure Anime Rage Awakenings",
                "mode": "MACRO_THEME",
                "probe_query": "anime characters rage snap edit shorts",
                "harvest_queries": [
                    "top 5 anime characters losing control edit 4k",
                    "pure rage awakening anime moments shorts",
                    "anime characters who lost all control edit"
                ],
                "title_template": "Top 5 Anime Characters Who Lost All Control & Snapped! 👹⚡ #shorts #anime"
            },
            {
                "id": "macro_beat_drop",
                "name": "Hardest Anime Phonk Beat Drops",
                "mode": "MACRO_THEME",
                "probe_query": "anime phonk beat drop edit shorts",
                "harvest_queries": [
                    "anime phonk beat drop 4k edit short",
                    "best anime velocity phonk edit 60fps",
                    "anime edit sync beat drop shorts"
                ],
                "title_template": "Top 5 HARDEST Anime Beat Drops on TikTok & YouTube! 🔥🔊 #shorts #animeedit"
            },
            {
                "id": "macro_villains",
                "name": "Most Menacing Anime Villains",
                "mode": "MACRO_THEME",
                "probe_query": "coldest anime villain moments edit shorts",
                "harvest_queries": [
                    "top 5 coldest anime villains edit 4k",
                    "anime villain dominance phonk edit",
                    "anime villains with insane aura short"
                ],
                "title_template": "Top 5 Anime Villains With UNTOUCHABLE Aura! 😈💀 #shorts #anime"
            },
            {
                "id": "macro_transformations",
                "name": "Insane Anime Transformations",
                "mode": "MACRO_THEME",
                "probe_query": "insane anime transformation edit shorts",
                "harvest_queries": [
                    "top 5 anime transformations edit 4k",
                    "anime ultimate form awakening edit",
                    "most iconic anime transformations short"
                ],
                "title_template": "Top 5 Most CHILLING Anime Transformations! ⚡🔥 #shorts #anime"
            },
            {
                "id": "macro_disrespect",
                "name": "Most Disrespectful Cold Moments",
                "mode": "MACRO_THEME",
                "probe_query": "most disrespectful anime moments edit shorts",
                "harvest_queries": [
                    "top 5 disrespectful anime moments 4k",
                    "coldest anime disrespect edit phonk",
                    "anime reality checks edit short"
                ],
                "title_template": "Top 5 Most DISRESPECTFUL Anime Moments In History! 💀🥶 #shorts #anime"
            },
            {
                "id": "macro_speed",
                "name": "Insane Anime Speedsters",
                "mode": "MACRO_THEME",
                "probe_query": "fastest anime speedsters edit shorts",
                "harvest_queries": [
                    "top 5 fastest anime characters edit 4k",
                    "anime speed blitz phonk edit 60fps",
                    "anime characters moving at light speed short"
                ],
                "title_template": "Top 5 FASTEST Anime Speedsters That Broke Reality! ⚡💨 #shorts #anime"
            },
            {
                "id": "macro_sword_draws",
                "name": "Badass Sword Unsheathing Moments",
                "mode": "MACRO_THEME",
                "probe_query": "anime sword draw edit shorts",
                "harvest_queries": [
                    "top 5 anime sword unsheathing moments 4k",
                    "coldest anime katana click edit short",
                    "anime swordsman bad ass draw phonk"
                ],
                "title_template": "Top 5 Most BADASS Anime Sword Draws Ranked! 🗡️🔥 #shorts #anime"
            }
        ]

        self.micro_franchises = [
            {
                "id": "micro_naruto",
                "name": "Naruto Fight Scenes",
                "franchise": "Naruto",
                "mode": "MICRO_FRANCHISE",
                "probe_query": "Naruto fight scenes edit shorts",
                "characters": ["Madara", "Itachi", "Sasuke", "Kakashi", "Pain", "Minato", "Obito", "Might Guy"],
                "harvest_queries": [
                    "Naruto best fight scenes edit 4k",
                    "Madara vs shinobi alliance 4k edit short",
                    "Kakashi vs Obito 4k 60fps edit short",
                    "Naruto Shippuden coldest fights edit"
                ],
                "title_template": "Top 5 GREATEST Naruto Fight Scenes Ranked! 🔥💀 #shorts #naruto #anime"
            },
            {
                "id": "micro_jjk",
                "name": "Jujutsu Kaisen Climax Edits",
                "franchise": "Jujutsu Kaisen",
                "mode": "MICRO_FRANCHISE",
                "probe_query": "Jujutsu Kaisen viral edit shorts",
                "characters": ["Gojo", "Sukuna", "Toji", "Yuji", "Megumi", "Yuta"],
                "harvest_queries": [
                    "best jjk edits ranking shorts",
                    "Gojo vs Sukuna 4k 60fps edit short",
                    "Toji Fushiguro 4k edit phonk short",
                    "Sukuna flame arrow 4k edit short"
                ],
                "title_template": "Top 5 Coldest Jujutsu Kaisen Moments Ranked! 💀⚡ #shorts #jjk #anime"
            },
            {
                "id": "micro_sololeveling",
                "name": "Solo Leveling Arise Edits",
                "franchise": "Solo Leveling",
                "mode": "MICRO_FRANCHISE",
                "probe_query": "Solo Leveling jinwoo arise edit shorts",
                "characters": ["Sung Jin-Woo", "Igris", "Beru", "Shadow Monarch"],
                "harvest_queries": [
                    "Solo Leveling Sung Jin-Woo arise 4k edit",
                    "Jin-Woo vs Beru 4k 60fps edit short",
                    "Solo Leveling phonk edit shorts"
                ],
                "title_template": "Top 5 Coldest Solo Leveling Jin-Woo Moments! 👑🗡️ #shorts #sololeveling"
            },
            {
                "id": "micro_dandadan",
                "name": "Dandadan Viral Sakuga",
                "franchise": "Dandadan",
                "mode": "MICRO_FRANCHISE",
                "probe_query": "Dandadan viral edit shorts",
                "characters": ["Okarun", "Momo", "Turbo Granny", "Aira"],
                "harvest_queries": [
                    "Dandadan Okarun transformation 4k edit short",
                    "Dandadan best fight scenes edit 60fps",
                    "Dandadan viral edit tiktok shorts"
                ],
                "title_template": "Top 5 Insane Dandadan Moments That Broke The Internet! 👽⚡ #shorts #dandadan"
            },
            {
                "id": "micro_demonslayer",
                "name": "Demon Slayer Infinity Castle & Sakuga",
                "franchise": "Demon Slayer",
                "mode": "MICRO_FRANCHISE",
                "probe_query": "Demon Slayer infinity castle edit shorts",
                "characters": ["Tanjiro", "Zenitsu", "Rengoku", "Akaza", "Kokushibo", "Yoriichi"],
                "harvest_queries": [
                    "Demon Slayer infinity castle 4k 60fps edit",
                    "Zenitsu 7th form 4k edit short",
                    "Demon Slayer coldest fight scenes edit"
                ],
                "title_template": "Top 5 Coldest Demon Slayer Fights Ranked! ⚔️🔥 #shorts #demonslayer"
            },
            {
                "id": "micro_bleach",
                "name": "Bleach TYBW Bankai Clashes",
                "franchise": "Bleach",
                "mode": "MICRO_FRANCHISE",
                "probe_query": "Bleach TYBW bankai edit shorts",
                "characters": ["Ichigo", "Aizen", "Yhwach", "Kenpachi", "Yamamoto", "Byakuya"],
                "harvest_queries": [
                    "Bleach TYBW best bankai 4k edit short",
                    "Aizen chair kyoka suigetsu edit 60fps",
                    "Yamamoto bankai zanka no tachi edit"
                ],
                "title_template": "Top 5 Coldest Bleach TYBW Moments Ranked! 🗡️⚡ #shorts #bleach #anime"
            },
            {
                "id": "micro_onepiece",
                "name": "One Piece Peak Moments",
                "franchise": "One Piece",
                "mode": "MICRO_FRANCHISE",
                "probe_query": "One Piece peak moments edit shorts",
                "characters": ["Luffy Gear 5", "Zoro", "Sanji", "Shanks", "Kaido"],
                "harvest_queries": [
                    "Luffy Gear 5 drums of liberation edit 4k",
                    "Zoro king of hell 4k edit short",
                    "Shanks divine departure edit 60fps"
                ],
                "title_template": "Top 5 PEAK One Piece Moments That Broke The Internet! 🏴‍☠️🔥 #shorts #onepiece"
            }
        ]

    def probe_trend_velocity(self, query: str) -> float:
        """
        Samples live YouTube search metadata for the probe query
        and calculates average view velocity across the top 5 results.
        """
        cmd = [
            sys.executable, "-m", "yt_dlp",
            f"ytsearch5:{query}",
            "--dump-json",
            "--flat-playlist",
            "--no-warnings"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
        total_views = 0
        valid_count = 0
        for line in res.stdout.strip().split("\n"):
            if not line:
                continue
            try:
                d = json.loads(line)
                views = d.get("view_count") or 0
                dur = d.get("duration") or 0
                # Filter to shorts format (<= 90s)
                if dur <= 90:
                    total_views += views
                    valid_count += 1
            except Exception:
                pass
        return float(total_views / max(1, valid_count))

    def evaluate_live_market(self, history: List[str] = None) -> Dict[str, Any]:
        """
        Executes live market velocity research across:
        1. Sound-First Radar: Trending Instagram Reels / TikTok songs (e.g. Dilruba Dilnasheen).
        2. Macro Themes (Cross-anime fights, aura, rage, beat drops).
        3. Micro Franchises (Bleach, Naruto, Dandadan, etc.).
        Picks the highest velocity candidate not in recent history.
        """
        history = [h.lower() for h in (history or [])]

        print("\n==================================================================")
        print("🔍 INTELLIGENT TREND GATE: PROBING REAL-TIME INTERNET VIRALITY")
        print("==================================================================")

        # 1. First probe Sound-First Virality Radar (Instagram / TikTok)
        try:
            from viral_sound_radar import ViralSoundRadar
            sound_radar = ViralSoundRadar()
            sound_winner = sound_radar.discover_hottest_viral_sound(history=history)
            if sound_winner and sound_winner.get("candidates") and len(sound_winner["candidates"]) >= 2:
                s_name = sound_winner["sound_name"]
                print(f"[Trend Gate] 🎵 SOUND-FIRST WINNER IDENTIFIED: '{s_name}'")
                return {
                    "id": f"sound_{s_name.replace(' ', '_').lower()}",
                    "name": f"{s_name} Viral Anime Edits",
                    "mode": "VIRAL_SOUND",
                    "viral_sound": s_name,
                    "artist": sound_winner.get("artist"),
                    "title_template": f"Top 5 {s_name} Anime Edits That Broke The Internet! 🔥🎵 #shorts #anime",
                    "harvest_queries": [
                        f"{s_name} anime edit 4k",
                        f"{s_name} anime edit tiktok",
                        f"{s_name} amv edit shorts"
                    ]
                }
        except Exception as e:
            print(f"[Trend Gate] Sound radar fallback note: {e}")

        candidates = self.macro_themes + self.micro_franchises
        scored_results = []

        for item in candidates:
            if item["id"].lower() in history or item["name"].lower() in history:
                print(f"  [Skip Recent] {item['name']}")
                continue
            
            print(f"  • Probing: '{item['probe_query']}' ({item['mode']})...")
            velocity = self.probe_trend_velocity(item["probe_query"])
            print(f"    -> Average Velocity: {int(velocity):,} views/video")
            
            scored_results.append({
                "item": item,
                "velocity": velocity
            })

        # Sort by velocity descending
        scored_results.sort(key=lambda x: x["velocity"], reverse=True)

        if not scored_results:
            fallback = self.macro_themes[0]
            return fallback

        winner = scored_results[0]["item"]
        winner_velocity = scored_results[0]["velocity"]

        print("------------------------------------------------------------------")
        print(f"🏆 TREND WINNER DETECTED: {winner['name']}")
        print(f"   Mode: {winner['mode']}")
        print(f"   Velocity: {int(winner_velocity):,} views")
        print("==================================================================\n")

        return winner

if __name__ == "__main__":
    gate = IntelligentTrendGate()
    decision = gate.evaluate_live_market()
    print("Decision Output:", json.dumps(decision, indent=2))
