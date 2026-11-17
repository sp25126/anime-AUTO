import yt_dlp
import json

vid_id = "lMyKKdtNs1Q"
url = f"https://www.youtube.com/watch?v={vid_id}"

ydl_opts = {
    'quiet': True,
    'skip_download': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    print("Title:", info.get('title'))
    print("Duration:", info.get('duration'))
    print("Channel:", info.get('uploader'))
    print("Views:", info.get('view_count'))
    heatmap = info.get('heatmap', [])
    print(f"Heatmap data points: {len(heatmap)}")
    top_peaks = sorted(heatmap, key=lambda x: x.get('intensityScoreNormalized') or x.get('value', 0), reverse=True)[:5]
    print("Top peaks in audience replay:")
    for p in top_peaks:
        print(" ", p)
