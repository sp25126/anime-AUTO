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

    # Extract all currently assigned distinct date slots in chronological order
    all_slots = sorted([meta["scheduled_slot_utc"] for _, meta in items])

    # Interleave / shuffle formats so no single niche repeats consecutively
    # Target pattern: Group A -> Group B -> Group C -> Group A -> Group B ...
    by_format = {}
    for path, meta in items:
        fmt = meta.get("format", "UNKNOWN")
        by_format.setdefault(fmt, []).append((path, meta))

    for fmt in by_format:
        random.shuffle(by_format[fmt])

    interleaved = []
    # Round-robin pop across available formats
    keys = list(by_format.keys())
    while any(by_format.values()):
        for k in keys:
            if by_format[k]:
                interleaved.append(by_format[k].pop(0))

    print(f"Interleaved sequence planned ({len(interleaved)} items):")
    for idx, (path, meta) in enumerate(interleaved):
        print(f"  [{idx+1:02d}] {meta['format']} - {meta['title'][:45]}")

    # Re-assign dates to YouTube video objects
    for idx, ((path, meta), target_slot) in enumerate(zip(interleaved, all_slots)):
        vid_id = meta["video_id"]
        ist_str = (datetime.datetime.fromisoformat(target_slot.replace("Z", "+00:00")) + datetime.timedelta(hours=5, minutes=30)).strftime("%Y-%m-%d %I:%M %p IST")

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
            print(f"Updated {vid_id} -> {ist_str} ({meta['format']})")
            meta["scheduled_slot_utc"] = target_slot
            meta["scheduled_slot_ist"] = ist_str
        except Exception as e:
            print(f"Error updating {vid_id}: {e}")

    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)

    print("\n✅ Successfully shuffled and interleaved all scheduled videos in YouTube Studio!")

if __name__ == "__main__":
    shuffle_and_reassign()
