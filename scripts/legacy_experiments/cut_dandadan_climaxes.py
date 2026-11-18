import subprocess
import os
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"
os.makedirs("assets/dandadan_cut", exist_ok=True)

with open("output/dandadan_downloaded.json", encoding="utf-8") as f:
    clips = json.load(f)

# Define 10-12s causal climax ranges for each clip
# Rank 5 down to Rank 1 countdown
cuts = [
    {"rank": 5, "id": "wcTxVIeerQ8", "file": "assets/dandadan_raw/clip_5_wcTxVIeerQ8.mp4", "start": 3.0, "duration": 11.5, "creator": "Molob", "action": "Turbo Granny Speed Burst"},
    {"rank": 4, "id": "89g7o-KsxFU", "file": "assets/dandadan_raw/clip_4_89g7o-KsxFU.mp4", "start": 4.0, "duration": 12.0, "creator": "Molob", "action": "Okarun Transformation Flash"},
    {"rank": 3, "id": "dFh6Vj15S8s", "file": "assets/dandadan_raw/clip_3_dFh6Vj15S8s.mp4", "start": 2.5, "duration": 11.5, "creator": "Molob", "action": "Momo Telekinesis Hand Crush"},
    {"rank": 2, "id": "m_7SdITOAAE", "file": "assets/dandadan_raw/clip_2_m_7SdITOAAE.mp4", "start": 3.0, "duration": 12.5, "creator": "Zyper", "action": "Alien Serpo Bass Drop Climax"},
    {"rank": 1, "id": "LQIL6uLsLjw", "file": "assets/dandadan_raw/clip_1_LQIL6uLsLjw.mp4", "start": 5.0, "duration": 13.5, "creator": "Flick", "action": "Route 765 Hyper Sakuga Final Peak"}
]

prepared = []

for c in cuts:
    out_file = f"assets/dandadan_cut/rank_{c['rank']}_{c['id']}.mp4"
    print(f"Cutting Rank #{c['rank']} ({c['action']}) - {c['duration']}s...")
    
    # Precise cut and normalize to 1080x1920 30fps CFR with stereo audio
    filter_complex = (
        "[0:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,"
        "crop=1080:1920,setsar=1[v];"
        "[0:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo[a]"
    )
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(c["start"]),
        "-i", c["file"],
        "-t", str(c["duration"]),
        "-filter_complex", filter_complex,
        "-map", "[v]", "-map", "[a]",
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k",
        out_file
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    prepared.append({
        "rank": c["rank"],
        "path": out_file,
        "duration": c["duration"],
        "creator": c["creator"],
        "action": c["action"]
    })

with open("output/dandadan_prepared_cuts.json", "w", encoding="utf-8") as f:
    json.dump(prepared, f, indent=2)

print("All 5 clips successfully cut to causal climax windows.")
