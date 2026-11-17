import subprocess
import os
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"
os.makedirs("output", exist_ok=True)

# Test clip: hasib_sample_full.mp4 (Gojo ignores a beauty, 25s) with full audio
input_clip = "output/dissections/hasib_sample_full.mp4"
creator_tag = "@hasibkunamv"
anime_title = "Jujutsu Kaisen"
hook_title = "Bro Ignored A Beauty Without Even Trying 💀 | Jujutsu Kaisen #shorts #anime"

# 1. Get exact duration
probe_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", input_clip]
probe_data = json.loads(subprocess.check_output(probe_cmd).decode("utf-8"))
total_duration = float(probe_data["format"]["duration"])
# Trim the last 2 seconds to remove creator end bumper
trim_duration = max(5.0, total_duration - 2.0)
print(f"Total Duration: {total_duration:.2f}s | Trimming to: {trim_duration:.2f}s")

# 2. Render trimmed base video with dynamic blurred background (1080x1920)
trimmed_base = "output/group_c_base_trimmed.mp4"
cmd_base = [
    "ffmpeg", "-y", "-ss", "0", "-t", str(trim_duration), "-i", input_clip,
    "-filter_complex",
    "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5,eq=brightness=-0.15:contrast=1.05[bg];"
    "[0:v]scale=1080:-1[fg];"
    "[bg][fg]overlay=0:(1920-h)/2[v]",
    "-map", "[v]", "-map", "0:a",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-c:a", "aac", "-b:a", "192k",
    trimmed_base
]
print("Rendering trimmed 9:16 base with blurred background...")
subprocess.run(cmd_base, check=True)

# 3. Create branded Outro Card using Pillow (Rock Solid, Zero Fontconfig crash)
# Text: ORIGINAL EDIT BY @hasibkunamv | Channel: @animefandom0_0
from PIL import Image, ImageDraw, ImageFont

outro_png = "output/group_c_outro_card.png"
img = Image.new("RGBA", (1080, 1920), (10, 12, 16, 255))
draw = ImageDraw.Draw(img)

font_tag = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 64)
font_label = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 46)
font_brand = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 52)

# Channel badge
b_brand = draw.textbbox((0, 0), "@animefandom0_0", font=font_brand)
bw = b_brand[2] - b_brand[0]
draw.text(((1080 - bw)//2, 820), "@animefandom0_0", font=font_brand, fill=(255, 255, 255, 255))

# Original edit by
b_lbl = draw.textbbox((0, 0), "ORIGINAL EDIT BY", font=font_label)
lw = b_lbl[2] - b_lbl[0]
draw.text(((1080 - lw)//2, 910), "ORIGINAL EDIT BY", font=font_label, fill=(255, 230, 0, 255))

# Creator tag
b_cre = draw.textbbox((0, 0), creator_tag, font=font_tag)
cw = b_cre[2] - b_cre[0]
# Black outline
for dx, dy in [(-3, 0), (3, 0), (0, -3), (0, 3), (-2, -2), (2, 2)]:
    draw.text(((1080 - cw)//2 + dx, 980 + dy), creator_tag, font=font_tag, fill=(0, 0, 0, 255))
draw.text(((1080 - cw)//2, 980), creator_tag, font=font_tag, fill=(255, 255, 255, 255))

img.save(outro_png)
print("Saved Pillow outro card PNG...")

outro_video = "output/group_c_outro_card.mp4"
outro_cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-i", outro_png,
    "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
    "-t", "2.0",
    "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k",
    "-r", "30",
    outro_video
]
print("Rendering branded attribution outro card MP4...")
subprocess.run(outro_cmd, check=True)

# 4. Concatenate trimmed base + branded outro card
concat_list = "output/group_c_concat.txt"
with open(concat_list, "w") as f:
    f.write(f"file 'group_c_base_trimmed.mp4'\n")
    f.write(f"file 'group_c_outro_card.mp4'\n")

final_concat = "output/group_c_accidental_rizz_mastered.mp4"
concat_cmd = [
    "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_list,
    "-af", "loudnorm=I=-14.0:TP=-1.5:LRA=11",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-c:a", "aac", "-b:a", "192k",
    final_concat
]
print("Mastering final video with EBU R128 audio...")
subprocess.run(concat_cmd, check=True)

# 5. Extract contact proof sheet for verification
proof_sheet = "output/group_c_accidental_rizz_proof.jpg"
subprocess.run([
    "ffmpeg", "-y", "-i", final_concat,
    "-vf", "select='not(mod(n\\,90))',scale=360:640,tile=3x3",
    "-frames:v", "1", "-q:v", "2",
    proof_sheet
], check=True)

print(f"SUCCESS: Rendered {final_concat} & Proof {proof_sheet}")
