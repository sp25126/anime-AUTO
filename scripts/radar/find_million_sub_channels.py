import json
import subprocess
import sys

def search_channel_data(query, count=5):
    cmd = [
        sys.executable, "-m", "yt_dlp",
        f"ytsearch{count}:{query}",
        "--print", "%(channel)s | %(channel_id)s | %(channel_url)s | %(view_count)s | %(title)s",
        "--no-warnings"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.stdout.strip().split("\n") if res.stdout.strip() else []

queries = [
    "anime couple moments that feel like a rom-com shorts",
    "anime accidental rizz shorts",
    "anime cold aura moments shorts",
    "these two are hilarious anime shorts",
    "anime moments that live in my head rent free shorts"
]

all_channels = {}

for q in queries:
    lines = search_channel_data(q, count=4)
    for l in lines:
        parts = l.split(" | ")
        if len(parts) >= 3:
            ch_name = parts[0]
            ch_id = parts[1]
            ch_url = parts[2]
            if ch_name not in all_channels:
                all_channels[ch_name] = {
                    "id": ch_id,
                    "url": ch_url,
                    "sample_title": parts[4] if len(parts) > 4 else ""
                }

print(f"Discovered {len(all_channels)} channels producing this style.")
for name, data in list(all_channels.items())[:15]:
    print(f"- {name}: {data['url']} | Sample: {data['sample_title']}")
