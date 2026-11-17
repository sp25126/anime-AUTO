import yt_dlp
import os

# Search for royalty free chill anime lofi beat
query = "ytsearch1:funny anime comedy lofi hip hop royalty free"
out_dir = "assets/audio"
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "trending_comedy_lofi_bed.mp3")

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': out_file.replace('.mp3', ''),
    'quiet': False
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([query])

print("Downloaded BGM:", os.path.exists(out_file))
