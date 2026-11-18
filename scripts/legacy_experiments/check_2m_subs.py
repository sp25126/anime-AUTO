import subprocess
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

test_channels = [
    "Ani-One Asia",
    "Muse Asia",
    "Crunchyroll",
    "Anime Channel by sho-pro",
    "TOHO animation チャンネル",
    "KADOKAWAanime",
    "Bilibili Global"
]

res_list = []
for name in test_channels:
    cmd = [python_exe, "-m", "yt_dlp", f"ytsearch1:{name}", "--dump-json", "--no-warnings"]
    try:
        out = subprocess.check_output(cmd).decode("utf-8", errors="ignore")
        d = json.loads(out.split("\n")[0])
        res_list.append({
            "name": d.get("channel"),
            "subs": d.get("channel_follower_count"),
            "url": d.get("channel_url")
        })
    except Exception as e:
        pass

for r in res_list:
    subs = f"{r['subs']:,}" if r['subs'] else "N/A"
    print(f"[{r['name']}] Subs: {subs} | URL: {r['url']}")
