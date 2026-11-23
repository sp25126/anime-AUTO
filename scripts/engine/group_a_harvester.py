"""
Master Multi-Platform Group A Anime Harvester
Supports:
1. Dynamic Multi-Scale Modes:
   - MACRO_THEME: Cross-anime compilation across multiple top franchises (e.g. Anime Fight Scenes, Coldest Aura, Beat Drops).
   - MICRO_FRANCHISE: Single-anime locked compilation (e.g. Naruto fight scenes, Dandadan, Jujutsu Kaisen).
2. 100% PURE ANIME ONLY (Zero cars, zero games, zero Marvel, zero IRL).
3. Anti-Content-ID Audio Shield (+2.5% micro pitch modulation + EBU R128 normalization).
4. High-Contrast Animated Ranking HUD (#5 to #1 CLIMAX).
5. Full Container Download to guarantee continuous audio.
"""

import os
import sys
import json
import re
import random
import subprocess
from PIL import Image, ImageDraw, ImageFont
from typing import List, Dict, Optional, Any

from semantic_roster import MACRO_THEME_REFERENCE_POOLS, MICRO_FRANCHISE_REFERENCE_POOLS

ANIME_DISCOVERY_ROSTER = [
    {"anime": "Jujutsu Kaisen", "characters": ["Gojo", "Sukuna", "Toji", "Yuji", "Megumi", "Yuta", "Nanami", "Mahito"]},
    {"anime": "Demon Slayer", "characters": ["Tanjiro", "Zenitsu", "Rengoku", "Akaza", "Kokushibo", "Yoriichi", "Tengen", "Muichiro"]},
    {"anime": "Solo Leveling", "characters": ["Sung Jin-Woo", "Igris", "Beru", "Shadow Monarch"]},
    {"anime": "Bleach", "characters": ["Ichigo", "Aizen", "Yhwach", "Kenpachi", "Byakuya", "Ulquiorra", "Grimmjow", "Yamamoto"]},
    {"anime": "One Piece", "characters": ["Luffy Gear 5", "Zoro", "Sanji", "Shanks", "Kaido", "Law", "Whitebeard", "Ace"]},
    {"anime": "Dandadan", "characters": ["Okarun", "Momo", "Turbo Granny", "Aira", "Jiji"]},
    {"anime": "Attack on Titan", "characters": ["Eren Yeager", "Levi Ackerman", "Mikasa", "Erwin Smith", "Armin", "Beast Titan"]},
    {"anime": "Chainsaw Man", "characters": ["Denji", "Makima", "Aki", "Power", "Katana Man"]},
    {"anime": "Naruto", "characters": ["Madara", "Itachi", "Sasuke", "Kakashi", "Pain", "Minato", "Obito", "Might Guy"]},
    {"anime": "Dragon Ball", "characters": ["Goku Ultra Instinct", "Vegeta", "Gohan Beast", "Broly", "Future Trunks", "Frieza"]},
    {"anime": "Hunter x Hunter", "characters": ["Gon Rage", "Killua Godspeed", "Hisoka", "Meruem", "Netero", "Chrollo"]},
    {"anime": "Black Clover", "characters": ["Asta Demon Form", "Yuno", "Yami Sukehiro", "Julius", "Mereoleona", "Noelle"]},
    {"anime": "Blue Lock", "characters": ["Isagi Yoichi", "Bachira", "Nagi Seishiro", "Rin Itoshi", "Barou", "Chigiri"]},
    {"anime": "Frieren", "characters": ["Frieren", "Fern", "Stark", "Himmel", "Serie", "Ubel"]},
    {"anime": "Mob Psycho 100", "characters": ["Mob 100%", "Reigen", "Toichiro", "Serizawa", "Dimple"]},
    {"anime": "One Punch Man", "characters": ["Saitama", "Garou Cosmic Fear", "Genos", "Boros", "Tatsumaki"]},
    {"anime": "Tokyo Ghoul", "characters": ["Kaneki Ken", "Touka", "Arima", "Juuzou", "Ayato"]},
    {"anime": "Vinland Saga", "characters": ["Thorfinn", "Askeladd", "Thorkell", "Canute"]},
    {"anime": "Fire Force", "characters": ["Shinra Kusakabe", "Arthur Boyle", "Beni", "Benimaru Shinmon"]},
    {"anime": "Fate", "characters": ["Gilgamesh", "Saber Alter", "Archer", "Berserker", "Shirou Emiya", "Lancer"]},
    {"anime": "Berserk", "characters": ["Guts", "Griffith", "Zodd"]},
    {"anime": "Overgeared", "characters": ["Grid", "Greed", "Khan"]},
    {"anime": "Bungo Stray Dogs", "characters": ["Dazai", "Chuya", "Akutagawa", "Atsushi"]},
    {"anime": "Seven Deadly Sins", "characters": ["Escanor", "Meliodas", "Ban", "King", "Zeldris"]},
    {"anime": "Monster", "characters": ["Johan Liebert", "Johan", "Tenma"]}
]

