import subprocess
import json
import re
from collections import Counter

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"
vid = "0e5DginyrIY"

print(f"Extracting top comments from video {vid}...")
cmd = [
    python_exe, "-m", "yt_dlp",
    f"https://www.youtube.com/watch?v={vid}",
    "--write-comments",
    "--dump-json",
    "--no-download"
]

res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
try:
    d = json.loads(res.stdout.split("\n")[0])
    comments = d.get("comments") or []
    print(f"Retrieved {len(comments)} comments.")
    
    # Regex to find timestamps: e.g. 1:45 or 01:45
    ts_pattern = re.compile(r'\b(\d{1,2}):(\d{2})\b')
    timestamp_mentions = []
    
    for c in comments:
        text = c.get("text", "")
        like_count = c.get("like_count") or 1
        matches = ts_pattern.findall(text)
        for m in matches:
            sec = int(m[0]) * 60 + int(m[1])
            # Weight timestamp by comment likes
            timestamp_mentions.append((sec, f"{m[0]}:{m[1]}", like_count, text[:80].replace("\n", " ")))
            
    # Group timestamps into 15-second buckets
    buckets = {}
    for sec, ts_str, likes, snippet in timestamp_mentions:
        b = (sec // 15) * 15
        if b not in buckets:
            buckets[b] = {"count": 0, "total_likes": 0, "samples": []}
        buckets[b]["count"] += 1
        buckets[b]["total_likes"] += likes
        if len(buckets[b]["samples"]) < 2:
            buckets[b]["samples"].append(f"{ts_str} (👍{likes}): \"{snippet}\"")
            
    print("\n--- TOP PUBLIC REACTION MOMENTS (BY COMMENT VELOCITY & LIKES) ---")
    sorted_buckets = sorted(buckets.items(), key=lambda x: (x[1]["total_likes"], x[1]["count"]), reverse=True)
    for b_sec, info in sorted_buckets[:5]:
        m_start = b_sec // 60
        s_start = b_sec % 60
        m_end = (b_sec + 25) // 60
        s_end = (b_sec + 25) % 60
        print(f"\n[PEAK MOMENT] {m_start:02d}:{s_start:02d} - {m_end:02d}:{s_end:02d} (Mentions: {info['count']} | Likes: {info['total_likes']:,})")
        for s in info["samples"]:
            print(f"   💬 {s}")
except Exception as e:
    print("Error parsing comments:", e)
