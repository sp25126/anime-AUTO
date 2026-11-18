import subprocess
import os
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

# Target: ZHVuXN4DHkE ("you thought you could beat me with this loser" - 1.76M views)
# Alternate high-action infinity flex: k0cny79b-Q4 or 442c2fp_4ds
vid = "ZHVuXN4DHkE"
out_tmpl = f"assets/scene_raw/{vid}.%(ext)s"
os.makedirs("assets/scene_raw", exist_ok=True)

print(f"Downloading Gojo vs Jogo scene clip {vid}...")
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
    p = f"assets/scene_raw/{vid}.{ext}"
    if os.path.exists(p):
        target_file = p
        break

print(f"Downloaded scene raw: {target_file}")
