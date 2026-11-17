import subprocess
import os

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

# Target: zpCZhbSKXq8 ("Like Him. (This took me 10+ hours)" by @Molob - 1.44M views, 45s)
vid = "zpCZhbSKXq8"
raw_out = f"assets/harvested_clips/{vid}.mp4"
os.makedirs("assets/harvested_clips", exist_ok=True)
os.makedirs("output", exist_ok=True)

print(f"[Harvester] Downloading {vid}...")
cmd_dl = [
    python_exe, "-m", "yt_dlp",
    f"https://www.youtube.com/watch?v={vid}",
    "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
    "-o", raw_out,
    "--no-playlist",
    "--quiet",
    "--no-warnings"
]
subprocess.run(cmd_dl)

final_vertical_short = "output/luffy_gear5_vertical_mastered.mp4"

print("[Compositor] Converting to strict 1080x1920 (9:16 portrait) with dynamic blurred background...")
# [bg] fills 1080x1920 with heavy boxblur and color grade
# [fg] keeps exact 16:9 proportion (1080:-2), centered
filter_complex = (
    "[0:v]fps=30,split=2[fg_raw][bg_raw];"
    "[bg_raw]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5,eq=brightness=-0.15:saturation=1.2[bg_blur];"
    "[fg_raw]scale=1080:-2,setsar=1[fg_scaled];"
    "[bg_blur][fg_scaled]overlay=0:(1920-h)/2[vout];"
    "[0:a]loudnorm=I=-14:TP=-1.5:LRA=11[aout]"
)

cmd_master = [
    "ffmpeg", "-y",
    "-i", raw_out,
    "-filter_complex", filter_complex,
    "-map", "[vout]", "-map", "[aout]",
    "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "256k",
    final_vertical_short
]
subprocess.run(cmd_master, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(f"[Done] Strict 9:16 vertical Short created: {final_vertical_short}")
