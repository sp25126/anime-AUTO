import yt_dlp
import json

queries = [
    "Dandadan okarun momo tunnel scene",
    "Dandadan turbo granny cursed moment",
    "Dandadan episode 1 okarun momo conversation",
    "Dandadan episode 2 funny moment"
]

ydl_opts = {
    'quiet': True,
    'skip_download': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for q in queries:
        print(f"\n=== Query: {q} ===")
        res = ydl.extract_info(f"ytsearch3:{q}", download=False)
        for e in res.get('entries', []):
            vid = e.get('id')
            title = e.get('title')
            dur = e.get('duration')
            uploader = e.get('uploader')
            heatmap = e.get('heatmap')
            print(f"- [{vid}] ({dur}s) | Heatmap: {'YES' if heatmap else 'NO'} | Channel: {uploader} | {title}")
