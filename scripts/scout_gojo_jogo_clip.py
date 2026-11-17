import subprocess
import json

queries = [
    "Gojo vs Jogo reality check english sub short",
    "Gojo holding Jogo hand english sub short",
    "Gojo infinity explanation english sub short"
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
            if 20 <= dur <= 65:
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

with open("output/gojo_jogo_candidates.json", "w", encoding="utf-8") as f:
    json.dump(candidates, f, indent=2)
