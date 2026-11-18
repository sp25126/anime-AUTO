import subprocess
import json

for vid in ['zpCZhbSKXq8', 'fZ0mCo_bOM8', 'iyLtLGufkBA']:
    cmd = ['python', '-m', 'yt_dlp', '-j', f'https://www.youtube.com/shorts/{vid}']
    res = subprocess.check_output(cmd).decode('utf-8', errors='ignore')
    d = json.loads(res)
    print(f"[{vid}] {d.get('width')}x{d.get('height')} (Ratio: {d.get('aspect_ratio')}) | Title: {d.get('title')[:35]}")
