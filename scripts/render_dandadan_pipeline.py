import subprocess
import os
import json
from PIL import Image, ImageDraw, ImageFont

def create_hud_overlay(width=1080, height=1920):
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Official channel logo watermark at top-right
    logo_path = "branding/watermark_badge_128.png"
    if os.path.exists(logo_path):
        badge = Image.open(logo_path).convert("RGBA")
        img.paste(badge, (width - 150, 40), badge)
        
    return img

def create_rank_badge(rank, title, creator, width=1080, height=1920):
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Pill box background
    box_x0, box_y0 = 60, 50
    box_x1, box_y1 = width - 180, 150
    draw.rounded_rectangle([box_x0, box_y0, box_x1, box_y1], radius=24, fill=(10, 10, 15, 210), outline=(255, 45, 85, 255), width=3)
    
    # Load fonts
    try:
        font_rank = ImageFont.truetype("arialbd.ttf", 52)
        font_sub = ImageFont.truetype("arial.ttf", 26)
    except:
        font_rank = font_sub = ImageFont.load_default()
        
    # Draw Rank & Anime Header
    draw.text((box_x0 + 25, box_y0 + 15), f"TOP {rank} • DANDADAN 4K", font=font_rank, fill=(255, 255, 255))
    draw.text((box_x0 + 28, box_y0 + 68), f"CR: @{creator} | @animefandom0_0", font=font_sub, fill=(0, 240, 255))
    
    return img

def render_dandadan_compilation():
    with open("output/dandadan_prepared_cuts.json", encoding="utf-8") as f:
        clips = json.load(f)
        
    os.makedirs("output/temp_dandadan", exist_ok=True)
    processed_clips = []
    
    for idx, c in enumerate(clips):
        rank = c["rank"]
        in_file = c["path"]
        badge_img = create_rank_badge(rank, "DANDADAN", c["creator"])
        badge_path = f"output/temp_dandadan/badge_rank_{rank}.png"
        badge_img.save(badge_path)
        
        watermark_img = create_hud_overlay()
        watermark_path = f"output/temp_dandadan/watermark.png"
        watermark_img.save(watermark_path)
        
        out_segment = f"output/temp_dandadan/segment_{idx}_{rank}.mp4"
        print(f"Compositing Rank #{rank} overlay...")
        
        # Overlay badge and watermark onto segment
        cmd = [
            "ffmpeg", "-y",
            "-i", in_file,
            "-i", badge_path,
            "-i", watermark_path,
            "-filter_complex", "[0:v][1:v]overlay=0:0[v1];[v1][2:v]overlay=0:0[vout]",
            "-map", "[vout]", "-map", "0:a",
            "-c:v", "libx264", "-preset", "ultrafast", "-crf", "18",
            "-c:a", "copy",
            out_segment
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        processed_clips.append(out_segment)
        
    # Concat file list
    concat_list_file = "output/temp_dandadan/concat_list.txt"
    with open(concat_list_file, "w") as f:
        for p in processed_clips:
            f.write(f"file '{os.path.abspath(p)}'\n")
            
    unmastered = "output/dandadan_unmastered.mp4"
    print("Concatenating all 5 countdown segments...")
    cmd_concat = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_list_file,
        "-c", "copy",
        unmastered
    ]
    subprocess.run(cmd_concat, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Audio Loudness Mastering to EBU R128 (-14.0 LUFS, -1.5 dBTP)
    mastered = "output/ranking_dandadan_booming_mastered.mp4"
    print("Mastering final audio to YouTube Shorts EBU R128 (-14.0 LUFS)...")
    cmd_master = [
        "ffmpeg", "-y",
        "-i", unmastered,
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "256k",
        mastered
    ]
    subprocess.run(cmd_master, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Master render complete: {mastered}")
    
    # Generate QA sheet
    qa_path = "output/ranking_dandadan_booming_qa.jpg"
    cmd_qa = [
        "ffmpeg", "-y",
        "-i", mastered,
        "-vf", "select='not(mod(n\,180))',scale=360:640,tile=3x3",
        "-vframes", "1",
        qa_path
    ]
    subprocess.run(cmd_qa, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"QA sheet saved: {qa_path}")

if __name__ == "__main__":
    render_dandadan_compilation()
