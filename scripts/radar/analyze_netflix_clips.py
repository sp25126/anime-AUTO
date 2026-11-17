import yt_dlp
import json

candidates = [
    ("FpR2IaKqF64", "Netflix Anime - Momo Works at a Maid Cafe"),
    ("2RPYcli_GnA", "Netflix Anime - Don't Challenge Turbo Granny"),
    ("iiwOVqGtZj4", "Netflix Anime - Okarun's Full Throttle")
]

ydl_opts = {
    'quiet': True,
    'skip_download': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for vid, desc in candidates:
        info = ydl.extract_info(f"https://www.youtube.com/watch?v={vid}", download=False)
        print(f"\nTarget: {desc} ({vid}) | Views: {info.get('view_count')}")
        heatmap = info.get('heatmap', [])
        peaks = sorted(heatmap, key=lambda x: x.get('intensityScoreNormalized') or x.get('value', 0), reverse=True)[:3]
        for p in peaks:
            print("  Top peak:", p)
