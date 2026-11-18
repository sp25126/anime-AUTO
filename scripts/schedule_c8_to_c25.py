#!/usr/bin/env python3
"""
Batch Uploader & Scheduler for Group C: C8 through C25
Channel: @animefandom0_0
Uploads all rendered Group C masters (C8-C25), applies ViralGrowthBooster metadata,
schedules them into open queue slots, and records them in config/scheduled_upload_registry.json.
"""

import os
import sys
import json
import datetime
from pathlib import Path
import googleapiclient.discovery
import google.oauth2.credentials
from googleapiclient.http import MediaFileUpload

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WORKSPACE_ROOT / "scripts" / "engine"))
from viral_growth_booster import ViralGrowthBoosterWorkflow

CONFIG_DIR = WORKSPACE_ROOT / "config"
TOKEN_FILE = CONFIG_DIR / "youtube_token.json"
REGISTRY_FILE = CONFIG_DIR / "scheduled_upload_registry.json"

TARGETS_C8_TO_C25 = [
    {
        "id": "c8",
        "key": "moment_underdog_silences_crowd",
        "file": "output/auto_group_c8_underdog_silences_crowd_master.mp4",
        "anime": "Black Clover",
        "creator": "@BlackCloverClips",
        "theme": "The Underdog Silences The Entire Crowd",
        "hook": "The Entire Stadium Went Dead Silent In 3 Seconds 💀 | Black Clover #shorts #anime"
    },
    {
        "id": "c9",
        "key": "moment_menacing_presence_walk",
        "file": "output/auto_group_c9_menacing_presence_walk_master.mp4",
        "anime": "Solo Leveling",
        "creator": "@SoloLevelingHub",
        "theme": "The Unstoppable Walking Hazard Presence",
        "hook": "Bro's Presence Alone Made Them Drop Their Weapons 🥶 | Solo Leveling #shorts #anime"
    },
    {
        "id": "c10",
        "key": "moment_instant_technique_copy",
        "file": "output/auto_group_c10_instant_technique_copy_master.mp4",
        "anime": "Fate Series",
        "creator": "@FateSakuga",
        "theme": "The Instant Master Technique Copy Flex",
        "hook": "He Saw It ONCE And Perfected It Instantly ⚡ | Fate Series #shorts #anime"
    },
    {
        "id": "c11",
        "key": "moment_heartbreaking_body_shield",
        "file": "output/auto_group_c11_heartbreaking_body_shield_master.mp4",
        "anime": "Demon Slayer",
        "creator": "@DemonSlayerVibes",
        "theme": "The Heartbreaking Sacrificial Body Shield",
        "hook": "His Body Moved On Its Own... 💔😭 | Demon Slayer #shorts #anime"
    },
    {
        "id": "c12",
        "key": "moment_mascot_true_form_reveal",
        "file": "output/auto_group_c12_mascot_true_form_reveal_master.mp4",
        "anime": "Dandadan",
        "creator": "@DandadanDaily",
        "theme": "Harmless Pet Unleashes Colossal True Form",
        "hook": "They Thought It Was A Cute Pet Until It Transformed 😱 | Dandadan #shorts #anime"
    },
    {
        "id": "c13",
        "key": "moment_touch_them_and_die",
        "file": "output/auto_group_c13_touch_them_and_die_master.mp4",
        "anime": "Mob Psycho 100",
        "creator": "@MobPsychoEdits",
        "theme": "The 'You Hurt My Loved One' Death Warrant",
        "hook": "The Single Biggest Mistake In Anime History 💀 | Mob Psycho 100 #shorts #anime"
    },
    {
        "id": "c14",
        "key": "moment_stare_of_pure_death",
        "file": "output/auto_group_c14_stare_of_pure_death_master.mp4",
        "anime": "Vinland Saga",
        "creator": "@VinlandSagaHub",
        "theme": "The Stare That Took 10 Years Off His Life",
        "hook": "That One Stare Took 10 Years Off His Life 🥶 | Vinland Saga #shorts #anime"
    },
    {
        "id": "c15",
        "key": "moment_genius_bluff_success",
        "file": "output/auto_group_c15_genius_bluff_success_master.mp4",
        "anime": "One Piece",
        "creator": "@OnePieceShorts",
        "theme": "The 0% Plan, 100% Confidence Master Bluff",
        "hook": "0% Plan, But 100% Confidence and It WORKED 😂 | One Piece #shorts #anime"
    },
    {
        "id": "c16",
        "key": "moment_standing_on_pure_willpower",
        "file": "output/auto_group_c16_standing_on_pure_willpower_master.mp4",
        "anime": "Berserk",
        "creator": "@BerserkLegacy",
        "theme": "The Undefeated Stand on Pure Willpower",
        "hook": "Even In Death, He Refused To Fall 👑 | Berserk #shorts #anime"
    },
    {
        "id": "c17",
        "key": "moment_holding_back_percentage_reveal",
        "file": "output/auto_group_c17_holding_back_percentage_reveal_master.mp4",
        "anime": "Frieren: Beyond Journey's End",
        "creator": "@FrierenClips",
        "theme": "The 'That Was Only 10% Power' Reality Drop",
        "hook": "He Thought They Were Equal Until Bro Dropped This Line 🥶 | Frieren #shorts #anime"
    },
    {
        "id": "c18",
        "key": "moment_cold_blood_revenge_execution",
        "file": "output/auto_group_c18_cold_blood_revenge_execution_master.mp4",
        "anime": "Tokyo Ghoul",
        "creator": "@TokyoGhoulZone",
        "theme": "The Cold-Blooded No-Mercy Revenge Execution",
        "hook": "Bro Did Not Let Him Finish His Villain Monologue 💀 | Tokyo Ghoul #shorts #anime"
    },
    {
        "id": "c19",
        "key": "moment_weapon_awakening_release",
        "file": "output/auto_group_c19_weapon_awakening_release_master.mp4",
        "anime": "Bleach TYBW",
        "creator": "@BleachSakuga",
        "theme": "First Legendary Weapon / Shikai Unsheathing",
        "hook": "The Sky Changed Color When He Unsheathed This Blade ⚔️ | Bleach #shorts #anime"
    },
    {
        "id": "c20",
        "key": "moment_unspoken_mutual_respect",
        "file": "output/auto_group_c20_unspoken_mutual_respect_master.mp4",
        "anime": "Jujutsu Kaisen",
        "creator": "@JJKMoments",
        "theme": "The Unspoken Nod of Two Peak Monsters",
        "hook": "When Two Monsters Acknowledge Each Other Without A Word 🤝 | Jujutsu Kaisen #shorts"
    },
    {
        "id": "c21",
        "key": "moment_cold_indifference_walkaway",
        "file": "output/auto_group_c21_cold_indifference_walkaway_master.mp4",
        "anime": "Fire Force",
        "creator": "@FireForceOfficial",
        "theme": "Cold Indifference Walkaway / Utter Disregard",
        "hook": "Bro Walked Away Before The Attack Even Landed 💀 | Fire Force #shorts #anime"
    },
    {
        "id": "c22",
        "key": "moment_villain_apologizes_in_terror",
        "file": "output/auto_group_c22_villain_apologizes_in_terror_master.mp4",
        "anime": "Solo Leveling",
        "creator": "@SoloLevelingAura",
        "theme": "Arrogant Villain Apologizes In Pure Terror",
        "hook": "The Exact Second The Villain Realized He Was Cooked 😭 | Solo Leveling #shorts #anime"
    },
    {
        "id": "c23",
        "key": "moment_one_finger_block_shock",
        "file": "output/auto_group_c23_one_finger_block_shock_master.mp4",
        "anime": "Fate Series",
        "creator": "@FateAnimeHub",
        "theme": "The Effortless One-Finger Block Humiliation",
        "hook": "He Stopped Their Strongest Attack With ONE FINGER 😱 | Fate Series #shorts #anime"
    },
    {
        "id": "c24",
        "key": "moment_battle_iq_counter_trap",
        "file": "output/auto_group_c24_battle_iq_counter_trap_master.mp4",
        "anime": "Naruto Shippuden",
        "creator": "@NarutoShippudenHub",
        "theme": "The 200 IQ Reverse Counter Trap",
        "hook": "Bro Calculated This 50 Moves Ahead 🧠⚡ | Naruto Shippuden #shorts #anime"
    },
    {
        "id": "c25",
        "key": "moment_unhinged_english_dub_masterpiece",
        "file": "output/auto_group_c25_unhinged_english_dub_masterpiece_master.mp4",
        "anime": "Dandadan",
        "creator": "@AnimeDubClips",
        "theme": "Unhinged / Out-of-Pocket English Dub Delivery",
        "hook": "The English Dub Voice Actors Had ZERO Chill Here 😭💀 | Dandadan #shorts #anime"
    }
]

