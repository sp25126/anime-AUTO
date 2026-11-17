import subprocess
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

queries = [
    "top anime moments trending this week",
    "anime funny moments english sub viral",
    "coldest anime moment english sub viral",
    "anime accidental rizz moment english sub"
]

trending_pool = {}
for q in queries:
    cmd = [python_exe, "-m", "yt_dlp", f"ytsearch6:{q}", "--dump-json", "--no-warnings"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            title = d.get("title")
            views = d.get("view_count") or 0
            dur = d.get("duration") or 0
            ch = d.get("channel")
            vid = d.get("id")
            if 15 <= dur <= 300 and views > 50000:
                trending_pool[vid] = {
                    "title": title,
                    "views": views,
                    "duration": dur,
                    "channel": ch,
                    "id": vid
                }
        except:
            pass

print(f"Discovered {len(trending_pool)} viral candidates across franchises:\n")
sorted_vids = sorted(trending_pool.values(), key=lambda x: x["views"], reverse=True)
for data in sorted_vids[:12]:
    print(f"• [{data['channel']}] {data['title'][:65]} | Views: {data['views']:,} | Dur: {data['duration']}s (ID: {data['id']})")

with open("output/multi_anime_radar.json", "w", encoding="utf-8") as f:
    json.dump(sorted_vids, f, indent=2)
