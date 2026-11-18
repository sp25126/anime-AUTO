import subprocess
import os
from PIL import Image, ImageDraw, ImageFont

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"
os.makedirs("output", exist_ok=True)

raw_clip = "output/nolonger_source.mp4"
bgm_file = "output/lofi_rizz_bgm.wav"

# Microsecond-accurate narrative boundaries:
# 111.2s: Girl shouts "WHAT ARE YOU TALKING ABOUT?!" (Instant conflict hook)
# 115.8s: Sensei calm turn: "Back then I lost my mind... You must be feeling the same right now..."
# 125.8s: Accidental Rizz Climax: "Because you have such sad eyes... Won't you tell me why?"
# 135.8s: Punchline: "...Father?" (Music mutes, stunned comedic silence)
# 138.5s: Scene lands on stunned reaction hold -> Cut to outro!
start_sec = 111.2
end_sec = 138.5
duration_sec = end_sec - start_sec # 27.3 seconds

print(f"Narrative arc: {start_sec:.2f}s to {end_sec:.2f}s (Duration: {duration_sec:.2f}s)")

# Filter complex:
# 1. Background: Warm aesthetic blur (Romance/Rizz) with soft vignette
# 2. Foreground: Native 16:9 centered with original Crunchyroll English subtitles
# 3. Audio: Anime dialogue (main) + ducked BGM with punchline mute at 24.5s (135.7s)
filter_complex = (
    # Background blurred stream
    f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
    f"boxblur=24:4,eq=saturation=1.22:brightness=0.02:gamma_r=1.06:gamma_b=0.96,vignette=angle=PI/6[bg];"
    # Foreground sharp stream
    f"[0:v]scale=1080:-1[fg];"
    # Overlay with 30fps
    f"[bg][fg]overlay=0:(1920-h)/2,fps=30[v_base];"
    # Audio: Ducked BGM that mutes right on the punchline (at 24.5s)
    f"[1:a]volume=0.22,atrim=0:{duration_sec},afade=t=out:st=24.2:d=0.3[bgm];"
    f"[0:a]volume=1.0[dialogue];"
    f"[dialogue][bgm]amix=inputs=2:duration=first:dropout_transition=2[a_base]"
)

base_mp4 = "output/perfect_base.mp4"
cmd_base = [
    "ffmpeg", "-y",
    "-ss", f"{start_sec:.2f}", "-t", f"{duration_sec:.2f}", "-i", raw_clip,
    "-i", bgm_file,
    "-filter_complex", filter_complex,
    "-map", "[v_base]", "-map", "[a_base]",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
    base_mp4
]
print("1. Rendering perfectly framed base clip with punchline bed mute...")
subprocess.run(cmd_base, check=True)

# 2. Render Branded Outro Card (2 seconds @ 30fps, 48000Hz)
print("2. Generating branded outro card...")
outro_png = "output/perfect_outro_card.png"
img = Image.new("RGBA", (1080, 1920), (12, 14, 18, 255))
draw = ImageDraw.Draw(img)

font_brand = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 56)
font_sub = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 44)

b_brand = draw.textbbox((0, 0), "@animefandom0_0", font=font_brand)
bw = b_brand[2] - b_brand[0]
for dx, dy in [(-3, 0), (3, 0), (0, -3), (0, 3)]:
    draw.text(((1080 - bw)//2 + dx, 880 + dy), "@animefandom0_0", font=font_brand, fill=(0, 0, 0, 255))
draw.text(((1080 - bw)//2, 880), "@animefandom0_0", font=font_brand, fill=(255, 255, 255, 255))

b_sub = draw.textbbox((0, 0), "DAILY PEAK ANIME MOMENTS", font=font_sub)
sw = b_sub[2] - b_sub[0]
draw.text(((1080 - sw)//2, 960), "DAILY PEAK ANIME MOMENTS", font=font_sub, fill=(255, 230, 0, 255))
img.save(outro_png)

outro_mp4 = "output/perfect_outro_card.mp4"
cmd_outro = [
    "ffmpeg", "-y",
    "-loop", "1", "-i", outro_png,
    "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
    "-t", "2.0",
    "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-r", "30", "-ar", "48000",
    outro_mp4
]
subprocess.run(cmd_outro, check=True)

# 3. Seamless Concat with Filtergraph (Zero Freeze)
print("3. Concatenating base + outro using filtercomplex (zero freeze)...")
final_mastered = "output/nolonger_perfect_cut_mastered.mp4"
concat_filter = (
    "[0:v]fps=30,scale=1080:1920[v0];"
    "[1:v]fps=30,scale=1080:1920[v1];"
    "[0:a]aformat=sample_rates=48000:channel_layouts=stereo[a0];"
    "[1:a]aformat=sample_rates=48000:channel_layouts=stereo[a1];"
    "[v0][a0][v1][a1]concat=n=2:v=1:a=1[v_out][a_concat];"
    "[a_concat]loudnorm=I=-14.0:TP=-1.5:LRA=11[a_out]"
)

cmd_concat = [
    "ffmpeg", "-y",
    "-i", base_mp4,
    "-i", outro_mp4,
    "-filter_complex", concat_filter,
    "-map", "[v_out]", "-map", "[a_out]",
    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
    "-c:a", "aac", "-b:a", "192k",
    final_mastered
]
subprocess.run(cmd_concat, check=True)

# 4. Generate QA Proof Sheet
print("4. Generating contact proof sheet...")
proof_sheet = "output/nolonger_perfect_cut_proof.jpg"
subprocess.run([
    "ffmpeg", "-y", "-i", final_mastered,
    "-vf", "select='not(mod(n\\,90))',scale=360:640,tile=3x3",
    "-frames:v", "1", "-q:v", "2",
    proof_sheet
], check=True)

print(f"\n=======================================================")
print(f"SUCCESS: Mastered Video Rendered with Perfect Cut!")
print(f"Path: {final_mastered}")
print(f"Proof: {proof_sheet}")
print(f"=======================================================")
