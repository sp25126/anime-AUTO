import yt_dlp
import json

queries = [
    "Dandadan accidental rizz",
    "Dandadan funny moment",
    "Dandadan okarun momo funny moment",
    "Chainsaw man funny moment",
    "Frieren savage moment"
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
            uploader = e.get('uploader')
            heatmap = e.get('heatmap')
            has_hm = "YES" if heatmap else "NO"
            print(f"- [{vid}] Heatmap: {has_hm} | Channel: {uploader} | {title}")
