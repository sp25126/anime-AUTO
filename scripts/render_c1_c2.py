import os
import sys
import json
import subprocess
from PIL import Image, ImageDraw, ImageFont

def render_group_c_short(input_clip, output_path, creator_tag, anime_name, max_dur=57.5):
    # 1. Probe duration
    probe_cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'json', input_clip]
    d = json.loads(subprocess.check_output(probe_cmd).decode('utf-8'))
    tot = float(d['format']['duration'])
    trim_dur = min(tot, max_dur)
    print(f"  Raw Duration: {tot:.2f}s | Full Scene Preserved: {trim_dur:.2f}s (+ 2.0s outro)")
    
    # 2. Render 16:9 uncropped over dynamic blurred background + EBU R128 audio
    temp_base = output_path.replace('.mp4', '_base.mp4')
    cmd = [
        'ffmpeg', '-y', '-ss', '0', '-t', str(trim_dur), '-i', input_clip,
        '-filter_complex',
        '[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5,eq=brightness=-0.15:contrast=1.05[bg];'
        '[0:v]scale=1080:-1[fg];'
        '[bg][fg]overlay=0:(1920-h)/2[v];'
        '[0:a]aresample=48000,loudnorm=I=-14:TP=-1.5:LRA=11[a]',
        '-map', '[v]', '-map', '[a]',
        '-c:v', 'libx264', '-preset', 'fast', '-crf', '18',
        '-c:a', 'aac', '-b:a', '192k',
        temp_base
    ]
    subprocess.run(cmd, check=True)
    
    # 3. Create Pillow outro card (2 seconds)
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
    subprocess.run(cmd_o, check=True)
    
    # 4. Concat base + outro
    concat_txt = output_path.replace('.mp4', '_concat.txt')
    with open(concat_txt, 'w', encoding='utf-8') as f:
        f.write(f"file '{os.path.abspath(temp_base)}'\nfile '{os.path.abspath(temp_outro)}'\n")
    
    cmd_stitch = [
        'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', concat_txt,
        '-c', 'copy', output_path
    ]
    subprocess.run(cmd_stitch, check=True)
    print(f'Successfully rendered: {output_path}')

if __name__ == '__main__':
    print('[RENDERING C1: Accidental Rizz]...')
    render_group_c_short('input/test_c1_candidate.mp4', 'output/auto_group_c1_accidental_rizz_master.mp4', '@Crunchyroll', 'The Apothecary Diaries')
    print('[RENDERING C2: Tsundere Blush]...')
    render_group_c_short('input/test_c2_candidate.mp4', 'output/auto_group_c2_tsundere_blush_master.mp4', '@5yenAnime', 'Kaguya-sama')
    print('ALL GROUP C TESTING MASTERS RENDERED!')
