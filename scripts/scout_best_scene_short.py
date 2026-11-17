import subprocess
import json

specific_scenes = [
    ("Aizen Stops Ichigo Theme", "aizen stops ichigo sword finger short"),
    ("Madara vs Shinobi Alliance", "madara what will you do about the second one short"),
    ("Gojo Embarrasses Jogo", "gojo infinity domain expansion jogo short"),
    ("Sukuna Stand Proud Jogo", "sukuna stand proud you are strong short"),
    ("Cid I Am Atomic", "cid i am atomic scene short"),
    ("Ayanokoji Tool Monologue", "ayanokoji all people are nothing but tools short")
]

analytics = []

for name, q in specific_scenes:
    cmd = [
        "python", "-m", "yt_dlp",
        f"ytsearch3:{q}",
        "--dump-json",
        "--flat-playlist",
        "--no-warnings"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    items = []
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            dur = d.get("duration") or 0
            if 15 <= dur <= 65:
                items.append({
                    "id": d.get("id"),
                    "title": d.get("title"),
                    "views": d.get("view_count") or 0,
                    "duration": dur,
                    "uploader": d.get("uploader") or d.get("channel")
                })
        except:
            pass
    if items:
        # Sort by views
        items.sort(key=lambda x: x["views"], reverse=True)
        analytics.append({"scene": name, "top_pick": items[0]})

for a in analytics:
    p = a["top_pick"]
    print(f"[{a['scene']}] {p['views']:,} views | {p['duration']}s | {p['title'][:40]} | @{p['uploader']}")

with open("output/top_scene_candidates.json", "w", encoding="utf-8") as f:
    json.dump(analytics, f, indent=2)
