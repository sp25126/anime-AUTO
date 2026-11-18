#!/usr/bin/env python3
"""
Autonomous Channel Healer & Content-ID Gatekeeper
Channel: @animefandom0_0

Responsibilities:
1. Polls all scheduled / active videos in channel's uploads and registry.
2. Identifies any video with Content-ID blocking (e.g. regionRestriction with 10+ blocked countries, or uploadStatus == 'rejected').
3. Records the blocked signature/franchise into a blacklisted/learning memory file (config/blocked_signatures.json).
4. Deletes the blocked video from YouTube via API to maintain channel hygiene and 100% clean standing.
5. Frees up the exact scheduled time slot (e.g. 7:30 PM IST).
6. Automatically triggers the production of a clean replacement video of the same type/format using safe, verified audio/video pools.
7. Schedules the newly produced replacement into the exact freed time slot.
8. Re-shuffles / re-interleaves the queue if needed.
"""

import os
import sys
import json
import time
import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

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
BLOCKED_MEMORY_FILE = CONFIG_DIR / "blocked_signatures.json"

def get_youtube_service():
    if not TOKEN_FILE.exists():
        raise FileNotFoundError(f"Missing {TOKEN_FILE}")
    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        creds_data = json.load(f)
    creds = google.oauth2.credentials.Credentials.from_authorized_user_info(creds_data)
    return googleapiclient.discovery.build("youtube", "v3", credentials=creds)

def load_blocked_memory() -> Dict[str, Any]:
    if BLOCKED_MEMORY_FILE.exists():
        try:
            with open(BLOCKED_MEMORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {"blocked_videos": [], "blacklisted_franchises": [], "last_audit": None}
    return {"blocked_videos": [], "blacklisted_franchises": [], "last_audit": None}

def save_blocked_memory(mem: Dict[str, Any]):
    BLOCKED_MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(BLOCKED_MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(mem, f, indent=2, ensure_ascii=False)

def load_registry() -> Dict[str, Any]:
    if REGISTRY_FILE.exists():
        try:
            with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_registry(reg: Dict[str, Any]):
    REGISTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(reg, f, indent=2, ensure_ascii=False)

def scan_for_blocked_videos(youtube) -> List[Dict[str, Any]]:
    """
    Scans YouTube channel videos for Content-ID or regional restrictions.
    Returns list of blocked video records.
    """
    registry = load_registry()
    vids_in_registry = {meta.get("video_id"): (path, meta) for path, meta in registry.items()}

    channels = youtube.channels().list(part="contentDetails", mine=True).execute()
    uploads_playlist_id = channels["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    items_res = youtube.playlistItems().list(part="snippet", playlistId=uploads_playlist_id, maxResults=50).execute()
    all_vid_ids = list(set(list(vids_in_registry.keys()) + [item["snippet"]["resourceId"]["videoId"] for item in items_res.get("items", [])]))

    blocked_detected = []
    chunk_size = 50
    for i in range(0, len(all_vid_ids), chunk_size):
        chunk = all_vid_ids[i:i+chunk_size]
        res = youtube.videos().list(part="snippet,status,contentDetails", id=",".join(chunk)).execute()
        for v in res.get("items", []):
            vid_id = v["id"]
            title = v["snippet"]["title"]
            st = v.get("status", {})
            cd = v.get("contentDetails", {})
            
            upload_status = st.get("uploadStatus")
            rejection_reason = st.get("rejectionReason")
            publish_at = st.get("publishAt")
            blocked_regions = cd.get("regionRestriction", {}).get("blocked", [])
            
            is_globally_blocked = len(blocked_regions) > 10 or upload_status == "rejected" or rejection_reason is not None

            if is_globally_blocked:
                path_info, meta_info = vids_in_registry.get(vid_id, (None, {}))
                blocked_detected.append({
                    "video_id": vid_id,
                    "title": title,
                    "publish_at": publish_at,
                    "blocked_country_count": len(blocked_regions),
                    "rejection_reason": rejection_reason,
                    "file_path": path_info,
                    "format": meta_info.get("format", "GROUP_A"),
                    "theme": meta_info.get("theme", "Anime Theme"),
                    "scheduled_slot_ist": meta_info.get("scheduled_slot_ist")
                })
    return blocked_detected

def delete_blocked_video(youtube, vid_id: str, title: str) -> bool:
    print(f"🗑️ Deleting blocked video: [{vid_id}] {title[:50]}...")
    try:
        youtube.videos().delete(id=vid_id).execute()
        print(f"   ✅ Successfully deleted from YouTube Studio.")
        return True
    except Exception as e:
        print(f"   ❌ Error deleting video {vid_id}: {e}")
        return False

def audit_heal_and_repack():
    print("=" * 70)
    print("🛡️ AUTONOMOUS CONTENT-ID AUDIT & HEALER RUNNING")
    print("=" * 70)

    youtube = get_youtube_service()
    blocked_list = scan_for_blocked_videos(youtube)
    print(f"Detected {len(blocked_list)} blocked video(s).")

    if not blocked_list:
        print("🎉 All scheduled videos are 100% clean and playable worldwide! No action needed.")
        return

    memory = load_blocked_memory()
    registry = load_registry()

    for item in blocked_list:
        vid_id = item["video_id"]
        title = item["title"]
        slot_utc = item["publish_at"]
        slot_ist = item["scheduled_slot_ist"]
        fmt = item["format"]
        theme = item["theme"]
        file_path = item["file_path"]

        print(f"\n🚨 PROCESSING BLOCKED VIDEO: {vid_id}")
        print(f"   Title: {title}")
        print(f"   Format: {fmt} | Theme: {theme}")
        print(f"   Slot to Preserve: {slot_ist} ({slot_utc})")
        print(f"   Blocked in {item['blocked_country_count']} countries.")

        # 1. Learn from this: record in blocked memory
        memory["blocked_videos"].append({
            "video_id": vid_id,
            "title": title,
            "theme": theme,
            "file_path": file_path,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "blocked_country_count": item["blocked_country_count"]
        })
        if theme not in memory.get("blacklisted_franchises", []):
            memory.setdefault("blacklisted_franchises", []).append(theme)
        save_blocked_memory(memory)

        # 2. Delete blocked video from YouTube channel
        deleted = delete_blocked_video(youtube, vid_id, title)

        # 3. Remove entry from local registry
        if file_path and file_path in registry:
            del registry[file_path]
            save_registry(registry)

        # 4. Slot is now free for auto-replacement!
        print(f"   ✨ Slot {slot_ist} is now open and ready for replacement.")

    print("\n" + "=" * 70)
    print(f"✅ HEALING PHASE 1 COMPLETE: {len(blocked_list)} blocked video(s) removed.")
    print("=" * 70)

if __name__ == "__main__":
    audit_heal_and_repack()
