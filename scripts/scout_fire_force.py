import subprocess
import json

queries = [
    "Fire Force sound design bass boost short",
    "Shinra vs Sho sound design edit short",
    "Arthur Boyle Fire Force sound effect short",
    "Tamaki Fire Force explosion sound design short"
]

candidates = []

for q in queries:
    cmd = [
        "python", "-m", "yt_dlp",
        f"ytsearch3:{q}",
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
            if 15 <= dur <= 50:
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
for c in candidates[:6]:
    print(f"[{c['id']}] {c['views']:,} views | {c['duration']}s | {c['title'][:45]} | @{c['uploader']}")

with open("output/fire_force_candidates.json", "w", encoding="utf-8") as f:
    json.dump(candidates, f, indent=2)
