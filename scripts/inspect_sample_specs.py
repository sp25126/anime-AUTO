import subprocess
import json

samples = [
    ('UnlimitedSkyyy', 'AQOqvkNZWS8'),
    ('hasibkunamv', 'M-0dbpKyyQ0'),
    ('hasibkunamv_2', '6wu14zP8M3Y'),
    ('Ref_Midnight_Heart', 'SWOh7guNi14')
]

for tag, vid in samples:
    cmd = ['python', '-m', 'yt_dlp', '-j', f'https://www.youtube.com/shorts/{vid}']
    d = json.loads(subprocess.check_output(cmd).decode('utf-8', errors='ignore'))
    print(f"[{tag}] {d.get('title')[:45]} | Views: {d.get('view_count'):,} | Dur: {d.get('duration')}s | {d.get('width')}x{d.get('height')}")
