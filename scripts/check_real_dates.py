import subprocess
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"
queries = [
    "Dandadan episode clip english sub",
    "Bleach TYBW episode clip english sub",
    "Blue Lock season 2 episode clip english sub"
]

all_vids = []
for q in queries:
    cmd = [python_exe, "-m", "yt_dlp", f"ytsearch4:{q}", "--dump-json", "--no-warnings"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            all_vids.append({
                "title": d.get("title"),
                "upload_date": d.get("upload_date"),
                "views": d.get("view_count") or 0,
                "duration": d.get("duration"),
                "id": d.get("id"),
                "channel": d.get("channel")
            })
        except:
            pass

# Sort by upload_date descending (latest real uploads first)
all_vids = sorted(all_vids, key=lambda x: x["upload_date"] or "", reverse=True)
print(f"Retrieved {len(all_vids)} latest clips on YouTube:")
for v in all_vids:
    print(f"• Date: {v['upload_date']} | Views: {v['views']:,} | Dur: {v['duration']}s | [{v['channel']}] {v['title'][:45]} ({v['id']})")
