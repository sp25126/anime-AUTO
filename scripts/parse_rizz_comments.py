import subprocess
import json
import re

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"
vid = "VIJuDnN0nNI"

cmd = [python_exe, "-m", "yt_dlp", f"https://www.youtube.com/watch?v={vid}", "--write-comments", "--dump-json", "--no-download"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
try:
    d = json.loads(res.stdout.split("\n")[0])
    comments = d.get("comments") or []
    print(f"Retrieved {len(comments)} comments from Crunchyroll video:")
    
    ts_pattern = re.compile(r'\b(\d{1,2}):(\d{2})\b')
    buckets = {}
    for c in comments:
        text = c.get("text", "").replace("\n", " ")
        likes = c.get("like_count") or 1
        for m in ts_pattern.findall(text):
            sec = int(m[0]) * 60 + int(m[1])
            b = (sec // 15) * 15
            if b not in buckets:
                buckets[b] = {"likes": 0, "count": 0, "sample": text[:80]}
            buckets[b]["count"] += 1
            buckets[b]["likes"] += likes

    sorted_b = sorted(buckets.items(), key=lambda x: (x[1]["likes"], x[1]["count"]), reverse=True)
    for b, inf in sorted_b[:5]:
        print(f"• Peak: {b//60:02d}:{b%60:02d} | Likes: {inf['likes']:,} | Mentions: {inf['count']} | Quote: \"{inf['sample']}\"")
except Exception as e:
    print("Error:", e)
