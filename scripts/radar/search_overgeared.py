import yt_dlp
import json

queries = [
    "Overgeared anime episode 1 moment",
    "Overgeared anime grid funny moment",
    "Overgeared anime fight clip",
    "Reborn as a Space Mercenary episode 1 funny moment"
]

ydl_opts = {
    'quiet': True,
    'skip_download': True,
    'extract_flat': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for q in queries:
        print(f"\n=== Query: {q} ===")
        res = ydl.extract_info(f"ytsearch3:{q}", download=False)
        for e in res.get('entries', []):
            print(f"- [{e.get('id')}] ({e.get('duration')}s) Channel: {e.get('uploader')} | {e.get('title')}")
