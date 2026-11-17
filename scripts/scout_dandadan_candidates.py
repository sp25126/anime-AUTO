import subprocess
import json
import os

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"
query = "Dandadan edit 4k short"
print(f"Scouting top Dandadan shorts for query: {query}")

cmd = [
    python_exe, "-m", "yt_dlp",
    f"ytsearch10:{query}",
    "--dump-json",
    "--flat-playlist",
    "--no-warnings"
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
items = []

for line in res.stdout.strip().split("\n"):
    if not line:
        continue
    try:
        data = json.loads(line)
        items.append({
            "id": data.get("id"),
            "title": data.get("title"),
            "url": f"https://www.youtube.com/shorts/{data.get('id')}",
            "view_count": data.get("view_count", 0),
            "duration": data.get("duration", 0),
            "channel": data.get("channel") or data.get("uploader")
        })
    except Exception as e:
        pass

print(f"Discovered {len(items)} Dandadan shorts:")
for idx, it in enumerate(items[:6]):
    print(f" #{idx+1} | {it['id']} | {it['duration']}s | {it['title'][:40]} | @{it['channel']}")

os.makedirs("output", exist_ok=True)
with open("output/dandadan_candidates.json", "w", encoding="utf-8") as f:
    json.dump(items, f, indent=2)

print("Done scouting candidates.")