def get_channel_and_service():
    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        creds_data = json.load(f)
    creds = google.oauth2.credentials.Credentials.from_authorized_user_info(creds_data)
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)
    ch_res = youtube.channels().list(part="snippet", mine=True).execute()
    title = ch_res["items"][0]["snippet"]["title"]
    print(f"Authenticated Channel: {title}")
    return youtube

def load_registry():
    if REGISTRY_FILE.exists():
        with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_registry(data):
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

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

    now_utc = datetime.datetime.now(datetime.timezone.utc)
    if scheduled_dates:
        latest_scheduled = max(scheduled_dates)
        next_date = (latest_scheduled + datetime.timedelta(days=1)).replace(hour=2, minute=0, second=0, microsecond=0)
    else:
        next_date = (now_utc + datetime.timedelta(days=1)).replace(hour=2, minute=0, second=0, microsecond=0)

    if next_date <= now_utc:
        next_date = (now_utc + datetime.timedelta(days=1)).replace(hour=2, minute=0, second=0, microsecond=0)

    return next_date

def main():
    print("=" * 70)
    print("🚀 BATCH SCHEDULER: GROUP C (C8 THROUGH C25)")
    print("=" * 70)

    youtube = get_channel_and_service()
    booster = ViralGrowthBoosterWorkflow()
    registry = load_registry()

    next_slot = get_next_available_slot(youtube)
    print(f"Initial Open Release Slot: {next_slot.isoformat()} ({(next_slot + datetime.timedelta(hours=5, minutes=30)).strftime('%Y-%m-%d %I:%M %p IST')})\n")

    uploaded_count = 0
    total = len(TARGETS_C8_TO_C25)

    for idx, item in enumerate(TARGETS_C8_TO_C25, 1):
        file_path = str(WORKSPACE_ROOT / item["file"])
        if not os.path.exists(file_path):
            print(f"[{idx}/{total}] ⚠️ Master not found on disk: {file_path}, skipping.")
            continue

        if file_path in registry and registry[file_path].get("status") == "uploaded":
            print(f"[{idx}/{total}] ⏩ Already uploaded: {Path(file_path).name} (ID: {registry[file_path].get('video_id')})")
            continue

        print(f"[{idx}/{total}] 📦 Preparing {Path(file_path).name}...")
        package = booster.assemble_boosted_metadata(
            video_path=file_path,
            target_name=item["anime"],
            group_type="GROUP_C",
            custom_hook=item["hook"]
        )

        current_scheduled_slot = next_slot
        next_slot = next_slot + datetime.timedelta(days=1)

        pub_iso = current_scheduled_slot.isoformat()
        ist_str = (current_scheduled_slot + datetime.timedelta(hours=5, minutes=30)).strftime("%Y-%m-%d %I:%M %p IST")

        print(f"   Title: {package['title']}")
        print(f"   Schedule Slot: {ist_str} ({pub_iso})")
        print(f"   Uploading binary ({round(os.path.getsize(file_path)/(1024*1024), 2)} MB)...")

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
                "format": "GROUP_C",
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
