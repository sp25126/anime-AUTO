import yt_dlp
import json

ydl_opts = {
    'quiet': True,
    'skip_download': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for vid in ["Y3pmO6q8jSU", "uVxJwJcCLqA"]:
        info = ydl.extract_info(f"https://www.youtube.com/watch?v={vid}", download=False)
        print("="*50)
        print("Title:", info.get('title'))
        print("Channel:", info.get('uploader'))
        print("Views:", info.get('view_count'))
        heatmap = info.get('heatmap', [])
        # Find contiguous hot zone where value > 0.8
        hot_zones = [h for h in heatmap if (h.get('intensityScoreNormalized') or h.get('value', 0)) >= 0.80]
        if hot_zones:
            print(f"Hot zone span: {hot_zones[0]['start_time']:.1f}s -> {hot_zones[-1]['end_time']:.1f}s")
            print("Peak value:", max(h.get('value', 0) for h in hot_zones))
