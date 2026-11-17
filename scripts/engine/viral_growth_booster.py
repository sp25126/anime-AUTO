"""
Autonomous Viral Growth Booster & Post-Production Workflow
Triggers automatically whenever a video render completes:
1. Researches real-time trending titles, curiosity hooks, and high-CTR phrasing.
2. Extracts mega-trending keywords and unrelated boost tags (SEO injection).
3. Computes the optimal upload time based on audience geography (7:30 PM IST / 14:00 UTC).
4. Generates an algorithmic description packed with fair-use copyright disclaimers, credits, and keyword stacks.
5. Implements FREE viral boost mechanisms:
   - High-engagement pinned comment prompt (sparks comment debates).
   - Dynamic animated end-card hook & subscribe prompt.
   - Related video deep-linking & playlist tagging.
"""

import os
import sys
import json
import random
import datetime
import subprocess
from typing import Dict, Any, List

ENGINE_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_ROOT = os.path.abspath(os.path.join(ENGINE_DIR, "..", ".."))
sys.path.append(ENGINE_DIR)

from metadata_engine import MetadataComplianceEngine

# Mega high-traffic booster tags across anime + unrelated viral pop-culture niches
UNRELATED_BOOST_KEYWORDS = [
    # Mega Anime Fandoms
    "jujutsu kaisen", "jjk", "gojo vs sukuna", "sukuna malevolent shrine",
    "demon slayer", "infinity castle", "tanjiro", "zenitsu godspeed",
    "one piece", "luffy gear 5", "zoro king of hell", "shanks divine departure",
    "solo leveling", "sung jin woo arise", "shadow monarch", "beru vs jin woo",
    "bleach tybw", "aizen kyoka suigetsu", "yamamoto bankai", "ichigo vasto lorde",
    "dandadan", "okarun turbo granny", "frieren beyond journeys end",
    "chainsaw man", "attack on titan", "eren yeager rumbling", "naruto shippuden",
    # Unrelated Mega-Trends (Cross-Niche Algorithm Leeching)
    "mrbeast", "sigma", "phonk", "gta6", "speed", "ishowspeed", "kai cenat",
    "trend", "explore", "tiktok", "reels", "gaming", "capcut"
]

TRENDING_HASHTAG_STACK = [
    "#shorts", "#anime", "#animeedit", "#fyp", "#viral", "#foryou",
    "#animetiktok", "#animeshorts", "#coldestanimemoments", "#sakuga",
    "#jjk", "#onepiece", "#gear5", "#sololeveling", "#demonslayer",
    "#dandadan", "#bleach", "#naruto", "#animecommunity"
]

# Random & unrelated viral hashtag pools to hijack broad YouTube Shorts feed traffic
UNRELATED_VIRAL_NICHE_HASHTAGS = [
    "#mrbeast", "#gaming", "#gta6", "#phonk", "#sigma", "#kaicenat",
    "#ishowspeed", "#trendingshorts", "#ytshorts", "#explore", "#viralvideo",
    "#popular", "#blowthisup", "#capcut", "#edit", "#tiktokviral",
    "#epic", "#entertainment", "#satisfying", "#cinema"
]

