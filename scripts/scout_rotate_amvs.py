import subprocess
import json
import os

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

queries = [
    "demon slayer infinity castle 4k amv 60fps",
    "sukuna vs mahoraga 4k amv 60fps",
    "gojo vs sukuna 4k amv 60fps",
    "solo leveling 4k amv 60fps"
]

candidates = []

for q in queries:
    print(f"Scouting horizontal AMVs for: {q}...")
    cmd = [
        python_exe, "-m", "yt_dlp",
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
            if 30 <= dur <= 240:
                candidates.append({
                    "query": q,
                    "id": d.get("id"),
                    "title": d.get("title"),
                    "duration": dur,
                    "uploader": d.get("uploader") or d.get("channel")
                })
                break
        except:
            pass

os.makedirs("output", exist_ok=True)
with open("output/rotate_candidates.json", "w", encoding="utf-8") as f:
    json.dump(candidates, f, indent=2)

for c in candidates:
    print(f"[{c['id']}] {c['duration']}s | {c['title'][:45]} | @{c['uploader']}")
