import subprocess
import os
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

raw_file = "assets/rotate_raw/aWApEIyXUp4.mp4"
base_file = "output/rotate_base.mp4"
os.makedirs("output", exist_ok=True)

# Slicing the prime 30s battle climax:
# Dynamic Blurred Background + centered 16:9 foreground
# Sits ready for the rotate-phone animation overlay and branding HUD
filter_complex = (
    "[0:v]fps=30,split=2[fg_raw][bg_raw];"
    "[bg_raw]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5,eq=brightness=-0.15:saturation=1.2[bg_blur];"
    "[fg_raw]scale=1080:-2,setsar=1[fg_scaled];"
    "[bg_blur][fg_scaled]overlay=0:(1920-h)/2[vout];"
    "[0:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo[aout]"
)

cmd = [
    "ffmpeg", "-y",
    "-ss", "2.0",
    "-i", raw_file,
    "-t", "30.0",
    "-filter_complex", filter_complex,
    "-map", "[vout]", "-map", "[aout]",
    "-c:v", "libx264", "-preset", "ultrafast", "-crf", "18",
    "-c:a", "aac", "-b:a", "192k",
    base_file
]

print("Rendering rotate base video with dynamic blurred background...")
subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Base video ready:", base_file)
