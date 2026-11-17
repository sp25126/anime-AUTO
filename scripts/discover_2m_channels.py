import subprocess
import json
import os

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

channels = [
    "https://www.youtube.com/@UnlimitedSkyyy",
    "https://www.youtube.com/@hasibkunamv"
]

for url in channels:
    cmd = [python_exe, "-m", "yt_dlp", "--dump-json", "--playlist-items", "1", url]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    try:
        d = json.loads(res.stdout.split("\n")[0])
        print(f"Channel: {d.get('channel')} | Subs: {d.get('channel_follower_count')} | URL: {url}")
    except Exception as e:
        print(f"Failed for {url}: {e}")

# Now search for 2M+ subscriber anime scene/moments channels
queries = [
    "anime moment short 10M views",
    "bro ignored a beauty anime short",
    "anime funny moments shorts 50M views",
    "anime scene 4k short 20M views"
]

found_channels = {}

for q in queries:
    cmd = [python_exe, "-m", "yt_dlp", f"ytsearch5:{q}", "--dump-json", "--flat-playlist", "--no-warnings"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            ch = d.get("uploader") or d.get("channel")
            ch_url = d.get("uploader_url") or d.get("channel_url")
            vid = d.get("id")
            title = d.get("title")
            views = d.get("view_count")
            if ch and ch not in found_channels:
                found_channels[ch] = {"name": ch, "url": ch_url, "sample_vid": vid, "sample_title": title, "views": views}
        except:
            pass

print(f"\nDiscovered {len(found_channels)} related creator channels:")
for k, v in list(found_channels.items())[:12]:
    print(f"  • {v['name']} | Sample: {v['sample_title'][:40]} ({v['sample_vid']})")
