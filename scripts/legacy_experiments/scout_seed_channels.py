import subprocess
import json
import os

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"
os.makedirs("output/research_channels", exist_ok=True)

targets = [
    ("UnlimitedSkyyy", "https://www.youtube.com/@UnlimitedSkyyy/shorts"),
    ("hasibkunamv", "https://www.youtube.com/@hasibkunamv/shorts")
]

channel_data = {}

for name, url in targets:
    print(f"Scouting channel: {name} ({url})...")
    cmd = [
        python_exe, "-m", "yt_dlp",
        url,
        "--dump-json",
        "--flat-playlist",
        "--playlist-end", "10",
        "--no-warnings"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    videos = []
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            videos.append({
                "id": d.get("id"),
                "title": d.get("title"),
                "views": d.get("view_count"),
                "duration": d.get("duration")
            })
        except:
            pass
    channel_data[name] = videos
    print(f"  -> Found {len(videos)} recent shorts for {name}")

with open("output/research_channels/seed_channels.json", "w", encoding="utf-8") as f:
    json.dump(channel_data, f, indent=2)

for name, vids in channel_data.items():
    print(f"\n=== {name} Top Shorts ===")
    for v in vids[:5]:
        print(f"  [{v['id']}] {v.get('title')[:50]} (dur: {v.get('duration')}s)")
