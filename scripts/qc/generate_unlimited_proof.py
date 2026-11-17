import subprocess
import os
from PIL import Image, ImageDraw, ImageFont

def generate_unlimited_proof_sheet(video_path="output/dandadan_unlimited_master.mp4", out_proof="output/dandadan_unlimited_proof.jpg"):
    timestamps = [
        ("00:02.5", "01. Slow-Zoom Sunset BG & Brand Header"),
        ("00:07.0", "02. Dialogue & Clean Subtitle Staging"),
        ("00:11.5", "03. Deadpan Punchline Audio Mute Beat"),
        ("00:15.5", "04. Comedic Climax & Expression"),
        ("00:18.8", "05. Seamless 30fps Outro Card")
    ]
    
    extracted_frames = []
    for i, (ts, label) in enumerate(timestamps):
        tmp_frame = f"output/proof_tmp_{i}.jpg"
        subprocess.run([
            "ffmpeg", "-y", "-ss", ts, "-i", video_path,
            "-vframes", "1", "-q:v", "2", tmp_frame
        ], capture_output=True)
        if os.path.exists(tmp_frame):
            extracted_frames.append((tmp_frame, label))
            
    # Composite into a 5-panel horizontal strip (1080x1920 scaled to 360x640 each -> 1800 x 690)
    w, h = 360, 640
    margin_top = 50
    margin_side = 10
    total_w = (w + margin_side) * len(extracted_frames) + margin_side
    total_h = h + margin_top + 20
    
    proof_img = Image.new("RGB", (total_w, total_h), (12, 16, 24))
    draw = ImageDraw.Draw(proof_img)
    
    for i, (f_path, label) in enumerate(extracted_frames):
        im = Image.open(f_path).resize((w, h), Image.Resampling.LANCZOS)
        x = margin_side + i * (w + margin_side)
        y = margin_top
        proof_img.paste(im, (x, y))
        draw.rectangle([x, y, x+w, y+h], outline=(0, 240, 255), width=2)
        draw.text((x + 10, 15), label, fill=(255, 255, 255))
        if os.path.exists(f_path):
            os.remove(f_path)
            
    proof_img.save(out_proof, quality=95)
    print(f"Proof sheet saved to {out_proof}")

if __name__ == "__main__":
    generate_unlimited_proof_sheet()
