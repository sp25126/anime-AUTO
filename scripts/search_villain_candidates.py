import subprocess
import json
import os

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

characters = [
    ("Madara Uchiha", "Madara entrance 4k edit short"),
    ("Aizen", "Aizen aura walk edit 4k short"),
    ("Ryomen Sukuna", "Sukuna walking edit 4k short"),
    ("Toji Fushiguro", "Toji entrance edit 4k short"),
    ("Gilgamesh", "Gilgamesh entrance edit 4k short"),
    ("Muzan Kibutsuji", "Muzan walking infinity castle edit 4k short")
]

curated = []

for name, q in characters:
    print(f"Searching top edit for {name} ({q})...")
    cmd = [
        python_exe, "-m", "yt_dlp",
        f"ytsearch3:{q}",
        "--dump-json",
        "--flat-playlist",
        "--no-warnings"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    found = 0
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            dur = d.get("duration") or 0
            # shorts are typically <= 60s
            if 10 <= dur <= 60:
                curated.append({
                    "character": name,
                    "id": d.get("id"),
                    "title": d.get("title"),
                    "duration": dur,
                    "uploader": d.get("uploader") or d.get("channel")
                })
                found += 1
                if found >= 2:
                    break
        except:
            pass

with open("output/villain_curated_candidates.json", "w", encoding="utf-8") as f:
    json.dump(curated, f, indent=2)

print(f"Found {len(curated)} viral candidate shorts:")
for c in curated:
    print(f"[{c['character']}] {c['id']} | {c['duration']}s | {c['title'][:40]} | @{c['uploader']}")
