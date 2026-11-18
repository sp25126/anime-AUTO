import subprocess
import os
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

# Target: aWApEIyXUp4 (Gojo vs Sukuna - Clarity [Edit/AMV] 4K by @KING_WIZZY, 35s)
vid = "aWApEIyXUp4"
out_tmpl = f"assets/rotate_raw/{vid}.%(ext)s"
os.makedirs("assets/rotate_raw", exist_ok=True)

print(f"Downloading 4K horizontal AMV {vid}...")
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
    p = f"assets/rotate_raw/{vid}.{ext}"
    if os.path.exists(p):
        target_file = p
        break

print(f"Downloaded file: {target_file}")
meta = {
    "id": vid,
    "title": "Gojo vs Sukuna - Clarity [Edit/AMV] 4K",
    "creator": "KING_WIZZY",
    "file": target_file
}
with open("output/rotate_downloaded_meta.json", "w", encoding="utf-8") as f:
    json.dump(meta, f, indent=2)
