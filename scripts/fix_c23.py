import subprocess, os, json
from PIL import Image, ImageDraw, ImageFont

inp = 'input/group_a_harvest/full_Fate_-hIEMOGO3Go.mp4'
out = 'output/auto_group_c23_one_finger_block_shock_master.mp4'
temp_base = out.replace('.mp4', '_base.mp4')

# Trim to 55.0s so total with 2.0s outro is 57.0s (safely inside Shorts boundary)
cmd = [
    'ffmpeg', '-y', '-i', inp, '-t', '55.0',
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
subprocess.run(cmd, check=True)

# Outro
outro_png = out.replace('.mp4', '_outro.png')
img = Image.new('RGBA', (1080, 1920), (10, 12, 16, 255))
draw = ImageDraw.Draw(img)
font_brand = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 52)
font_label = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 46)
font_tag = ImageFont.truetype('C:/Windows/Fonts/impact.ttf', 64)

bw = draw.textbbox((0,0), '@animefandom0_0', font=font_brand)[2]
draw.text(((1080-bw)//2, 820), '@animefandom0_0', font=font_brand, fill=(255,255,255,255))

lw = draw.textbbox((0,0), 'ORIGINAL CLIP BY', font=font_label)[2]
draw.text(((1080-lw)//2, 910), 'ORIGINAL CLIP BY', font=font_label, fill=(255,230,0,255))

creator_tag = '@FateAnimeHub'
cw = draw.textbbox((0,0), creator_tag, font=font_tag)[2]
for dx, dy in [(-3,0),(3,0),(0,-3),(0,3)]:
    draw.text(((1080-cw)//2+dx, 980+dy), creator_tag, font=font_tag, fill=(0,0,0,255))
draw.text(((1080-cw)//2, 980), creator_tag, font=font_tag, fill=(255,255,255,255))
img.save(outro_png)

temp_outro = out.replace('.mp4', '_outro.mp4')
cmd_o = [
    'ffmpeg', '-y', '-loop', '1', '-i', outro_png,
    '-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=48000',
    '-t', '2.0', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
    '-c:a', 'aac', '-b:a', '192k', '-r', '30', temp_outro
]
subprocess.run(cmd_o, check=True)

concat_txt = out.replace('.mp4', '_concat.txt')
with open(concat_txt, 'w', encoding='utf-8') as f:
    f.write(f"file '{os.path.abspath(temp_base)}'\nfile '{os.path.abspath(temp_outro)}'\n")

cmd_stitch = [
    'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', concat_txt,
    '-c', 'copy', out
]
subprocess.run(cmd_stitch, check=True)

# Cleanup
for tmp in [temp_base, outro_png, temp_outro, concat_txt]:
    if os.path.exists(tmp): os.remove(tmp)

cmd_chk = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'json', out]
d = json.loads(subprocess.check_output(cmd_chk).decode())
print('Fixed C23 duration:', d['format']['duration'])
