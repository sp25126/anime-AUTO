import os
import sys
import json
import datetime
from pathlib import Path
import googleapiclient.discovery
import google.oauth2.credentials
from googleapiclient.http import MediaFileUpload

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(WORKSPACE_ROOT))
sys.path.insert(0, str(WORKSPACE_ROOT / "scripts" / "engine"))

from viral_growth_booster import ViralGrowthBoosterWorkflow

CONFIG_DIR = WORKSPACE_ROOT / "config"
TOKEN_FILE = CONFIG_DIR / "youtube_token.json"
REGISTRY_FILE = CONFIG_DIR / "scheduled_upload_registry.json"

# The 5 vacant slots freed by deleting the blocked videos:
# 2026-11-23T14:00:00Z | 2026-11-23 07:30 PM IST
# 2026-11-26T14:00:00Z | 2026-11-26 07:30 PM IST
# 2026-11-29T14:00:00Z | 2026-11-29 07:30 PM IST
# 2026-12-01T14:00:00Z | 2026-12-01 07:30 PM IST
# 2026-12-07T14:00:00Z | 2026-12-07 07:30 PM IST

REPLACEMENT_TARGETS = [
    {
        "slot_utc": "2026-11-23T14:00:00Z",
        "slot_ist": "2026-11-23 07:30 PM IST",
        "file": "output/auto_group_c3_brutal_reality_check_master.mp4",
        "format": "GROUP_C",
        "theme": "The Brutal Reality Check / Arrogance Crushed",
        "hook": "The Exact Second He Realized He Messed Up 💀 | Brutal Reality Check #shorts #anime"
    },
    {
        "slot_utc": "2026-11-26T14:00:00Z",
        "slot_ist": "2026-11-26 07:30 PM IST",
        "file": "output/auto_group_c4_character_rage_snap_master.mp4",
        "format": "GROUP_C",
        "theme": "When The Gentle Character Finally Snaps",
        "hook": "The Moment The Calm Character Finally Snapped 😱⚡ | Rage Snap #shorts #anime"
    },
    {
        "slot_utc": "2026-11-29T14:00:00Z",
        "slot_ist": "2026-11-29 07:30 PM IST",
        "file": "output/auto_group_c5_cold_verbal_violation_master.mp4",
        "format": "GROUP_C",
        "theme": "Coldest Verbal Disrespect & One-Liners",
        "hook": "Bro Didn't Have To Disrespect Him Like That 😭💀 | Verbal Violation #shorts #anime"
    },
    {
        "slot_utc": "2026-12-01T14:00:00Z",
        "slot_ist": "2026-12-01 07:30 PM IST",
        "file": "output/auto_group_c6_clutch_savior_arrival_master.mp4",
        "format": "GROUP_C",
        "theme": "Peak Emotional Clutch Rescue (Savior Arrival)",
        "hook": "When All Hope Was Lost... HE ARRIVED 🥶🔥 | Savior Arrival #shorts #anime"
    },
    {
        "slot_utc": "2026-12-07T14:00:00Z",
        "slot_ist": "2026-12-07 07:30 PM IST",
        "file": "output/auto_group_c7_unhinged_comedy_gag_master.mp4",
        "format": "GROUP_C",
        "theme": "Unhinged / Out-of-Context Deranged Gags",
        "hook": "Anime Moments That Feel Completely Illegal 😂💀 | Dandadan #shorts #anime"
    }
]

def load_registry():
    if REGISTRY_FILE.exists():
        with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_registry(reg):
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(reg, f, indent=2, ensure_ascii=False)

def fill_vacant_slots():
    print("=" * 70)
    print("🚀 FILLING VACANT SLOTS WITH CLEAN GROUP C REPLACEMENTS")
    print("=" * 70)

    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        creds_data = json.load(f)
    creds = google.oauth2.credentials.Credentials.from_authorized_user_info(creds_data)
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)

    booster = ViralGrowthBoosterWorkflow()
    registry = load_registry()

    for idx, item in enumerate(REPLACEMENT_TARGETS, 1):
        file_path = item["file"]
        slot_utc = item["slot_utc"]
        slot_ist = item["slot_ist"]

        if not os.path.exists(file_path):
            print(f"[{idx}/5] ⚠️ File missing: {file_path}")
            continue

        print(f"\n[{idx}/5] 📦 Uploading replacement to slot {slot_ist} ({slot_utc})...")
        pkg = booster.assemble_boosted_metadata(
            video_path=file_path,
            target_name=item["theme"],
            group_type=item["format"],
            custom_hook=item["hook"]
        )

        body = {
            "snippet": {
                "title": pkg["title"][:100],
                "description": pkg["description"],
                "tags": pkg["tags"],
                "categoryId": "24"
            },
            "status": {
                "privacyStatus": "private",
                "publishAt": slot_utc,
                "selfDeclaredMadeForKids": False
            }
        }

        media = MediaFileUpload(file_path, mimetype="video/mp4", resumable=True, chunksize=1024*1024*5)
        request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)

        res = None
        while res is None:
            st, res = request.next_chunk()
            if st:
                print(f"   Uploaded {int(st.progress()*100)}%...")
        
        vid_id = res.get("id")
        print(f"   ✅ SUCCESS! Scheduled ID: {vid_id} at {slot_ist}")
        print(f"   URL: https://youtu.be/{vid_id}")

        registry[file_path] = {
            "status": "uploaded",
            "video_id": vid_id,
            "title": pkg["title"],
            "scheduled_slot_utc": slot_utc,
            "scheduled_slot_ist": slot_ist,
            "format": item["format"],
            "theme": item["theme"],
            "uploaded_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
        save_registry(registry)

    print("\n" + "=" * 70)
    print("🎉 ALL VACANT SLOTS SUCCESSFULLY FILLED WITH CLEAN GROUP C MASTERS!")
    print("=" * 70)

if __name__ == "__main__":
    fill_vacant_slots()