class ViralGrowthBoosterWorkflow:
    def __init__(self):
        self.metadata_engine = MetadataComplianceEngine(
            youtube_creds_path=os.path.join(WORKSPACE_ROOT, "config", "youtube_token.json")
        )

    def probe_live_trending_hashtags(self) -> List[str]:
        """
        Dynamically scrapes the top real-time trending hashtags from current viral YouTube Shorts,
        capturing whatever random topic, pop-culture meme, or trend is booming right now.
        """
        discovered = []
        try:
            cmd = [
                sys.executable, "-m", "yt_dlp",
                "ytsearch6:#shorts trending",
                "--dump-json", "--flat-playlist", "--no-warnings"
            ]
            res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
            for line in res.stdout.strip().split("\n"):
                if not line: continue
                try:
                    d = json.loads(line)
                    title = d.get("title", "")
                    for token in title.split():
                        if token.startswith("#") and len(token) > 2 and len(token) < 25:
                            clean_tag = token.strip(".,!?:;").lower()
                            if clean_tag not in discovered:
                                discovered.append(clean_tag)
                except Exception:
                    pass
        except Exception:
            pass
        return discovered[:8]

    def calculate_best_upload_schedule(self) -> Dict[str, Any]:
        """
        Calculates optimal global audience upload window:
        - 7:30 PM IST (14:00 UTC) = Peak prime-time viewing across India, Asia, and European evening, 
          leading directly into US East Coast morning/lunch browsing.
        - Scans current scheduled queue to ensure zero collision.
        """
        next_slot = self.metadata_engine.get_next_available_release_slot()
        ist_time = next_slot + datetime.timedelta(hours=5, minutes=30)
        return {
            "scheduled_utc": next_slot,
            "scheduled_utc_iso": next_slot.isoformat(),
            "scheduled_ist_str": ist_time.strftime("%Y-%m-%d %I:%M %p IST"),
            "strategy": "Peak Asian & European Prime Time (7:30 PM IST / 2:00 PM UTC) + US Morning Surge"
        }

    def generate_viral_curiosity_title(self, target_name: str, group_type: str = "GROUP_A", rank1_char: str = "") -> str:
        """
        Creates psychological curiosity hooks designed to stop thumbs from scrolling.
        Employs open loops, extreme contrast, and debate sparks.
        """
        clean_name = target_name.replace("Top 5", "").replace("Anime", "").strip()
        if group_type == "GROUP_A":
            templates = [
                f"Top 5 Coldest {clean_name} In Anime History! 💀🥶 #shorts #anime",
                f"Rank #1 Broke The Entire Internet! 🔥💀 ({clean_name}) #shorts #animeedit",
                f"Top 5 Most Insane {clean_name} Ranked! ⚔️🔥 #shorts #anime",
                f"Nobody Expected Rank #1 To Do That... 😱⚡ ({clean_name}) #shorts",
                f"Top 5 Legendary {clean_name} Ranked From #5 To #1! 👑💥 #shorts #anime"
            ]
            if rank1_char:
                templates.append(f"Is {rank1_char} Really #1?! 💀 Top 5 {clean_name} #shorts #anime")
            return random.choice(templates)
        elif group_type == "GROUP_B":
            return f"ROTATE YOUR PHONE for Maximum Chills! 📱🔄⚡ ({clean_name}) #shorts #animeedit"
        else:
            return f"The Way They Reacted Is Actually Insane 😭💀 | {clean_name} #shorts"

    def generate_pinned_comment_bait(self, target_name: str, rank1_name: str = "Rank #1") -> str:
        """
        FREE VIRAL BOOST #1: High-engagement pinned comment.
        Forces viewers into intense comment debates, driving the YouTube Shorts algorithm.
        """
        prompts = [
            f"👇 Honest opinion: Did {rank1_name} deserve the #1 spot, or who got robbed? Drop your top 3! 🔥",
            f"👀 Who has MORE aura than {rank1_name}? Tell me below and I'll pin the best comment! 📌",
            f"⚡ Be honest... which rank gave you the most goosebumps? 1, 2, 3, 4, or 5? 👇",
            f"🔥 Subscribe if your favorite made the list! Who should be in Part 2? 🎬"
        ]
        return random.choice(prompts)

    def assemble_boosted_metadata(
        self,
        video_path: str,
        target_name: str,
        group_type: str = "GROUP_A",
        rank1_char: str = "",
        custom_hook: str = ""
    ) -> Dict[str, Any]:
        """
        Main workflow execution: produces the complete package for YouTube release.
        """
        timing = self.calculate_best_upload_schedule()
        title = custom_hook or self.generate_viral_curiosity_title(target_name, group_type, rank1_char)
        pinned_comment = self.generate_pinned_comment_bait(target_name, rank1_char or "Rank #1")

        # Combine specific target keywords with unrelated mega-traffic keywords
        boost_tags = [target_name.lower(), f"{target_name.lower()} edit", f"{target_name.lower()} ranking"]
        boost_tags.extend(UNRELATED_BOOST_KEYWORDS)
        # Unique preserving order, keeping total characters strictly within YouTube limit (< 400 chars)
        seen_tags = set()
        final_tags = []
        curr_tag_len = 0
        for t in boost_tags:
            clean_t = t.replace("<", "").replace(">", "").strip()
            if clean_t and clean_t not in seen_tags:
                if curr_tag_len + len(clean_t) + 1 <= 380 and len(final_tags) < 25:
                    seen_tags.add(clean_t)
                    final_tags.append(clean_t)
                    curr_tag_len += len(clean_t) + 1

        # Assemble multi-tier viral hashtag stack: Core Anime + Random Live Viral + Unrelated Mega Niches
        live_scraped_tags = self.probe_live_trending_hashtags()
        random_unrelated_sample = random.sample(UNRELATED_VIRAL_NICHE_HASHTAGS, min(8, len(UNRELATED_VIRAL_NICHE_HASHTAGS)))

        combined_hashtags = []
        for tag_list in [TRENDING_HASHTAG_STACK, live_scraped_tags, random_unrelated_sample]:
            for t in tag_list:
                if t.lower() not in [x.lower() for x in combined_hashtags]:
                    combined_hashtags.append(t)

        hashtags_str = " ".join(combined_hashtags)

        # High-retention SEO description with disclaimer and keyword cloud
        description = f"""{title}

Rankings & Clips featured in this video:
🔥 {target_name} • Full 4K 60FPS Experience

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💬 JOIN THE DISCUSSION:
{pinned_comment}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ COPYRIGHT & FAIR-USE NOTICE:
I do not own the anime, footage, or music featured in this video. All rights, credits, and intellectual property belong entirely to their respective original owners, authors, animation studios, and production committees. 

This video is created under Fair Use (Section 107 of the Copyright Act 1976) for purposes of entertainment, criticism, review, and transformative commentary.

📩 URGENT REMOVAL REQUEST / BUSINESS INQUIRIES:
If you are the legal copyright holder or creator of any content used in this video and want it immediately removed, PLEASE DO NOT STRIKE THE CHANNEL. 
Kindly contact me directly at:
👉 animefandom8866@gmail.com
I will respectfully review and delete/remove the video within 24 hours.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔔 SUBSCRIBE to @animefandom0_0 for daily 4K anime edits, viral rankings, and cold moments!

{hashtags_str}
"""

        package = {
            "video_path": video_path,
            "title": title[:100],
            "description": description,
            "tags": final_tags,
            "scheduled_utc": timing["scheduled_utc"],
            "scheduled_utc_iso": timing["scheduled_utc_iso"],
            "scheduled_ist": timing["scheduled_ist_str"],
            "timing_strategy": timing["strategy"],
            "pinned_comment": pinned_comment,
            "free_boost_methods": [
                "1. Comment Section Catalyst (Pinned debate question drives high engagement velocity)",
                "2. Cross-Anime SEO Injection (High-traffic tags index the short next to viral JJK, One Piece, and Solo Leveling videos)",
                "3. Strategic Prime-Time Scheduling (7:30 PM IST captures multi-continent peak viewership)",
                "4. 100-Second Infinite Retention Hook (Clean #1 badge keeps viewers watching until the very end)"
            ]
        }
        return package

if __name__ == "__main__":
    booster = ViralGrowthBoosterWorkflow()
    sample_pkg = booster.assemble_boosted_metadata(
        video_path="output/auto_group_a_macro_disrespect_master.mp4",
        target_name="Most Disrespectful Anime Cold Moments",
        group_type="GROUP_A",
        rank1_char="Meruem"
    )
    print("\n=======================================================")
    print("🚀 VIRAL GROWTH BOOSTER WORKFLOW OUTPUT")
    print("=======================================================")
    print(f"Title: {sample_pkg['title']}")
    print(f"Scheduled: {sample_pkg['scheduled_ist']} ({sample_pkg['scheduled_utc_iso']})")
    print(f"Pinned Comment Bait:\n{sample_pkg['pinned_comment']}")
    print(f"\nTags ({len(sample_pkg['tags'])}):\n{', '.join(sample_pkg['tags'][:10])}...")
    print(f"\nFree Boost Techniques Applied:\n" + "\n".join(sample_pkg['free_boost_methods']))
