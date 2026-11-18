import subprocess
import os
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

# Search for native 9:16 vertical Luffy TikTok shorts
queries = [
    "luffy gear 5 tiktok edit vertical 9:16",
    "luffy gear 5 phone edit tiktok",
    "luffy gear 5 drums of liberation edit short"
]

candidates = []

for q in queries:
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
            if 15 <= dur <= 58:
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
for c in candidates[:5]:
    print(f"[{c['id']}] {c['views']:,} views | {c['duration']}s | {c['title'][:40]} | @{c['uploader']}")

with open("output/vertical_luffy_candidates.json", "w", encoding="utf-8") as f:
    json.dump(candidates, f, indent=2)
