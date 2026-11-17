import subprocess
import json

queries = [
    ("Unaware OP Protagonist", "bro forgot he was supposed to hide his power anime"),
    ("Accidental Rizz", "bro rizz them without knowing anime"),
    ("Cold Disrespect", "coldest anime disrespect scene"),
    ("Saddest Goodbyes", "saddest anime moment short"),
    ("Sudden Rage Snap", "anime character snaps rage scene short"),
    ("Underestimated Reality Check", "anime underestimated reality check short")
]

results = []
for name, q in queries:
    cmd = [
        "python", "-m", "yt_dlp",
        f"ytsearch3:{q}",
        "--dump-json",
        "--flat-playlist",
        "--no-warnings"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    samples = []
    for line in res.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            d = json.loads(line)
            samples.append({
                "title": d.get("title"),
                "duration": d.get("duration"),
                "id": d.get("id"),
                "uploader": d.get("uploader") or d.get("channel")
            })
        except:
            pass
    results.append({"niche": name, "samples": samples})

for r in results:
    print(f"[{r['niche']}]")
    for s in r['samples'][:2]:
        print(f"  -> {s['title'][:50]} ({s['duration']}s) by @{s['uploader']}")

with open("output/single_scene_subcategories.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
