import subprocess
import os
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

# Target: 7ZLS5KNDelI ("I AM ATOMIC Right Version / My Giga Chad Sound" - 3.4M views, 18s)
# Unmatched ear-pleasing audio design + massive viral recognition
vid = "7ZLS5KNDelI"
raw_out = f"assets/harvested_clips/{vid}.mp4"
os.makedirs("assets/harvested_clips", exist_ok=True)
os.makedirs("output", exist_ok=True)

print(f"[Harvester] Downloading viral sound design edit ({vid})...")
cmd = [
    python_exe, "-m", "yt_dlp",
    f"https://www.youtube.com/watch?v={vid}",
    "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    "-o", raw_out,
    "--no-playlist",
    "--quiet",
    "--no-warnings"
]
subprocess.run(cmd)

probe_cmd = [
    "ffprobe", "-v", "error", "-select_streams", "v:0",
    "-show_entries", "stream=width,height,duration",
    "-of", "csv=p=0", raw_out
]
meta = subprocess.check_output(probe_cmd).decode().strip()
print(f"Downloaded raw clip specs: {meta}")
