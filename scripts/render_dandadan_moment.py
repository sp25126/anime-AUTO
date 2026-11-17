import subprocess
import os
from PIL import Image, ImageDraw, ImageFont

def render_dandadan_moment():
    video_raw = "input/dandadan_maid_cafe_raw.mp4"
    bgm_path = "assets/audio/trending_comedy_lofi_bed.mp3"
    header_overlay = "assets/dandadan_header_overlay.png"
    output_master = "output/dandadan_maid_cafe_broadcast.mp4"
    temp_main = "output/dandadan_temp_main.mp4"
    temp_outro = "output/dandadan_temp_outro.mp4"

    os.makedirs("output", exist_ok=True)

    # 1. Generate High-End Outro Card
    outro_img = "assets/dandadan_outro_card.png"
    img = Image.new("RGB", (1080, 1920), (12, 12, 16))
    draw = ImageDraw.Draw(img)
    
    font_impact = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 64)
    font_bold = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 32)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 26)

    # Gradient top/bottom
    for y in range(1920):
        r = int(12 + 10 * (y / 1920.0))
        g = int(12 + 12 * (y / 1920.0))
        b = int(18 + 25 * (y / 1920.0))
        draw.line([(0, y), (1080, y)], fill=(r, g, b))

    # Center Brand Elements
    draw.text((540, 780), "ANIME FANDOM", font=font_impact, fill=(255, 235, 60), anchor="mm")
    draw.text((540, 850), "NEW VIRAL SHORTS DAILY", font=font_bold, fill=(240, 240, 240), anchor="mm")
    draw.text((540, 910), "SUBSCRIBE • LIKE • SHARE", font=font_bold, fill=(255, 100, 100), anchor="mm")
    draw.text((540, 1100), "Dandadan Season 2 • Clip by Netflix Anime", font=font_sub, fill=(160, 160, 160), anchor="mm")
    img.save(outro_img, "PNG")

    # 2. Main Video Staging & Filtergraph
    # [0:a] is voice (sidechain trigger)
    # [1:a] is BGM (ducked music)
    filtergraph = (
        "[0:v]split=2[bg_raw][fg_raw];"
        "[bg_raw]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
        "boxblur=24:5,eq=brightness=-0.12:saturation=1.15[bg_blur];"
        "[fg_raw]scale=1080:-1[fg_sharp];"
        "[bg_blur][fg_sharp]overlay=(W-w)/2:(H-h)/2[staged];"
        "[staged][2:v]overlay=0:0,fps=30,format=yuv420p[v_main];"
        
        # Audio
        "[0:a]asplit=2[voice_main][voice_sc];"
        "[1:a]volume=0.30[bgm_base];"
        "[bgm_base][voice_sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=500[ducked_bgm];"
        "[ducked_bgm]asendcmd=c='10.8 volume volume 0'[muted_bgm];"
        "[voice_main][muted_bgm]amix=inputs=2:duration=first:dropout_transition=0.2[a_mixed];"
        "[a_mixed]loudnorm=I=-14:LRA=7:TP=-2.0[a_main]"
    )

    print("Rendering main 9:16 sequence...")
    cmd_main = [
        "ffmpeg", "-y",
        "-ss", "0.0",
        "-t", "17.6",
        "-i", video_raw,
        "-stream_loop", "-1",
        "-i", bgm_path,
        "-i", header_overlay,
        "-filter_complex", filtergraph,
        "-map", "[v_main]",
        "-map", "[a_main]",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        temp_main
    ]
    res_main = subprocess.run(cmd_main, capture_output=True, text=True)
    if res_main.returncode != 0:
        print("Error on main render:", res_main.stderr[-400:])
        return False

    # 3. Render 30fps Outro Card
    print("Rendering outro sequence...")
    cmd_outro = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-t", "2.4",
        "-i", outro_img,
        "-f", "lavfi", "-t", "2.4", "-i", "anullsrc=r=44100:cl=stereo",
        "-filter_complex", "[0:v]scale=1080:1920,fps=30,format=yuv420p[v_out]",
        "-map", "[v_out]",
        "-map", "1:a",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        temp_outro
    ]
    res_outro = subprocess.run(cmd_outro, capture_output=True, text=True)
    if res_outro.returncode != 0:
        print("Error on outro render:", res_outro.stderr[-300:])
        return False

    # 4. Seamless Resampled Concat (0 Stuck Frames)
    print("Executing resampled concat master...")
    cmd_concat = [
        "ffmpeg", "-y",
        "-i", temp_main,
        "-i", temp_outro,
        "-filter_complex", (
            "[0:v]fps=30,scale=1080:1920[v0];"
            "[1:v]fps=30,scale=1080:1920[v1];"
            "[v0][0:a][v1][1:a]concat=n=2:v=1:a=1[v_final][a_final]"
        ),
        "-map", "[v_final]",
        "-map", "[a_final]",
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "18",
        "-c:a", "aac",
        "-b:a", "192k",
        output_master
    ]
    res_concat = subprocess.run(cmd_concat, capture_output=True, text=True)

    # Cleanup temp
    if os.path.exists(temp_main): os.remove(temp_main)
    if os.path.exists(temp_outro): os.remove(temp_outro)

    if res_concat.returncode == 0:
        print(f"Master successfully created: {output_master}")
        return True
    else:
        print("Concat error:", res_concat.stderr[-300:])
        return False

if __name__ == "__main__":
    render_dandadan_moment()
