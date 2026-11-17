import subprocess
import os
import json
import re
from PIL import Image, ImageDraw, ImageFont
from genre_background_engine import build_ffmpeg_filtergraph

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"
os.makedirs("output/inhouse_moments", exist_ok=True)

# 1. Target Clip: Dandadan Episode Clip with English Subtitles
vid = "0e5DginyrIY"
anime_name = "Dandadan"
target_url = f"https://www.youtube.com/watch?v={vid}"

# 2. Source: Dandadan Full Episode Clip
raw_clip_path = "output/inhouse_moments/dandadan_full_episode.mp4"
start_sec = 330 # 5:30 (Peak moment discovered from public comment reactions)
duration_sec = 25
genre = "romance_rizz" # Okarun & Momo cute dork/rizz moment
hook_title = "Bro Turned Into A Demon The Second They Disrespected Her 💀 | Dandadan #shorts #anime"

# 3. Apply Genre-Adaptive Background Compositor
filtergraph = build_ffmpeg_filtergraph(genre)
rendered_base = "output/inhouse_moments/dandadan_moment_base.mp4"
print(f"Compositing 9:16 vertical canvas ({start_sec}s to {start_sec + duration_sec}s) with [{genre.upper()}] genre background...")

cmd_render = [
    "ffmpeg", "-y", "-ss", str(start_sec), "-t", str(duration_sec),
    "-i", raw_clip_path,
    "-filter_complex", filtergraph,
    "-map", "[v]", "-map", "0:a",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-c:a", "aac", "-b:a", "192k",
    rendered_base
]
subprocess.run(cmd_render, check=True)

# 4. Generate Branded Outro Card (2 seconds)
outro_png = "output/inhouse_moments/outro_card.png"
img = Image.new("RGBA", (1080, 1920), (12, 14, 18, 255))
draw = ImageDraw.Draw(img)

font_brand = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 56)
font_sub = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 44)

# Branded Text
b_brand = draw.textbbox((0, 0), "@animefandom0_0", font=font_brand)
bw = b_brand[2] - b_brand[0]
for dx, dy in [(-3, 0), (3, 0), (0, -3), (0, 3)]:
    draw.text(((1080 - bw)//2 + dx, 880 + dy), "@animefandom0_0", font=font_brand, fill=(0, 0, 0, 255))
draw.text(((1080 - bw)//2, 880), "@animefandom0_0", font=font_brand, fill=(255, 255, 255, 255))

b_sub = draw.textbbox((0, 0), "DAILY PEAK ANIME MOMENTS", font=font_sub)
sw = b_sub[2] - b_sub[0]
draw.text(((1080 - sw)//2, 960), "DAILY PEAK ANIME MOMENTS", font=font_sub, fill=(255, 230, 0, 255))

img.save(outro_png)

outro_mp4 = "output/inhouse_moments/outro_card.mp4"
cmd_outro = [
    "ffmpeg", "-y",
    "-loop", "1", "-i", outro_png,
    "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
    "-t", "2.0",
    "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-r", "30",
    outro_mp4
]
subprocess.run(cmd_outro, check=True)

# 5. Concatenate and Master Audio (EBU R128)
concat_list = "output/inhouse_moments/concat.txt"
with open(concat_list, "w") as f:
    f.write(f"file 'dandadan_moment_base.mp4'\n")
    f.write(f"file 'outro_card.mp4'\n")

final_mastered = "output/inhouse_moments/dandadan_peak_moment_mastered.mp4"
cmd_master = [
    "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list,
    "-af", "loudnorm=I=-14.0:TP=-1.5:LRA=11",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-c:a", "aac", "-b:a", "192k",
    final_mastered
]
subprocess.run(cmd_master, check=True)

# 6. Extract Contact Proof Sheet
proof_jpg = "output/inhouse_moments/dandadan_peak_moment_proof.jpg"
subprocess.run([
    "ffmpeg", "-y", "-i", final_mastered,
    "-vf", "select='not(mod(n\\,90))',scale=360:640,tile=3x3",
    "-frames:v", "1", "-q:v", "2",
    proof_jpg
], check=True)

print(f"\n=======================================================")
print(f"SUCCESS: 100% In-House Moment Short Created!")
print(f"Output Video: {final_mastered}")
print(f"Proof Sheet: {proof_jpg}")
print(f"Hook Title: {hook_title}")
print(f"=======================================================")
