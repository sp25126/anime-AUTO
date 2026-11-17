import subprocess
import json
import os

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

# Search queries across TikTok, Instagram, and YouTube for satisfying sound design
queries = [
    "fire force sound design edit tiktok 9:16",
    "anime satisfying sound effects sakuga edit tiktok",
    "jjk satisfying sound design bass boost edit reels"
]

candidates = []

for q in queries:
    print(f"Scouting sound design edits across platforms: '{q}'...")
    cmd = [
        python_exe, "-m", "yt_dlp",
        f"ytsearch4:{q}",
        "--dump-json",
        "--flat-playlist",
        "--no-warnings"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            dur = d.get("duration") or 0
            if 15 <= dur <= 55:
                candidates.append({
                    "id": d.get("id"),
                    "title": d.get("title"),
                    "duration": dur,
                    "views": d.get("view_count") or 0,
                    "uploader": d.get("uploader") or d.get("channel")
                })
        except:
            pass

candidates.sort(key=lambda x: x["views"], reverse=True)
os.makedirs("output", exist_ok=True)
with open("output/sound_design_candidates.json", "w", encoding="utf-8") as f:
    json.dump(candidates, f, indent=2)

print(f"\nDiscovered {len(candidates)} candidate edits:")
for c in candidates[:6]:
    print(f"  [{c['id']}] {c['views']:,} views | {c['duration']}s | {c['title'][:45]} | @{c['uploader']}")
