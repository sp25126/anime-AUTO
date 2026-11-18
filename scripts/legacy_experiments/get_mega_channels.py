import subprocess
import json
import os

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

megas = [
    "Anime Day Senpai",
    "KenzoAE",
    "Anime_Trio",
    "OtakuSensei",
    "Kudasai",
    "Crunchyroll",
    "Muse Asia"
]

results = []

for q in megas:
    cmd = [python_exe, "-m", "yt_dlp", f"ytsearch1:{q} anime short", "--dump-json", "--no-warnings"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="ignore")
    try:
        d = json.loads(res.stdout.split("\n")[0])
        results.append({
            "query": q,
            "channel": d.get("channel") or d.get("uploader"),
            "channel_id": d.get("channel_id"),
            "channel_url": d.get("channel_url"),
            "subs": d.get("channel_follower_count"),
            "sample_vid": d.get("id"),
            "sample_title": d.get("title")
        })
    except Exception as e:
        pass

for r in results:
    subs = f"{r['subs']:,}" if r['subs'] else "N/A"
    print(f"[{r['channel']}] Subs: {subs} | Sample: {r['sample_title'][:40]} ({r['sample_vid']})")

with open("output/research_channels/mega_channels.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
