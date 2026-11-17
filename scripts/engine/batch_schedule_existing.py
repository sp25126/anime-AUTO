import os
import sys
import json
import random
import datetime
from pathlib import Path
import googleapiclient.discovery
import google.oauth2.credentials
from googleapiclient.http import MediaFileUpload

# Inject script engine directory to import viral_growth_booster
sys.path.insert(0, str(Path(__file__).resolve().parent / "engine"))
from viral_growth_booster import ViralGrowthBoosterWorkflow

CONFIG_DIR = Path("config")
TOKEN_FILE = CONFIG_DIR / "youtube_token.json"
STATE_FILE = CONFIG_DIR / "scheduled_upload_registry.json"

MASTER_CATALOG = [
    # GROUP A - 100s Compilations
    {
        "file": "output/auto_group_a_macro_aura_master.mp4",
        "format": "GROUP_A",
        "theme": "Coldest Anime Aura Walks & Battle Strolls",
        "rank1": "Aizen / Sukuna",
        "hook": "Top 5 Coldest Anime Aura Walks In History! 💀🥶 #shorts #anime"
    },
    {
        "file": "output/auto_group_a_macro_beat_drop_master.mp4",
        "format": "GROUP_A",
        "theme": "Hardest Anime Phonk Beat Drops",
        "rank1": "Toji / Sung Jin-Woo",
        "hook": "Top 5 Insane Anime Phonk Beat Drops That Hit Different! 🔊⚡ #shorts #animeedit"
    },
    {
        "file": "output/auto_group_a_macro_disrespect_master.mp4",
        "format": "GROUP_A",
        "theme": "Most Disrespectful Anime Moments",
        "rank1": "Meruem / Escanor",
        "hook": "Rank #1 Broke The Entire Internet! 🔥💀 (Top 5 Disrespect Moments) #shorts"
    },
    {
        "file": "output/auto_group_a_macro_fights_master.mp4",
        "format": "GROUP_A",
        "theme": "Insane Sakuga Clashes & Martial Arts",
        "rank1": "Kakashi vs Obito",
        "hook": "Top 5 Insane Sakuga Clashes Ranked From #5 To #1! ⚔️💥 #shorts #anime"
    },
    {
        "file": "output/auto_group_a_macro_rage_master.mp4",
        "format": "GROUP_A",
        "theme": "Pure Uncut Anime Rage Awakenings",
        "rank1": "Adult Gon / Mob",
        "hook": "Nobody Expected Rank #1 To Do That... 😱⚡ (Top 5 Pure Rage Snaps) #shorts"
    },
    {
        "file": "output/auto_group_a_macro_speed_master.mp4",
        "format": "GROUP_A",
        "theme": "Fastest Anime Speedsters & Blitzes",
        "rank1": "Minato Flying Raijin",
        "hook": "Top 5 Fastest Speed Blitzes In Anime! ⚡💨 #shorts #anime"
    },
    {
        "file": "output/auto_group_a_macro_sword_draws_master.mp4",
        "format": "GROUP_A",
        "theme": "Badass Anime Katana Draws & Scabbard Clicks",
        "rank1": "Zoro / Zenitsu",
        "hook": "Top 5 Badass Anime Katana Draws With Insane Sound Design! 🗡️✨ #shorts"
    },
    {
        "file": "output/auto_group_a_macro_transformations_master.mp4",
        "format": "GROUP_A",
        "theme": "God-Tier Anime Transformations",
        "rank1": "Goku UI / Luffy Gear 5",
        "hook": "Rank #1 Broke The Whole Animation Budget! 🔥⚡ (Top 5 Transformations) #shorts"
    },
    {
        "file": "output/auto_group_a_macro_villains_master.mp4",
        "format": "GROUP_A",
        "theme": "Coldest Anime Villain Dominance",
        "rank1": "Pain / Madara",
        "hook": "Top 5 Coldest Anime Villains Ranked By Pure Aura! 👑🥶 #shorts #anime"
    },
    {
        "file": "output/auto_group_a_micro_naruto_master.mp4",
        "format": "GROUP_A",
        "theme": "Naruto Shippuden Peak Climax Moments",
        "rank1": "Madara Meteor Drop",
        "hook": "Top 5 Coldest Naruto Shippuden Moments Ranked! 🍥🔥 #shorts #naruto"
    },
    # GROUP B - 30s Rotate Your Phone
    {
        "file": "output/auto_group_b1_phonk_velocity_master.mp4",
        "format": "GROUP_B",
        "theme": "Anime Phonk Velocity AMV",
        "rank1": "Speed Ramp Drop",
        "hook": "ROTATE YOUR PHONE for Maximum Chills! 📱🔄⚡ (Phonk Velocity) #shorts #animeedit"
    },
    {
        "file": "output/auto_group_b2_orchestral_reboot_master.mp4",
        "format": "GROUP_B",
        "theme": "Memory Reboot Timeless Guitar AMV",
        "rank1": "Demon Slayer Cinema",
        "hook": "ROTATE YOUR PHONE for Goosebumps! 📱🔄✨ (Memory Reboot Peak Cinema) #shorts"
    },
    {
        "file": "output/auto_group_b3_sakuga_clash_master.mp4",
        "format": "GROUP_B",
        "theme": "Sakuga Clashes Fullscreen AMV",
        "rank1": "Martial Arts Climax",
        "hook": "ROTATE YOUR PHONE For 60FPS Sakuga Clashes! 📱🔄⚔️ #shorts #anime"
    },
    {
        "file": "output/auto_group_b4_transformation_master.mp4",
        "format": "GROUP_B",
        "theme": "God-Tier Transformation Fullscreen AMV",
        "rank1": "Goku Ultra Instinct",
        "hook": "ROTATE YOUR PHONE For God-Tier Transformations! 📱🔄🔥 #shorts #animeedit"
    },
    {
        "file": "output/auto_group_b5_villain_aura_master.mp4",
        "format": "GROUP_B",
        "theme": "Coldest Villain Aura Fullscreen AMV",
        "rank1": "Sosuke Aizen / Ryomen Sukuna",
        "hook": "ROTATE YOUR PHONE for Unshakeable Villain Aura! 📱🔄👑 #shorts #anime"
    },
    {
        "file": "output/auto_group_b6_sword_draw_master.mp4",
        "format": "GROUP_B",
        "theme": "Katana Draws & Scabbard Clicks Fullscreen AMV",
        "rank1": "Zenitsu Thunderclap / Zoro",
        "hook": "ROTATE YOUR PHONE for Satisfying Katana Draws! 📱🔄🗡️ #shorts #animeedit"
    },
    {
        "file": "output/auto_group_b7_rage_snap_master.mp4",
        "format": "GROUP_B",
        "theme": "Anime Rage Snaps Fullscreen AMV",
        "rank1": "Adult Gon / Naruto 6 Tails",
        "hook": "ROTATE YOUR PHONE for Pure Anime Rage Snaps! 📱🔄😡⚡ #shorts #anime"
    },
    {
        "file": "output/auto_group_b8_speed_blitz_master.mp4",
        "format": "GROUP_B",
        "theme": "Speed Blitz Velocity Fullscreen AMV",
        "rank1": "Minato Flying Raijin / Killua",
        "hook": "ROTATE YOUR PHONE for High-Velocity Speed Blitz! 📱🔄⚡💨 #shorts #anime"
    },
    {
        "file": "output/auto_group_b9_domain_expansion_master.mp4",
        "format": "GROUP_B",
        "theme": "Domain Expansion Fullscreen AMV",
        "rank1": "Gojo Infinite Void / Sukuna",
        "hook": "ROTATE YOUR PHONE for Peak Domain Expansions! 📱🔄🔮 #shorts #jjk"
    },
    {
        "file": "output/auto_group_b10_single_franchise_master.mp4",
        "format": "GROUP_B",
        "theme": "Solo Leveling Sung Jin-Woo Fullscreen AMV",
        "rank1": "Arise Shadow Monarch",
        "hook": "ROTATE YOUR PHONE for Sung Jin-Woo Shadow Monarch! 📱🔄👑⚡ #shorts #sololeveling"
    },
    # GROUP C - Micro Moments
    {
        "file": "output/auto_group_c1_accidental_rizz_master.mp4",
        "format": "GROUP_C",
        "theme": "Accidental Rizz - Jinshi & Maomao",
        "rank1": "Jinshi Frog Scene",
        "hook": "Bro Really Said That With A Straight Face 😭💀 | Accidental Rizz #shorts #anime"
    },
    {
        "file": "output/auto_group_c2_tsundere_blush_master.mp4",
        "format": "GROUP_C",
        "theme": "Tsundere Blush - Kaguya-sama Iino Miko",
        "rank1": "Iino Toyed With",
        "hook": "She Thought She Was In Control But Blushed So Hard 😭💀 #shorts #animeedit"
    }
]

