import yt_dlp
import json

queries = [
    "Blue Box anime confession moment",
    "Blue Box chinatsu taiki moment",
    "The Apothecary Diaries jinshi maomao rizz moment",
    "Reborn as a Space Mercenary funny moment"
]

ydl_opts = {
    'quiet': True,
    'skip_download': True,
    'extract_flat': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for q in queries:
        print(f"\n=== Query: {q} ===")
        res = ydl.extract_info(f"ytsearch4:{q}", download=False)
        for e in res.get('entries', []):
            print(f"- [{e.get('id')}] ({e.get('duration')}s) {e.get('title')}")
