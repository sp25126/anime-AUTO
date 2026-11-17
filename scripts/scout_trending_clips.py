import subprocess
import json
import re

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

# Search for trending clips from current seasonal anime
queries = [
    "Dandadan episode funny moment english sub",
    "Bleach TYBW episode peak moment english sub",
    "Blue Lock season 2 episode clip english sub",
    "anime funny moments episode clip 2026 english sub"
]

results = []
for q in queries:
    cmd = [python_exe, "-m", "yt_dlp", f"ytsearch3:{q}", "--dump-json", "--no-warnings"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            results.append({
                "title": d.get("title"),
                "id": d.get("id"),
                "channel": d.get("channel"),
                "views": d.get("view_count") or 0,
                "duration": d.get("duration"),
                "url": f"https://www.youtube.com/watch?v={d.get('id')}"
            })
        except:
            pass

print(f"Scouted {len(results)} candidate episode clips:")
for r in results[:8]:
    print(f"• [{r['channel']}] {r['title'][:55]} | Views: {r['views']:,} | Dur: {r['duration']}s ({r['id']})")
