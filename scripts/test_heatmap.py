import yt_dlp
import json

def test_search_and_heatmap():
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }
    query = 'ytsearch3:anime accidental rizz moment'
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        res = ydl.extract_info(query, download=False)
        entries = res.get('entries', [])
        for e in entries:
            v_id = e.get('id')
            title = e.get('title')
            duration = e.get('duration')
            heatmap = e.get('heatmap')
            print(f"ID: {v_id} | Title: {title} | Duration: {duration}s")
            if heatmap:
                print(f"  -> Heatmap detected! Points: {len(heatmap)}")
                top = sorted(heatmap, key=lambda x: x.get('intensityScoreNormalized', 0), reverse=True)[:2]
                print(f"  -> Top peaks: {top}")
            else:
                print("  -> No heatmap payload found in metadata.")

if __name__ == '__main__':
    test_search_and_heatmap()
