import subprocess
import json

ids = ['rWkB4qXvfK4', 'joGp46knFus', 'NhCKJcyEzhI', 'PWFHR0CSaLo', 'kSAvhgcj43w', '67_b_h89ZgI', 'QvW5Q9W68Ww']
metadata = []

for vid in ids:
    cmd = ['yt-dlp', '--dump-json', f'https://www.youtube.com/shorts/{vid}']
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        data = json.loads(res.stdout)
        info = {
            'id': vid,
            'title': data.get('title', ''),
            'views': data.get('view_count', 0),
            'duration': data.get('duration', 0),
            'uploader': data.get('uploader', ''),
            'url': f'https://www.youtube.com/shorts/{vid}'
        }
        metadata.append(info)
        print(f"[{vid}] {info['views']:,} views | {info['duration']}s | {info['title'][:45]} | @{info['uploader']}")
    else:
        print(f"[{vid}] Failed to fetch")

with open('output/dandadan_scouted_metadata.json', 'w', encoding='utf-8') as f:
    json.dump(metadata, f, indent=2)
