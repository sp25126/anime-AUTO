import yt_dlp
import json

ydl_opts = {
    'quiet': True,
    'extract_flat': True,
    'playlist_items': '1-6'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    res = ydl.extract_info('https://www.youtube.com/@UnlimitedSkyyy/shorts', download=False)
    for e in res.get('entries', []):
        vid_id = e.get('id')
        title = e.get('title')
        print(f"ID: {vid_id} | Title: {title}")
