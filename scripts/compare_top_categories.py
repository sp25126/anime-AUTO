import subprocess
import json

queries = [
    ("moment_accidental_rizz", "bro rizz them without knowing anime short"),
    ("moment_hidden_power_flex", "bro forgot he was supposed to hide his power anime short"),
    ("moment_underdog_silences_crowd", "anime underdog shocks crowd short"),
    ("moment_touch_them_and_die", "anime you hurt my loved one short")
]

results = []

for cat_id, q in queries:
    cmd = [
        "python", "-m", "yt_dlp",
        f"ytsearch5:{q}",
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
                "id": d.get("id"),
                "title": d.get("title"),
                "duration": d.get("duration"),
                "views": d.get("view_count", 0),
                "uploader": d.get("uploader") or d.get("channel")
            })
        except:
            pass
    results.append({"cat_id": cat_id, "query": q, "samples": samples})

for r in results:
    print(f"*** {r['cat_id']} ***")
    for s in r['samples'][:3]:
        print(f"  [{s['id']}] {s['views']:,} views | {s['duration']}s | {s['title'][:45]} | @{s['uploader']}")

with open("output/yt_research_comparison.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
