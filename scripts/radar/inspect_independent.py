import yt_dlp
import json

candidates = [
    ("A0kMxMaCW9o", "Mitsuri - Overgeared Funny Moments Compilation"),
    ("yeTMPl82lQc", "Seijinnime - Overgeared Grid & Doran vs Yura"),
    ("imbUgADJEFg", "Blue Box - Chinatsu Taiki"),
    ("UhyGNxOf6wo", "Reborn as Space Mercenary - Elma Cute Tsundere")
]

ydl_opts = {
    'quiet': True,
    'skip_download': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for vid_id, desc in candidates:
        try:
            info = ydl.extract_info(f"https://www.youtube.com/watch?v={vid_id}", download=False)
            heatmap = info.get('heatmap', [])
            uploader = info.get('uploader')
            views = info.get('view_count')
            print(f"\nID: {vid_id} | {desc} | Channel: {uploader} | Views: {views}")
            if heatmap:
                print(f"  Heatmap points: {len(heatmap)}")
                top = sorted(heatmap, key=lambda x: x.get('intensityScoreNormalized') or x.get('value', 0), reverse=True)[:3]
                print(f"  Top peaks: {top}")
            else:
                print("  No heatmap.")
        except Exception as e:
            print(f"Error on {vid_id}: {e}")
