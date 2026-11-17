import subprocess
import os
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

with open("output/dandadan_candidates.json", encoding="utf-8") as f:
    candidates = json.load(f)[:5]

os.makedirs("assets/dandadan_raw", exist_ok=True)
downloaded = []

for idx, c in enumerate(candidates):
    vid = c["id"]
    out_tmpl = f"assets/dandadan_raw/clip_{idx+1}_{vid}.%(ext)s"
    print(f"Downloading #{idx+1} ({vid}): {c['title'][:35]}...")
    cmd = [
        python_exe, "-m", "yt_dlp",
        f"https://www.youtube.com/watch?v={vid}",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "-o", out_tmpl,
        "--no-playlist",
        "--quiet",
        "--no-warnings"
    ]
    res = subprocess.run(cmd)
    
    # locate file
    target_file = None
    for ext in ["mp4", "mkv", "webm"]:
        p = f"assets/dandadan_raw/clip_{idx+1}_{vid}.{ext}"
        if os.path.exists(p):
            target_file = p
            break
            
    if target_file:
        print(f"  -> Successfully saved: {target_file}")
        downloaded.append({
            "rank": 5 - idx, # Rank 5 down to 1
            "id": vid,
            "title": c["title"],
            "channel": c["channel"],
            "path": target_file
        })
    else:
        print(f"  -> Failed to download {vid}")

with open("output/dandadan_downloaded.json", "w", encoding="utf-8") as f:
    json.dump(downloaded, f, indent=2)

print(f"Downloaded {len(downloaded)} clips.")
