import subprocess
import json
import os

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

queries = [
    "coldest anime villain entrance short",
    "anime villain aura walk short",
    "top 5 coldest anime entrances short"
]

results = []

for q in queries:
    print(f"Searching: {q}...")
    cmd = [
        python_exe, "-m", "yt_dlp",
        f"ytsearch6:{q}",
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
            results.append({
                "query": q,
                "id": d.get("id"),
                "title": d.get("title"),
                "duration": d.get("duration"),
                "views": d.get("view_count", 0),
                "uploader": d.get("uploader") or d.get("channel")
            })
        except:
            pass

os.makedirs("output", exist_ok=True)
with open("output/villain_aura_research.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print(f"Scouted {len(results)} reference videos.")
for r in results[:8]:
    print(f"[{r['id']}] {r['duration']}s | {r['title'][:45]} | @{r['uploader']}")
