import os
from PIL import Image

bgs = {
    "romcom_sunset": "assets/backgrounds/romcom_sunset.webp",
    "cyberpunk_moon": "assets/backgrounds/cyberpunk_moon.jpg",
    "sakuga_lightning": "assets/backgrounds/sakuga_lightning.jpg",
    "night_galaxy": "assets/backgrounds/night_galaxy.jpg",
    "ghibli_meadow": "assets/backgrounds/ghibli_meadow.jpg"
}

header_path = "assets/brand_header_card.png"
header = Image.open(header_path).convert("RGBA")

# Extract a representative frame from the Dandadan video
video_frame_path = "output/dandadan_sample_frame.jpg"
if not os.path.exists(video_frame_path):
    os.system(f"ffmpeg -y -ss 00:00:04.0 -i input/dandadan_maid_cafe_raw.mp4 -vframes 1 {video_frame_path}")

raw_frame = Image.open(video_frame_path).convert("RGBA")
# Scale video to 1080x608
vid_scaled = raw_frame.resize((1080, 608), Image.Resampling.LANCZOS)

for name, bg_path in bgs.items():
    if not os.path.exists(bg_path):
        continue
    bg = Image.open(bg_path).convert("RGBA")
    bg = bg.resize((1080, 1920), Image.Resampling.LANCZOS)
    
    # Composite:
    # 1. Background
    # 2. Header card at y=456
    # 3. Video at y=656
    canvas = bg.copy()
    canvas.paste(header, (0, 456), header)
    canvas.paste(vid_scaled, (0, 656))
    
    out_path = f"output/preview_genre_{name}.jpg"
    canvas.convert("RGB").save(out_path, quality=95)
    print(f"Generated preview: {out_path}")
