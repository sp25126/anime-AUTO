import subprocess
import os
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"
os.makedirs("assets/dandadan_blur_cut", exist_ok=True)
os.makedirs("output", exist_ok=True)

cuts = [
    {"rank": 5, "id": "wcTxVIeerQ8", "file": "assets/dandadan_raw/clip_5_wcTxVIeerQ8.mp4", "start": 3.0, "duration": 11.5, "creator": "Molob", "views": "105K"},
    {"rank": 4, "id": "89g7o-KsxFU", "file": "assets/dandadan_raw/clip_4_89g7o-KsxFU.mp4", "start": 4.0, "duration": 12.0, "creator": "Molob", "views": "360K"},
    {"rank": 3, "id": "dFh6Vj15S8s", "file": "assets/dandadan_raw/clip_3_dFh6Vj15S8s.mp4", "start": 2.5, "duration": 11.5, "creator": "Molob", "views": "260K"},
    {"rank": 2, "id": "m_7SdITOAAE", "file": "assets/dandadan_raw/clip_2_m_7SdITOAAE.mp4", "start": 3.0, "duration": 12.5, "creator": "Zyper", "views": "1.1M"},
    {"rank": 1, "id": "LQIL6uLsLjw", "file": "assets/dandadan_raw/clip_1_LQIL6uLsLjw.mp4", "start": 5.0, "duration": 13.5, "creator": "Flick", "views": "2.4M"}
]

prepared = []

for c in cuts:
    out_file = f"assets/dandadan_blur_cut/rank_{c['rank']}_{c['id']}.mp4"
    print(f"Preparing Rank #{c['rank']} ({c['id']}) with dynamic blurred background...")
    
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
        "id": c["id"],
        "path": out_file,
        "duration": c["duration"],
        "creator": c["creator"],
        "views": c["views"]
    })

concat_list = "output/dandadan_blur_concat.txt"
with open(concat_list, "w") as f:
    for p in prepared:
        f.write(f"file '{os.path.abspath(p['path'])}'\n")

raw_concat = "output/dandadan_blur_base.mp4"
print("Concatenating into base video with dynamic blurred background...")
subprocess.run([
    "ffmpeg", "-y",
    "-f", "concat", "-safe", "0",
    "-i", concat_list,
    "-c", "copy",
    raw_concat
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("Base video created successfully:", raw_concat)
