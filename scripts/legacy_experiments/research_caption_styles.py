import subprocess
import json
import os

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

queries = [
    "anime shorts dynamic subtitles captions",
    "the moment he knew he messed up anime subtitles short",
    "anime scene subtitles font style short"
]

results = []

for q in queries:
    print(f"Scouting subtitle styles for: {q}...")
    cmd = [
        python_exe, "-m", "yt_dlp",
        f"ytsearch5:{q}",
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
            if 15 <= dur <= 60:
                results.append({
                    "id": d.get("id"),
                    "title": d.get("title"),
                    "views": d.get("view_count") or 0,
                    "uploader": d.get("uploader") or d.get("channel")
                })
        except:
            pass

os.makedirs("output", exist_ok=True)
with open("output/caption_style_research.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

for r in results[:6]:
    print(f"[{r['id']}] {r['views']:,} views | {r['title'][:45]} | @{r['uploader']}")
