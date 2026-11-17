import yt_dlp
import os

url = "https://www.youtube.com/watch?v=FpR2IaKqF64"
out_dir = "input"
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "dandadan_maid_cafe_raw.mp4")

ydl_opts = {
    'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': out_file,
    'quiet': False
}

print(f"Downloading {url} to {out_file}...")
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Downloaded successfully:", os.path.exists(out_file))
