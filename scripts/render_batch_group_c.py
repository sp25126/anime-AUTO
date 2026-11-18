#!/usr/bin/env python3
"""
Master Group C Micro-Moment Pipeline & Batch Renderer
Channel: @animefandom0_0
Renders viral 20s-35s single uncut dialogue/action moments across Group C subcategories:
16:9 uncropped anime centered over dynamic blurred background + EBU R128 (-14.0 LUFS) audio + 2.0s branded attribution outro card.
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = WORKSPACE_ROOT / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

def render_group_c_short(input_clip: str, output_path: str, creator_tag: str, anime_name: str, max_dur: float = 57.5) -> str:
    print(f"\n[Group C Renderer] Processing: {Path(input_clip).name} -> {Path(output_path).name}")
    probe_cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'json', str(input_clip)]
    d = json.loads(subprocess.check_output(probe_cmd).decode('utf-8'))
    tot = float(d['format']['duration'])
    
    # User directive: Show the full scene or as much as possible, leaving 2.0s for the branded attribution outro card (YouTube Shorts limit = 60s)
    trim_dur = min(tot, max_dur)
    print(f"  Raw Duration: {tot:.2f}s | Preserving Full Scene: {trim_dur:.2f}s (+ 2.0s outro card)")
    
    # 1. 16:9 uncropped over dynamic blurred background + EBU R128 audio (-14.0 LUFS, -1.5 TP)
    temp_base = output_path.replace('.mp4', '_base.mp4')
    cmd = [
        'ffmpeg', '-y', '-ss', '0', '-t', str(trim_dur), '-i', str(input_clip),
        '-filter_complex',
        '[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5,eq=brightness=-0.15:contrast=1.05[bg];'
        '[0:v]scale=1080:-1[fg];'
        '[bg][fg]overlay=0:(1920-h)/2[v];'
        '[0:a]aresample=48000,loudnorm=I=-14.0:TP=-1.5:LRA=11[a]',
        '-map', '[v]', '-map', '[a]',
        '-c:v', 'libx264', '-preset', 'fast', '-crf', '18',
        '-c:a', 'aac', '-b:a', '192k',
        temp_base
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    # 2. 2-second Pillow Outro Attribution Card
    outro_png = output_path.replace('.mp4', '_outro.png')
    img = Image.new('RGBA', (1080, 1920), (10, 12, 16, 255))
    draw = ImageDraw.Draw(img)
    font_brand = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 52)
    font_label = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 46)
    font_tag = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 64)
    
    bw = draw.textbbox((0,0), '@animefandom0_0', font=font_brand)[2]
    draw.text(((1080-bw)//2, 820), '@animefandom0_0', font=font_brand, fill=(255,255,255,255))
    
    lw = draw.textbbox((0,0), 'ORIGINAL CLIP BY', font=font_label)[2]
    draw.text(((1080-lw)//2, 910), 'ORIGINAL CLIP BY', font=font_label, fill=(255,230,0,255))
    
    cw = draw.textbbox((0,0), creator_tag, font=font_tag)[2]
    for dx, dy in [(-3,0),(3,0),(0,-3),(0,3)]:
        draw.text(((1080-cw)//2+dx, 980+dy), creator_tag, font=font_tag, fill=(0,0,0,255))
    draw.text(((1080-cw)//2, 980), creator_tag, font=font_tag, fill=(255,255,255,255))
    img.save(outro_png)
    
    temp_outro = output_path.replace('.mp4', '_outro.mp4')
    cmd_o = [
        'ffmpeg', '-y', '-loop', '1', '-i', outro_png,
        '-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=48000',
        '-t', '2.0', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
        '-c:a', 'aac', '-b:a', '192k', '-r', '30', temp_outro
    ]
    subprocess.run(cmd_o, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    # 3. Concatenate base + outro
    concat_txt = output_path.replace('.mp4', '_concat.txt')
    with open(concat_txt, 'w', encoding='utf-8') as f:
        f.write(f"file '{os.path.abspath(temp_base)}'\nfile '{os.path.abspath(temp_outro)}'\n")
    
    cmd_stitch = [
        'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', concat_txt,
        '-c', 'copy', output_path
    ]
    subprocess.run(cmd_stitch, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    print(f"  ✅ Render complete: {output_path}")
    return output_path

GROUP_C_TARGETS = [
    {
        "id": "c3",
        "key": "moment_brutal_reality_check",
        "input": "input/test_b3_candidate.mp4",
        "output": "output/auto_group_c3_brutal_reality_check_master.mp4",
        "creator": "@SakugaAnime",
        "anime": "Demon Slayer",
        "hook": "The Exact Second He Realized He Messed Up 💀 | Brutal Reality Check #shorts #anime",
        "theme": "The Brutal Reality Check / Arrogance Crushed"
    },
    {
        "id": "c4",
        "key": "moment_character_rage_snap",
        "input": "input/test_b7_candidate.mp4",
        "output": "output/auto_group_c4_character_rage_snap_master.mp4",
        "creator": "@RageClips",
        "anime": "Hunter x Hunter",
        "hook": "The Moment The Calm Character Finally Snapped 😱⚡ | Rage Snap #shorts #anime",
        "theme": "When The Gentle Character Finally Snaps"
    },
    {
        "id": "c5",
        "key": "moment_cold_verbal_violation",
        "input": "input/test_b5_candidate.mp4",
        "output": "output/auto_group_c5_cold_verbal_violation_master.mp4",
        "creator": "@BleachClips",
        "anime": "Bleach TYBW",
        "hook": "Bro Didn't Have To Disrespect Him Like That 😭💀 | Verbal Violation #shorts #anime",
        "theme": "Coldest Verbal Disrespect & One-Liners"
    },
    {
        "id": "c6",
        "key": "moment_clutch_savior_arrival",
        "input": "input/test_b4_candidate.mp4",
        "output": "output/auto_group_c6_clutch_savior_arrival_master.mp4",
        "creator": "@DBZClips",
        "anime": "Dragon Ball Super",
        "hook": "When All Hope Was Lost... HE ARRIVED 🥶🔥 | Savior Arrival #shorts #anime",
        "theme": "Peak Emotional Clutch Rescue (Savior Arrival)"
    },
    {
        "id": "c7",
        "key": "moment_unhinged_comedy_gag",
        "input": "input/dandadan_maid_cafe_raw.mp4",
        "output": "output/auto_group_c7_unhinged_comedy_gag_master.mp4",
        "creator": "@AnimeComedyHub",
        "anime": "Dandadan",
        "hook": "Anime Moments That Feel Completely Illegal 😂💀 | Dandadan #shorts #anime",
        "theme": "Unhinged / Out-of-Context Deranged Gags"
    }
]

def batch_render_c3_to_c7():
    print("=" * 70)
    print("🎬 BATCH RENDERING GROUP C SUB-CATEGORIES (C3 TO C7)")
    print("=" * 70)
    rendered = []
    for target in GROUP_C_TARGETS:
        inp = target["input"]
        out = target["output"]
        if not os.path.exists(inp):
            print(f"⚠️ Input not found: {inp}, skipping {target['id']}")
            continue
        res = render_group_c_short(
            input_clip=inp,
            output_path=out,
            creator_tag=target["creator"],
            anime_name=target["anime"],
            max_dur=57.5
        )
        rendered.append((target, res))
    print(f"\n🎉 Successfully rendered {len(rendered)} Group C masters!")
    return rendered

if __name__ == "__main__":
    batch_render_c3_to_c7()
