import json
import random
import datetime
from pathlib import Path
import googleapiclient.discovery
import google.oauth2.credentials

CONFIG_DIR = Path("config")
TOKEN_FILE = CONFIG_DIR / "youtube_token.json"
REGISTRY_FILE = CONFIG_DIR / "scheduled_upload_registry.json"

def shuffle_and_reassign():
    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        creds_data = json.load(f)
    creds = google.oauth2.credentials.Credentials.from_authorized_user_info(creds_data)
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)

    with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
        registry = json.load(f)

    items = list(registry.items())
    print(f"Total videos to re-shuffle: {len(items)}")

    # Group videos by format to ensure diverse rotation
    by_format = {}
    for path, meta in items:
        fmt = meta.get("format", "UNKNOWN")
        by_format.setdefault(fmt, []).append((path, meta))

    for fmt in by_format:
        random.shuffle(by_format[fmt])
        print(f"  Format {fmt}: {len(by_format[fmt])} videos")

    # Interleave formats so no single niche repeats consecutively
    # Pattern: Group A -> Group B -> Group C -> Group A -> Group B ...
    interleaved = []
    keys = ["GROUP_A", "GROUP_B", "GROUP_C"]
    # Ensure any unexpected formats are also handled
    for k in by_format:
        if k not in keys:
            keys.append(k)

    while any(by_format.values()):
        for k in keys:
            if k in by_format and by_format[k]:
                interleaved.append(by_format[k].pop(0))

    print(f"\nPlanned interleaved sequence ({len(interleaved)} videos):")
    for idx, (path, meta) in enumerate(interleaved[:15]):
        print(f"  [{idx+1:02d}] {meta.get('format')} - {meta['title'][:45]}")
    if len(interleaved) > 15:
        print(f"  ... and {len(interleaved)-15} more videos.")

    # Target slot: Every morning at 7:30 AM IST (02:00:00Z UTC, within 7:00 AM - 8:00 AM window)
    # Starting from Nov 23, 2026 (first open slot following previously scheduled queue)
    start_dt = datetime.datetime(2026, 11, 23, 2, 0, 0, tzinfo=datetime.timezone.utc)
    all_slots = [(start_dt + datetime.timedelta(days=i)).strftime("%Y-%m-%dT02:00:00Z") for i in range(len(interleaved))]

    # Re-assign dates to YouTube video objects
    print("\nUpdating YouTube Studio scheduled dates...")
    updated_count = 0
    for idx, ((path, meta), target_slot) in enumerate(zip(interleaved, all_slots)):
        vid_id = meta["video_id"]
        ist_dt = datetime.datetime.fromisoformat(target_slot.replace("Z", "+00:00")) + datetime.timedelta(hours=5, minutes=30)
        ist_str = ist_dt.strftime("%Y-%m-%d %I:%M %p IST")

        # Update YouTube API
        body = {
            "id": vid_id,
            "status": {
                "privacyStatus": "private",
                "publishAt": target_slot,
                "selfDeclaredMadeForKids": False
            }
        }
        try:
            res = youtube.videos().update(part="status", body=body).execute()
            print(f"[{idx+1:02d}/{len(interleaved)}] Updated {vid_id} -> {ist_str} ({meta.get('format')}) - {meta['title'][:40]}")
            meta["scheduled_slot_utc"] = target_slot
            meta["scheduled_slot_ist"] = ist_str
            updated_count += 1
        except Exception as e:
            print(f"[{idx+1:02d}/{len(interleaved)}] Error updating {vid_id}: {e}")

    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Successfully shuffled and scheduled {updated_count}/{len(interleaved)} videos in YouTube Studio for 7:30 AM IST!")

if __name__ == "__main__":
    shuffle_and_reassign()
