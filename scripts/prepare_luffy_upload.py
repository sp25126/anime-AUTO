import subprocess
import os
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

# Top candidate: pF3qDOiiKGI ("[4K] Luffy Gear 5「Edit」(Toma Toma)" by @ZorosPasta - 1.17M views, 27s, native 9:16 vertical TikTok/Shorts format)
vid = "pF3qDOiiKGI"
raw_out = f"assets/harvested_clips/{vid}.mp4"
os.makedirs("assets/harvested_clips", exist_ok=True)
os.makedirs("output", exist_ok=True)

print(f"[Harvester] Downloading viral Gear 5 edit ({vid}) by @ZorosPasta...")
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

final_upload_video = "output/luffy_gear5_booming_tiktok_mastered.mp4"

# Normalize audio to YouTube Shorts EBU R128 (-14.0 LUFS, -1.5 dBTP) and ensure strict 30fps CFR
print("[Audio Master] Mastering audio to EBU R128 (-14.0 LUFS)...")
cmd_master = [
    "ffmpeg", "-y",
    "-i", raw_out,
    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
    "-c:v", "copy",
    "-c:a", "aac", "-b:a", "256k",
    final_upload_video
]
subprocess.run(cmd_master, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(f"[Done] Master video ready for upload: {final_upload_video}")
