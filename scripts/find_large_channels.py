import subprocess
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

queries = [
    "anime funny moments shorts 10M",
    "bro rizz anime shorts",
    "anime savage moment shorts",
    "anime confession scene short"
]

channels = {}
for q in queries:
    cmd = [python_exe, "-m", "yt_dlp", f"ytsearch8:{q}", "--dump-json", "--no-warnings"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            ch = d.get("channel") or d.get("uploader")
            subs = d.get("channel_follower_count")
            views = d.get("view_count") or 0
            if ch and subs and subs >= 500000 and ch not in channels:
                channels[ch] = {
                    "name": ch,
                    "subs": subs,
                    "title": d.get("title"),
                    "views": views,
                    "id": d.get("id")
                }
        except:
            pass

print(f"Found {len(channels)} high-subscriber channels:")
for k, v in sorted(channels.items(), key=lambda x: x[1]["subs"], reverse=True):
    print(f"[{v['name']}] Subs: {v['subs']:,} | Video Views: {v['views']:,} | {v['title'][:50]} (ID: {v['id']})")
