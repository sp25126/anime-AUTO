import subprocess
import os
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"
os.makedirs("assets/villain_blur_cut", exist_ok=True)
os.makedirs("output", exist_ok=True)

# 5 villain countdown cuts (10.5s - 12.5s each):
# Rank 5: Gilgamesh (King of Heroes Golden Aura Walk)
# Rank 4: Toji Fushiguro (Cursed Tool Stroll)
# Rank 3: Muzan Kibutsuji (Infinity Castle Biwa Step)
# Rank 2: Sosuke Aizen (Espada Throne Chair Aura)
# Rank 1: Madara Uchiha (Shinobi Alliance March)

cuts = [
    {"rank": 5, "character": "GILGAMESH", "file": "assets/villain_raw/clip_5_VsITq4NxiMA.mp4", "start": 3.0, "duration": 11.0, "creator": "Zeref Edit", "views": "450K"},
    {"rank": 4, "character": "TOJI", "file": "assets/villain_raw/clip_4_9_VAGhAdne8.mp4", "start": 3.0, "duration": 11.5, "creator": "Zyper", "views": "1.8M"},
    {"rank": 3, "character": "MUZAN", "file": "assets/villain_raw/clip_3_GBcj2wT-INA.mp4", "start": 4.0, "duration": 11.5, "creator": "AnimeTwixMaster", "views": "920K"},
    {"rank": 2, "character": "AIZEN", "file": "assets/villain_raw/clip_2_5BlQ-SuJhF0.mp4", "start": 2.0, "duration": 12.0, "creator": "RECONZ AE", "views": "2.3M"},
    {"rank": 1, "character": "MADARA", "file": "assets/villain_raw/clip_1_7WqbOlbogTc.mp4", "start": 2.5, "duration": 12.5, "creator": "NARUTO 93", "views": "4.6M"}
]

prepared = []

for c in cuts:
    out_file = f"assets/villain_blur_cut/rank_{c['rank']}_{c['character']}.mp4"
    print(f"Preparing Rank #{c['rank']} ({c['character']}) with dynamic blurred video background...")
    
    # Split:
    # [bg] fills 1080x1920, heavy boxblur, darkened slightly
    # [fg] keeps exact 16:9 proportion (1080:-2), centered
    filter_complex = (
        "[0:v]fps=30,split=2[fg_raw][bg_raw];"
        "[bg_raw]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5,eq=brightness=-0.15:saturation=1.2[bg_blur];"
        "[fg_raw]scale=1080:-2,setsar=1[fg_scaled];"
        "[bg_blur][fg_scaled]overlay=0:(1920-h)/2[vout];"
        "[0:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo[aout]"
    )
    cmd = [
        "ffmpeg", "-y",
        "-ss", str(c["start"]),
        "-i", c["file"],
        "-t", str(c["duration"]),
        "-filter_complex", filter_complex,
        "-map", "[vout]", "-map", "[aout]",
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k",
        out_file
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    prepared.append({
        "rank": c["rank"],
        "character": c["character"],
        "path": out_file,
        "duration": c["duration"],
        "creator": c["creator"],
        "views": c["views"]
    })

concat_list = "output/villain_blur_concat.txt"
with open(concat_list, "w") as f:
    for p in prepared:
        f.write(f"file '{os.path.abspath(p['path'])}'\n")

raw_concat = "output/villain_blur_base.mp4"
print("Concatenating into base video with dynamic blurred background...")
subprocess.run([
    "ffmpeg", "-y",
    "-f", "concat", "-safe", "0",
    "-i", concat_list,
    "-c", "copy",
    raw_concat
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

with open("output/villain_prepared.json", "w", encoding="utf-8") as f:
    json.dump(prepared, f, indent=2)

print("Villain base video generated successfully:", raw_concat)
