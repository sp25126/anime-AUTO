import subprocess
import os
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

# 5 Chosen Iconic Villains:
# Rank 5: Gilgamesh (Ego Walk) - VsITq4NxiMA
# Rank 4: Toji Fushiguro (Montagem Rugada Walk) - 9_VAGhAdne8
# Rank 3: Muzan Kibutsuji (Infinity Castle Entrance) - GBcj2wT-INA
# Rank 2: Sosuke Aizen (Timeless Aura) - 5BlQ-SuJhF0
# Rank 1: Madara Uchiha (Fourth War Walk) - 7WqbOlbogTc

selected = [
    {"rank": 5, "character": "Gilgamesh", "id": "VsITq4NxiMA", "creator": "Zeref Edit"},
    {"rank": 4, "character": "Toji Fushiguro", "id": "9_VAGhAdne8", "creator": "Zyper"},
    {"rank": 3, "character": "Muzan Kibutsuji", "id": "GBcj2wT-INA", "creator": "AnimeTwixMaster"},
    {"rank": 2, "character": "Sosuke Aizen", "id": "5BlQ-SuJhF0", "creator": "RECONZ AE"},
    {"rank": 1, "character": "Madara Uchiha", "id": "7WqbOlbogTc", "creator": "NARUTO 93"}
]

os.makedirs("assets/villain_raw", exist_ok=True)
downloaded = []

for s in selected:
    vid = s["id"]
    out_tmpl = f"assets/villain_raw/clip_{s['rank']}_{vid}.%(ext)s"
    print(f"Downloading Rank #{s['rank']} ({s['character']} - {vid})...")
    cmd = [
        python_exe, "-m", "yt_dlp",
        f"https://www.youtube.com/watch?v={vid}",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "-o", out_tmpl,
        "--no-playlist",
        "--quiet",
        "--no-warnings"
    ]
    subprocess.run(cmd)
    
    target_file = None
    for ext in ["mp4", "mkv", "webm"]:
        p = f"assets/villain_raw/clip_{s['rank']}_{vid}.{ext}"
        if os.path.exists(p):
            target_file = p
            break
            
    if target_file:
        print(f"  -> Saved: {target_file}")
        downloaded.append({
            "rank": s["rank"],
            "character": s["character"],
            "id": vid,
            "creator": s["creator"],
            "path": target_file
        })
    else:
        print(f"  -> Failed to download {vid}")

with open("output/villain_downloaded.json", "w", encoding="utf-8") as f:
    json.dump(downloaded, f, indent=2)

print(f"Successfully downloaded {len(downloaded)} villain clips.")
