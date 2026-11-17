import yt_dlp
import json

candidates = [
    ("imbUgADJEFg", "Blue Box - Chinatsu Secretly Likes Taiki"),
    ("LNFuqVdrIvM", "Blue Box - Small Gifts, Big Moments Netflix"),
    ("Y3pmO6q8jSU", "The Apothecary Diaries - Jinshi True Essence"),
    ("uVxJwJcCLqA", "The Apothecary Diaries - Jealous Jinshi")
]

ydl_opts = {
    'quiet': True,
    'skip_download': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for vid_id, desc in candidates:
        url = f"https://www.youtube.com/watch?v={vid_id}"
        try:
            info = ydl.extract_info(url, download=False)
            heatmap = info.get('heatmap')
            has_sub = len(info.get('subtitles', {})) > 0 or len(info.get('automatic_captions', {})) > 0
            formats = [f"{f.get('height')}p" for f in info.get('formats', []) if f.get('height')]
            max_res = max([f.get('height') for f in info.get('formats', []) if f.get('height')] or [0])
            print(f"\nID: {vid_id} | {desc}")
            print(f"  Duration: {info.get('duration')}s | Max Res: {max_res}p")
            if heatmap:
                top = sorted(heatmap, key=lambda x: x.get('intensityScoreNormalized') or x.get('value', 0), reverse=True)[:2]
                print(f"  Heatmap points: {len(heatmap)} | Peak: {top}")
            else:
                print("  No heatmap available.")
        except Exception as e:
            print(f"Error on {vid_id}: {e}")