NON_ANIME_BANNED_KEYWORDS = [
    "free fire", "ff edit", "pubg", "bgmi", "gta", "gta 5", "fortnite", "roblox", "minecraft",
    "cod", "call of duty", "valorant", "league of legends", "genshin impact", "honkai", "clash royale",
    "spider-man", "spiderman", "batman", "superman", "iron man", "avengers", "marvel", "dc", "hulk",
    "deadpool", "wolverine", "cocomelon", "peppa pig", "talking tom", "poppy playtime", "skibidi",
    "gtr", "r35", "supra", "bmw", "mercedes", "audi", "lamborghini", "ferrari", "porsche", "mustang",
    "car edit", "jdm", "drift car", "ronaldo", "messi", "neymar", "football edit", "cricket", "hollywood", "movie edit"
]

class MasterAnimeGroupAHarvester:
    def __init__(self, workspace_root: str):
        self.workspace_root = workspace_root
        self.input_dir = os.path.join(workspace_root, "input", "group_a_harvest")
        self.cuts_dir = os.path.join(workspace_root, "output", "group_a_cuts")
        os.makedirs(self.input_dir, exist_ok=True)
        os.makedirs(self.cuts_dir, exist_ok=True)

    def is_strictly_anime(self, title: str, channel: str, required_anime: str = None) -> bool:
        text = f"{title} {channel}".lower()
        if any(b in text for b in NON_ANIME_BANNED_KEYWORDS):
            return False

        # If a specific franchise is required (e.g. Naruto)
        if required_anime and required_anime.lower() not in text:
            # Check characters for that franchise
            matched_char = False
            for entry in ANIME_DISCOVERY_ROSTER:
                if entry["anime"].lower() == required_anime.lower():
                    if any(ch.lower() in text for ch in entry["characters"]):
                        matched_char = True
                        break
            if not matched_char:
                return False

        has_generic_anime_tag = any(k in text for k in ["anime", "amv", "sakuga", "waifu", "shonen", "otaku"])
        matches_character = False
        for entry in ANIME_DISCOVERY_ROSTER:
            if entry["anime"].lower() in text:
                matches_character = True
                break
            for ch in entry["characters"]:
                if ch.lower() in text:
                    matches_character = True
                    break
            if matches_character:
                break

        return has_generic_anime_tag or matches_character

    def extract_clip_vibrant_accent(self, video_path: str, seek_sec: float = 3.0) -> tuple:
        """
        Samples a keyframe from the clip and extracts the most vibrant/saturated dominant accent color.
        Adapts dynamically to the fight/background (e.g. fire/orange, blood/red, cursed/purple, neon/cyan).
        """
        try:
            cmd = [
                "ffmpeg", "-ss", str(seek_sec), "-i", video_path,
                "-vframes", "1", "-f", "image2pipe", "-vcodec", "png", "-"
            ]
            proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            if not proc.stdout:
                return (0, 240, 255)
            import io
            img = Image.open(io.BytesIO(proc.stdout)).convert("RGB")
            small = img.resize((32, 32))
            colors = small.getcolors(32 * 32)
            if not colors:
                return (0, 240, 255)

            best_c = (0, 240, 255)
            max_sat = 0.0
            for count, (r, g, b) in colors:
                # Filter out pure blacks/shadows and overblown whites
                if r + g + b < 70 or r + g + b > 710:
                    continue
                max_val = max(r, g, b)
                min_val = min(r, g, b)
                sat = (max_val - min_val) / max(1, max_val)
                if sat > max_sat:
                    max_sat = sat
                    best_c = (r, g, b)

            # Boost brightness/vibrancy so text is vivid on dark HUD box
            mx = max(best_c)
            if mx > 0:
                boost = 255.0 / mx
                best_c = (
                    min(255, int(best_c[0] * boost)),
                    min(255, int(best_c[1] * boost)),
                    min(255, int(best_c[2] * boost))
                )
            return best_c
        except Exception:
            return (0, 240, 255)

    def generate_hud_overlay_image(self, rank: int, title_line1: str, title_line2: str, creator: str, views: str, output_path: str, accent_color: tuple = None):
        img = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        try:
            font_title = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 62)
            font_sub = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 70)
            font_rank = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 95)
            font_small = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 32)
        except Exception:
            font_title = ImageFont.load_default()
            font_sub = ImageFont.load_default()
            font_rank = ImageFont.load_default()
            font_small = ImageFont.load_default()

        if accent_color is None:
            accent_color = (0, 240, 255)

        # Top Header Box: tinted background from fight aura + vibrant neon border + glow
        card_bg = (
            int(accent_color[0] * 0.14) + 8,
            int(accent_color[1] * 0.14) + 8,
            int(accent_color[2] * 0.14) + 12,
            238
        )
        outer_glow = (accent_color[0], accent_color[1], accent_color[2], 70)
        border_color = (accent_color[0], accent_color[1], accent_color[2], 240)
        
        # Soft atmospheric outer glow rim
        draw.rounded_rectangle([(66, 126), (1014, 319)], radius=26, outline=outer_glow, width=3)
        # Main solid card
        draw.rounded_rectangle([(70, 130), (1010, 315)], radius=24, fill=card_bg, outline=border_color, width=4)
        draw.text((540, 185), title_line1, font=font_title, fill=(255, 255, 255), anchor="mm")
        
        # Scale down font_sub if title_line2 is long
        sub_len = font_sub.getlength(title_line2)
        if sub_len > 860:
            scale_ratio = 860 / sub_len
            new_size = max(38, int(70 * scale_ratio))
            font_sub_scaled = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", new_size)
        else:
            font_sub_scaled = font_sub
        draw.text((540, 260), title_line2, font=font_sub_scaled, fill=accent_color, anchor="mm")

        # Rank Badge: Clean "#1" without "CLIMAX" text, tinted to background
        rank_bg = (
            int(accent_color[0] * 0.18) + 10 if rank == 1 else 20,
            int(accent_color[1] * 0.18) + 10 if rank == 1 else 20,
            int(accent_color[2] * 0.18) + 15 if rank == 1 else 30,
            240
        )
        rank_fg = accent_color if rank == 1 else (255, 255, 255)
        rank_label = f"#{rank}"

        badge_w = int(font_rank.getlength(rank_label)) + 60
        box_left = 60
        box_right = box_left + max(200, badge_w)
        badge_border = (accent_color[0], accent_color[1], accent_color[2], 240) if rank == 1 else (accent_color[0], accent_color[1], accent_color[2], 140)
        draw.rounded_rectangle([(box_left, 470), (box_right, 595)], radius=20, fill=rank_bg, outline=badge_border, width=4)
        draw.text(((box_left + box_right)//2, 532), rank_label, font=font_rank, fill=rank_fg, anchor="mm")

        # Creator Credit
        credit_text = f"Edit: {creator} • {views}"
        credit_w = int(font_small.getlength(credit_text)) + 40
        c_left = 60
        c_right = min(1000, c_left + max(480, credit_w))
        draw.rounded_rectangle([(c_left, 1340), (c_right, 1410)], radius=18, fill=(15, 15, 25, 210), outline=(255, 255, 255, 40), width=2)
        draw.text(((c_left + c_right)//2, 1375), credit_text, font=font_small, fill=(240, 240, 240), anchor="mm")

        img.save(output_path, "PNG")
        return output_path

    def harvest_ranking_pack(self, trend_decision: Dict[str, Any] = None, target_clips_count: int = 5) -> Optional[str]:
        """
        Dynamically adapts based on the Intelligent Trend Gate:
        - If mode is 'MICRO_FRANCHISE': Locks to that single anime (e.g. Naruto fight scenes).
        - If mode is 'MACRO_THEME': Fans out across 5 distinct anime franchises.
        """
        if not trend_decision:
            trend_decision = {
                "id": "macro_fights",
                "name": "Anime Fight Scenes & Clashes",
                "mode": "MACRO_THEME",
                "harvest_queries": ["anime fight scenes 4k edit short", "anime combat sakuga edit short"]
            }

        mode = trend_decision.get("mode", "MACRO_THEME")
        target_name = trend_decision.get("name", "Anime Fight Scenes")
        franchise_lock = trend_decision.get("franchise") # e.g. "Naruto" if micro
        theme_id = trend_decision.get("id", "macro_fights")

        print(f"\n[Master Anime Harvester] Mode: {mode} | Target: '{target_name}' (ID: {theme_id})...")

        collected_candidates = []
        seen_ids = set()

        if mode == "MICRO_FRANCHISE" and franchise_lock:
            # Check if franchise has curated semantic reference pool
            ref_pool = MICRO_FRANCHISE_REFERENCE_POOLS.get(franchise_lock)
            if ref_pool and len(ref_pool) >= target_clips_count:
                selected_refs = random.sample(ref_pool, target_clips_count)
            else:
                entry = next((e for e in ANIME_DISCOVERY_ROSTER if e["anime"].lower() == franchise_lock.lower()), None)
                chars = entry["characters"] if entry else [franchise_lock]
                selected_refs = [
                    {"character": chars[i % len(chars)], "form": "Peak Moment", "query": f"{chars[i % len(chars)]} {franchise_lock} fight scene edit 4k"}
                    for i in range(target_clips_count)
                ]

            for idx, ref in enumerate(selected_refs):
                char = ref["character"]
                q = ref["query"]
                print(f"  • Scouting Rank #{target_clips_count - idx}: {franchise_lock} ({char}) - '{ref.get('form', '')}'...")
                
                cmd = [sys.executable, "-m", "yt_dlp", f"ytsearch5:{q}", "--dump-json", "--flat-playlist", "--no-warnings"]
                res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
                for line in res.stdout.strip().split("\n"):
                    if not line: continue
                    try:
                        d = json.loads(line)
                        vid_id = d.get("id")
                        vid_title = d.get("title") or ""
                        uploader = d.get("uploader") or d.get("channel") or "Unknown"
                        dur = d.get("duration") or 0
                        # Accept clips >= 12s; if clip is shorter than 20s, it will loop seamlessly to 20s
                        if vid_id in seen_ids or not (12 <= dur <= 180): continue
                        if not self.is_strictly_anime(vid_title, uploader, required_anime=franchise_lock): continue
                        seen_ids.add(vid_id)
                        collected_candidates.append({
                            "id": vid_id, "title": vid_title, "anime": franchise_lock,
                            "character": char, "form": ref.get("form", char),
                            "uploader": uploader, "duration": dur,
                            "url": f"https://www.youtube.com/watch?v={vid_id}"
                        })
                        break
                    except: pass
        else:
            # Macro Theme: Check if theme has curated semantic reference pool
            macro_pool = list(MACRO_THEME_REFERENCE_POOLS.get(theme_id, []))
            if macro_pool and len(macro_pool) >= target_clips_count:
                random.shuffle(macro_pool)
                candidate_pool = macro_pool
            else:
                selected_roster = random.sample(ANIME_DISCOVERY_ROSTER, len(ANIME_DISCOVERY_ROSTER))
                candidate_pool = [
                    {"anime": e["anime"], "character": random.choice(e["characters"]), "form": "Viral Climax", "query": f"{random.choice(e['characters'])} {e['anime']} viral edit 4k"}
                    for e in selected_roster
                ]

            for ref in candidate_pool:
                if len(collected_candidates) >= target_clips_count:
                    break
                anime_name = ref["anime"]
                char = ref["character"]
                q = ref["query"]
                current_rank = target_clips_count - len(collected_candidates)
                print(f"  • Scouting Rank #{current_rank}: {anime_name} ({char}) - '{ref.get('form', '')}'...")

                # Search across TikTok, Instagram Reels, and YouTube Shorts syndications
                scout_queries = [
                    f"{q} tiktok edit",
                    f"{q} instagram reels amv 4k",
                    f"{q} amv 4k"
                ]
                candidate_found = False
                for sq in scout_queries:
                    if candidate_found: break
                    cmd = [sys.executable, "-m", "yt_dlp", f"ytsearch4:{sq}", "--dump-json", "--flat-playlist", "--no-warnings"]
                    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
                    for line in res.stdout.strip().split("\n"):
                        if not line: continue
                        try:
                            d = json.loads(line)
                            vid_id = d.get("id")
                            vid_title = d.get("title") or ""
                            uploader = d.get("uploader") or d.get("channel") or "Unknown"
                            dur = d.get("duration") or 0
                            # Accept clips >= 10s
                            if vid_id in seen_ids or not (10 <= dur <= 180): continue
                            if not self.is_strictly_anime(vid_title, uploader): continue
                            seen_ids.add(vid_id)
                            collected_candidates.append({
                                "id": vid_id, "title": vid_title, "anime": anime_name,
                                "character": char, "form": ref.get("form", char),
                                "uploader": uploader, "duration": dur,
                                "url": f"https://www.youtube.com/watch?v={vid_id}"
                            })
                            print(f"    ✓ Found candidate for Rank #{current_rank}: {vid_title[:45]} ({dur}s)")
                            candidate_found = True
                            break
                        except: pass

        print(f"[Master Anime Harvester] Harvested {len(collected_candidates)} verified 100% anime candidates.")
        prepared_clips = []
        for rank_idx, cand in enumerate(collected_candidates[:target_clips_count]):
            rank = target_clips_count - rank_idx
            raw_full = os.path.join(self.input_dir, f"full_{cand['anime'].replace(' ', '_')}_{cand['id']}.mp4")
            hud_png = os.path.join(self.cuts_dir, f"hud_rank_{rank}.png")
            out_clip = os.path.join(self.cuts_dir, f"prepared_rank_{rank}_{cand['id']}.mp4")

            # Dynamic HUD Titles based on Mode
            if mode == "MICRO_FRANCHISE":
                h_line1 = f"TOP 5 {franchise_lock.upper()} FIGHTS"
                h_line2 = f"{cand['character'].upper()}"
            else:
                if "aura" in theme_id:
                    h_line1 = "COLDEST AURA WALKS"
                elif "rage" in theme_id:
                    h_line1 = "ANIME RAGE AWAKENINGS"
                elif "beat_drop" in theme_id:
                    h_line1 = "HARDEST BEAT DROPS"
                elif "villain" in theme_id:
                    h_line1 = "COLDEST ANIME VILLAINS"
                elif "transform" in theme_id:
                    h_line1 = "PEAK TRANSFORMATIONS"
                elif "disrespect" in theme_id:
                    h_line1 = "COLDEST DISRESPECTS"
                elif "speed" in theme_id:
                    h_line1 = "FASTEST SPEEDSTERS"
                elif "sword" in theme_id:
                    h_line1 = "BADASS SWORD DRAWS"
                else:
                    h_line1 = "TOP 5 ANIME FIGHTS"
                h_line2 = f"{cand['anime'].upper()} • {cand['character'].upper()}"

            # Download full container to ensure full audio stream
            if not os.path.exists(raw_full) or os.path.getsize(raw_full) < 500000:
                print(f"[Harvester] Downloading Pure Anime #{rank}: {cand['anime']} - {cand['character']} (@{cand['uploader']})...")
                dl_cmd = [
                    sys.executable, "-m", "yt_dlp", cand["url"],
                    "-f", "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080][ext=mp4]/best",
                    "-o", raw_full,
                    "--no-warnings"
                ]
                subprocess.run(dl_cmd, capture_output=True)

            # Check if yt-dlp produced an alternate extension or name
            if not os.path.exists(raw_full):
                base_no_ext = os.path.splitext(raw_full)[0]
                for ext in [".webm", ".mkv", ".mp4.webm", ".mp4.mkv"]:
                    alt_p = base_no_ext + ext
                    if os.path.exists(alt_p) and os.path.getsize(alt_p) > 200000:
                        raw_full = alt_p
                        break

            # Cloud Runner Fallback: If live web download was blocked, strictly find matching anime clips
            if not os.path.exists(raw_full) or os.path.getsize(raw_full) < 200000:
                print(f"[Harvester Warning] Live download blocked for {cand['anime']}. Searching local verified cache...")
                matched_cached = None
                anime_slug = cand['anime'].replace(' ', '_').lower()
                char_slug = cand['character'].lower()
                
                # Search 1: Check repo assets/anime_clips_pool for exact anime or character match
                asset_pool = os.path.join(self.workspace_root, "assets", "anime_clips_pool")
                if os.path.exists(asset_pool):
                    for pool_f in os.listdir(asset_pool):
                        if pool_f.endswith((".mp4", ".webm")) and (anime_slug in pool_f.lower() or char_slug in pool_f.lower()):
                            pool_p = os.path.join(asset_pool, pool_f)
                            if os.path.getsize(pool_p) > 200000:
                                matched_cached = pool_p
                                break
                
                # Search 2: Check input/group_a_harvest for exact anime match
                if not matched_cached and os.path.exists(self.input_dir):
                    for cached_f in os.listdir(self.input_dir):
                        if cached_f.endswith((".mp4", ".webm")) and (anime_slug in cached_f.lower() or char_slug in cached_f.lower()):
                            cached_p = os.path.join(self.input_dir, cached_f)
                            if os.path.getsize(cached_p) > 500000:
                                matched_cached = cached_p
                                break

                # Search 3: For MACRO_THEME cross-anime rankings, if this specific anime is missing, pick any other authentic anime clip from pool
                if not matched_cached and mode == "MACRO_THEME" and os.path.exists(asset_pool):
                    available_pool = [os.path.join(asset_pool, f) for f in os.listdir(asset_pool) if f.endswith(".mp4")]
                    if available_pool:
                        matched_cached = available_pool[(rank - 1) % len(available_pool)]

                if matched_cached:
                    print(f"  ✓ Strict Cache hit for {cand['anime']}: {os.path.basename(matched_cached)}")
                    raw_full = matched_cached
                else:
                    print(f"  ❌ Skipping clip #{rank}: No authentic clip found matching franchise '{cand['anime']}'")
                    continue

            # Extract dynamic background accent color from the clip
            dynamic_accent = self.extract_clip_vibrant_accent(raw_full, seek_sec=3.0)

            # Generate HUD with dynamic color matching the fight background
            self.generate_hud_overlay_image(
                rank=rank,
                title_line1=h_line1,
                title_line2=h_line2,
                creator=f"@{cand['uploader'][:12]}",
                views="Viral",
                output_path=hud_png,
                accent_color=dynamic_accent
            )

            # Intelligently determine climax window without loops or premature climax cutoffs
            from climax_detector import detect_climax_window
            start_sec, clip_dur = detect_climax_window(
                raw_clip=raw_full,
                title=cand.get("title", ""),
                anime=cand.get("anime", ""),
                character=cand.get("character", "")
            )

            # Dynamic blurred background + 16:9 uncropped + HUD + Anti-Copyright Audio Protection with TEMPO COMPENSATION
            filter_complex = (
                f"[0:v]fps=30,split=2[fg_raw][bg_raw];"
                f"[bg_raw]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5,eq=brightness=-0.15:saturation=1.2[bg_blur];"
                f"[fg_raw]scale=1080:-2,setsar=1[fg_scaled];"
                f"[bg_blur][fg_scaled]overlay=0:(1920-h)/2[base_comp];"
                f"[base_comp][1:v]overlay=0:0[vout];"
                f"[0:a]aresample=48000,asetrate=48000*1.025,atempo=1/1.025,aresample=48000,apad,aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo,loudnorm=I=-14:TP=-1.5:LRA=7[aout]"
            )
            # ZERO stream looping: never repeat the first few seconds at the end!
            comp_cmd = [
                "ffmpeg", "-y",
                "-ss", f"{start_sec:.2f}", "-t", f"{clip_dur:.2f}",
                "-i", raw_full,
                "-i", hud_png,
                "-filter_complex", filter_complex,
                "-map", "[vout]", "-map", "[aout]",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                "-c:a", "aac", "-b:a", "256k",
                "-t", f"{clip_dur:.2f}",
                out_clip
            ]
            subprocess.run(comp_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if os.path.exists(out_clip) and os.path.getsize(out_clip) > 50000:
                prepared_clips.append(out_clip)

        if not prepared_clips:
            return None

        # Stitch 5 clips
        concat_txt = os.path.join(self.workspace_root, "output", "group_a_concat_list.txt")
        with open(concat_txt, "w", encoding="utf-8") as f:
            for p in prepared_clips:
                f.write(f"file '{os.path.abspath(p)}'\n")

        final_stitched = os.path.join(self.workspace_root, "output", "ranking_pure_anime_80s_master.mp4")
        stitch_cmd = [
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0",
            "-i", concat_txt,
            "-c:v", "copy",
            "-c:a", "copy",
            final_stitched
        ]
        subprocess.run(stitch_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if os.path.exists(final_stitched) and os.path.getsize(final_stitched) > 1000000:
            print(f"[Master Anime Harvester] SUCCESS: Created {len(prepared_clips)}-clip Pure Anime compilation: {final_stitched}")
            # Generate contact sheet proof for instant visual verification
            proof_sheet = os.path.join(self.workspace_root, "output", "group_a_local_proof_sheet.jpg")
            ps_cmd = [
                "ffmpeg", "-y",
                "-i", final_stitched,
                "-vf", "select='not(mod(n\\,120))',scale=270:480,tile=5x3",
                "-frames:v", "1",
                proof_sheet
            ]
            subprocess.run(ps_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if os.path.exists(proof_sheet):
                print(f"[Master Anime Harvester] QA Contact Sheet generated: {proof_sheet}")
            return final_stitched
        return None

if __name__ == "__main__":
    h = MasterAnimeGroupAHarvester(r"c:\Users\saumy\OneDrive\Desktop\anime compiation")
    print("MasterAnimeGroupAHarvester ready with Multi-Scale Macro/Micro support.")
