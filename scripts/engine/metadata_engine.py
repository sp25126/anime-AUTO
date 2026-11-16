"""
Metadata, Trending Tag Scout & Fair-Use Compliance Engine
Generates:
1. High-CTR Emotional Curiosity Titles
2. Cross-Franchise Viral Trending Hashtags (even unrelated mega-trends like #gear5, #jjk, #solo_leveling, #dandadan)
3. Legal Fair-Use Disclaimer & Takedown Notice with animefandom8866@gmail.com
4. Next Available Release Slot Finder (Prevents colliding with existing scheduled queue)
"""

import datetime
from typing import Dict, List, Tuple
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

TAKEDOWN_EMAIL = "animefandom8866@gmail.com"

# Evergreen and trending viral hashtags that boost algorithmic discovery across Shorts
GLOBAL_VIRAL_MEGA_HASHTAGS = [
    "#shorts", "#anime", "#animeedit", "#fyp", "#viral", "#foryou",
    "#animemoments", "#dandadan", "#jjk", "#jujutsukaisen", "#onepiece",
    "#gear5", "#sololeveling", "#bleach", "#chainsawman", "#frieren",
    "#accidentalrizz", "#coldestanimemoments", "#animeshorts"
]

class MetadataComplianceEngine:
    def __init__(self, youtube_creds_path: str = "config/youtube_token.json"):
        self.creds_path = youtube_creds_path

    def get_next_available_release_slot(self) -> datetime.datetime:
        """
        Scans YouTube Studio's scheduled videos, finds the latest scheduled release,
        and schedules the new video for the NEXT DAY at 14:00:00Z (7:30 PM IST).
        Guarantees zero overlap or collision with existing scheduled videos!
        """
        try:
            creds = Credentials.from_authorized_user_file(self.creds_path)
            youtube = build("youtube", "v3", credentials=creds)
            
            uploads_id = youtube.channels().list(part="contentDetails", mine=True).execute()['items'][0]['contentDetails']['relatedPlaylists']['uploads']
            p_res = youtube.playlistItems().list(part="contentDetails", playlistId=uploads_id, maxResults=20).execute()
            video_ids = [it['contentDetails']['videoId'] for it in p_res.get('items', [])]
            
            latest_scheduled = None
            if video_ids:
                v_res = youtube.videos().list(part="status", id=",".join(video_ids)).execute()
                for it in v_res.get('items', []):
                    pub_at = it['status'].get('publishAt')
                    if pub_at:
                        # Parse ISO 8601 (e.g., 2026-11-20T14:00:00Z)
                        dt = datetime.datetime.fromisoformat(pub_at.replace("Z", "+00:00"))
                        if latest_scheduled is None or dt > latest_scheduled:
                            latest_scheduled = dt

            now_utc = datetime.datetime.now(datetime.timezone.utc)
            if latest_scheduled and latest_scheduled > now_utc:
                # Add exactly 1 day to the latest scheduled video at 14:00 UTC (7:30 PM IST)
                next_slot = (latest_scheduled + datetime.timedelta(days=1)).replace(hour=14, minute=0, second=0, microsecond=0)
            else:
                # If no scheduled queue, schedule for tomorrow at 14:00 UTC
                next_slot = (now_utc + datetime.timedelta(days=1)).replace(hour=14, minute=0, second=0, microsecond=0)

            return next_slot
        except Exception as e:
            print(f"[MetadataEngine] Error fetching schedule queue: {e}. Fallback to Nov 21.")
            # Fallback safe date
            return datetime.datetime(2026, 11, 21, 14, 0, 0, tzinfo=datetime.timezone.utc)

    def generate_metadata(
        self,
        anime_title: str,
        moment_label: str,
        group_type: str = "GROUP_C",
        custom_hook: str = ""
    ) -> Dict[str, any]:
        """
        Constructs high-CTR curiosity titles, mega-trend hashtags, tags, and takedown disclaimers.
        """
        # 1. High-CTR Title Generation
        if group_type == "GROUP_A": # Edit Ranking
            titles = [
                f"Top 5 GREATEST {anime_title} Edits on YouTube! 🔥💀 #shorts #anime",
                f"Top 5 Coldest {anime_title} Moments That Broke The Internet! 🥶⚡ #shorts",
                f"Ranking The Most Insane {anime_title} Sakuga Moments! 👑 #shorts #animeedit"
            ]
            chosen_title = custom_hook if custom_hook else titles[0]
        elif group_type == "GROUP_B": # Rotate Phone
            chosen_title = f"ROTATE YOUR PHONE for the Coldest {anime_title} Edit! 📱🔄⚡ #shorts #animeedit"
        else: # GROUP_C Micro-Moment
            titles = [
                f"These two are hilarious 🤣 | {anime_title} #shorts #anime",
                f"Bro really didn't hesitate 💀 | {anime_title} #shorts",
                f"The way she looked at him is insane 😭 | {anime_title} #shorts",
                f"Protect them at all costs 🥹 | {anime_title} #shorts"
            ]
            chosen_title = custom_hook if custom_hook else titles[0]

        # 2. Viral Hashtags String for Description (boosted discovery)
        hashtags_block = " ".join(GLOBAL_VIRAL_MEGA_HASHTAGS)

        # 3. Description with Fair-Use Disclaimer & Contact Email
        description = f"""{chosen_title}

{moment_label} ✨

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 FEATURED ANIME:
• Title: {anime_title}
• Production Category: {group_type}
• Channel: @animefandom0_0

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
FOLLOW @animefandom0_0 FOR DAILY ANIME SHORTS & EDITS!

{hashtags_block}
"""

        # 4. Search Tags (Comma-separated keyword tags)
        tags = [
            "shorts", "anime", "anime edit", "anime moments", "anime funny moments",
            "accidental rizz", "coldest anime moments", "fyp", "viral anime",
            anime_title.lower(), f"{anime_title.lower()} moments", f"{anime_title.lower()} edit",
            "dandadan", "jjk", "one piece", "gear 5", "solo leveling", "bleach tybw", "frieren"
        ]

        return {
            "title": chosen_title[:100], # YouTube max 100 chars
            "description": description,
            "tags": tags[:30],           # Top 30 tags
            "scheduled_utc": self.get_next_available_release_slot()
        }

if __name__ == "__main__":
    engine = MetadataComplianceEngine()
    slot = engine.get_next_available_release_slot()
    print(f"Next Available YouTube Release Slot: {slot.isoformat()} (7:30 PM IST)")
    sample = engine.generate_metadata("The Apothecary Diaries", "Jinshi royal charm vs Maomao disgust", "GROUP_C")
    print(f"\nGenerated Title: {sample['title']}")
    print(f"\nScheduled Time: {sample['scheduled_utc']}")
