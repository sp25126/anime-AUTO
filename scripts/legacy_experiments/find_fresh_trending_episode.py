import subprocess
import json
from datetime import datetime, timedelta

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

# Search queries for fresh episodes from the past 7-14 days with English subtitles
queries = [
    "Bleach TYBW Part 3 episode clip english sub",
    "Blue Lock Season 2 episode clip english sub",
    "Dandadan episode clip english sub",
    "Re Zero Season 3 episode clip english sub"
]

results = []
# 14 days ago filter
cutoff_date = (datetime.now() - timedelta(days=14)).strftime("%Y%m%d")
print(f"Searching for trending anime clips uploaded AFTER {cutoff_date}...")

for q in queries:
    cmd = [
        python_exe, "-m", "yt_dlp",
        f"ytsearch5:{q}",
        "--dateafter", f"now-14days",
        "--dump-json",
        "--no-warnings"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            up_date = d.get("upload_date")
            views = d.get("view_count") or 0
            dur = d.get("duration") or 0
            # Must be a reasonable clip length (20s to 400s)
            if up_date and up_date >= cutoff_date and 20 <= dur <= 600:
                results.append({
                    "title": d.get("title"),
                    "id": d.get("id"),
                    "channel": d.get("channel"),
                    "views": views,
                    "duration": dur,
                    "upload_date": up_date,
                    "url": f"https://www.youtube.com/watch?v={d.get('id')}"
                })
        except:
            pass

# Sort by views descending
results = sorted(results, key=lambda x: x["views"], reverse=True)
print(f"\nFound {len(results)} fresh clips uploaded in the last 14 days:")
for r in results[:10]:
    print(f"• [{r['upload_date']}] {r['title'][:55]} | Views: {r['views']:,} | Dur: {r['duration']}s | ID: {r['id']}")

with open("output/fresh_trending_clips.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