def load_registry():
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_registry(registry):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

def get_channel_and_service():
    if not TOKEN_FILE.exists():
        raise FileNotFoundError(f"Missing {TOKEN_FILE}")
    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        creds_data = json.load(f)
    creds = google.oauth2.credentials.Credentials.from_authorized_user_info(creds_data)
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)
    return youtube

def get_next_available_slot(youtube):
    channels = youtube.channels().list(part="contentDetails", mine=True).execute()
    uploads_playlist_id = channels["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    items_res = youtube.playlistItems().list(part="snippet", playlistId=uploads_playlist_id, maxResults=50).execute()
    vid_ids = [item["snippet"]["resourceId"]["videoId"] for item in items_res.get("items", [])]

    scheduled_dates = []
    if vid_ids:
        vids_res = youtube.videos().list(part="snippet,status", id=",".join(vid_ids)).execute()
        for v in vids_res.get("items", []):
            st = v["status"]
            pub_at = st.get("publishAt")
            if pub_at:
                dt = datetime.datetime.fromisoformat(pub_at.replace("Z", "+00:00"))
                scheduled_dates.append(dt)

    # Base target: 7:30 PM IST = 14:00 UTC
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    if scheduled_dates:
        latest_scheduled = max(scheduled_dates)
        next_date = (latest_scheduled + datetime.timedelta(days=1)).replace(hour=14, minute=0, second=0, microsecond=0)
    else:
        next_date = (now_utc + datetime.timedelta(days=1)).replace(hour=14, minute=0, second=0, microsecond=0)

    if next_date <= now_utc:
        next_date = (now_utc + datetime.timedelta(days=1)).replace(hour=14, minute=0, second=0, microsecond=0)

    return next_date

def main():
    print("=" * 70)
    print("🚀 BATCH SCHEDULING ALL RENDERED MASTERS TO YOUTUBE QUEUE")
    print("=" * 70)

    youtube = get_channel_and_service()
    booster = ViralGrowthBoosterWorkflow()
    registry = load_registry()

    next_slot = get_next_available_slot(youtube)
    print(f"Initial Open Release Slot: {next_slot.isoformat()} ({(next_slot + datetime.timedelta(hours=5, minutes=30)).strftime('%Y-%m-%d %I:%M %p IST')})\n")

    uploaded_count = 0
    total_to_process = len(MASTER_CATALOG)

    for idx, item in enumerate(MASTER_CATALOG, 1):
        file_path = item["file"]
        if not os.path.exists(file_path):
            print(f"[{idx}/{total_to_process}] ⚠️ File missing on disk: {file_path}, skipping.")
            continue

        if file_path in registry and registry[file_path].get("status") == "uploaded":
            print(f"[{idx}/{total_to_process}] ⏩ Already uploaded: {file_path} (ID: {registry[file_path].get('video_id')})")
            continue

        print(f"[{idx}/{total_to_process}] 📦 Preparing {Path(file_path).name}...")
        package = booster.assemble_boosted_metadata(
            video_path=file_path,
            target_name=item["theme"],
            group_type=item["format"],
            rank1_char=item["rank1"],
            custom_hook=item["hook"]
        )

        current_scheduled_slot = next_slot
        next_slot = next_slot + datetime.timedelta(days=1)

        pub_iso = current_scheduled_slot.isoformat()
        ist_str = (current_scheduled_slot + datetime.timedelta(hours=5, minutes=30)).strftime("%Y-%m-%d %I:%M %p IST")

        print(f"   Title: {package['title']}")
        print(f"   Schedule Slot: {ist_str} ({pub_iso})")
        print(f"   Uploading video binary ({round(os.path.getsize(file_path)/(1024*1024), 2)} MB)...")

        body = {
            "snippet": {
                "title": package["title"][:100],
                "description": package["description"],
                "tags": package["tags"],
                "categoryId": "24" # Entertainment
            },
            "status": {
                "privacyStatus": "private",
                "publishAt": pub_iso,
                "selfDeclaredMadeForKids": False
            }
        }

        media = MediaFileUpload(file_path, mimetype="video/mp4", resumable=True, chunksize=1024*1024*10)
        request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)

        try:
            response = None
            while response is None:
                status, response = request.next_chunk()
                if status:
                    print(f"   Uploaded {int(status.progress() * 100)}%...")
            video_id = response.get("id")
            print(f"   ✅ SUCCESS! Video Scheduled with ID: {video_id}")
            print(f"   URL: https://youtu.be/{video_id}")

            registry[file_path] = {
                "status": "uploaded",
                "video_id": video_id,
                "title": package["title"],
                "scheduled_slot_utc": pub_iso,
                "scheduled_slot_ist": ist_str,
                "format": item["format"],
                "theme": item["theme"],
                "uploaded_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
            }
            save_registry(registry)
            uploaded_count += 1

        except Exception as e:
            print(f"   ❌ UPLOAD ERROR: {e}")
            if "quotaExceeded" in str(e) or "dailyUploadLimitExceeded" in str(e):
                print("   🚨 YouTube API Upload Quota / Daily Limit reached! Stopping batch gracefully.")
                break

    print("\n" + "=" * 70)
    print(f"🎉 BATCH COMPLETE: {uploaded_count} new video(s) scheduled in YouTube queue.")
    print("=" * 70)

if __name__ == "__main__":
    main()
