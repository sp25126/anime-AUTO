import urllib.request
import urllib.parse
import json
import re

candidates = [
    ("Dandadan", "Dandadan edit 4k short"),
    ("Solo Leveling", "Solo Leveling edit 4k short"),
    ("Bleach TYBW", "Bleach TYBW edit 4k short"),
    ("Demon Slayer", "Demon Slayer edit 4k short"),
    ("Chainsaw Man", "Chainsaw Man edit 4k short")
]

results = {}

for name, q in candidates:
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(q)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode("utf-8", errors="ignore")
        # Extract video IDs and short titles
        video_ids = list(set(re.findall(r"/shorts/([a-zA-Z0-9_-]{11})", html)))
        print(f"[{name}] Found {len(video_ids)} shorts")
        results[name] = {"query": q, "shorts_count": len(video_ids), "sample_ids": video_ids[:5]}
    except Exception as e:
        print(f"Error for {name}: {e}")

with open("output/trend_scout_result.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("Scouting complete.")
