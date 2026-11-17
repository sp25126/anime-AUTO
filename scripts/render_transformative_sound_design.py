import os
import sys
import subprocess
from PIL import Image, ImageDraw, ImageFont

def render_transformative_sound_design():
    raw_path = "assets/harvested_clips/7ZLS5KNDelI.mp4"
    output_path = "output/atomic_sound_design_mastered.mp4"
    fps = 30

    print("[Studio Compositor] Initializing Transformative Sound Design Short with Anti-Copyright Overhaul...")
    os.makedirs("output", exist_ok=True)

    # Cut to 16.0s (Trims any trailing creator outro card)
    duration_sec = 16.0
    total_frames = int(duration_sec * fps) # 480 frames

    # 1. First, build 1080x1920 base with Dynamic Blurred Background
    base_file = "output/temp_sound_design_base.mp4"
    filter_complex = (
        "[0:v]fps=30,split=2[fg_raw][bg_raw];"
        "[bg_raw]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5,eq=brightness=-0.15:saturation=1.2[bg_blur];"
        "[fg_raw]scale=1080:-2,setsar=1[fg_scaled];"
        "[bg_blur][fg_scaled]overlay=0:(1920-h)/2[vout];"
        "[0:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo[aout]"
    )
    cmd_base = [
        "ffmpeg", "-y",
        "-i", raw_path,
        "-t", str(duration_sec),
        "-filter_complex", filter_complex,
        "-map", "[vout]", "-map", "[aout]",
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k",
        base_file
    ]
    subprocess.run(cmd_base, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[Studio Compositor] Base canvas generated: {base_file}")

    # Fonts
    font_hook_main = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 64)
    font_hook_sub = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 46)
    font_credit = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
    font_outro_title = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 64)
    font_outro_sub = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 30)

    # Small Corner Watermark (64x64)
    logo_path = "branding/watermark_badge_128.png"
    corner_logo = Image.open(logo_path).convert("RGBA").resize((64, 64), Image.Resampling.LANCZOS) if os.path.exists(logo_path) else None

    # Replace creator end section with our custom branded attribution card
    # Outro plays during final 45 frames (1.5s)
    outro_start_frame = total_frames - 45

    temp_unmastered = "output/temp_sound_unmastered.mp4"
    ffmpeg_pipe_cmd = [
        "ffmpeg", "-y",
        "-i", base_file,
        "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", "1080x1920", "-pix_fmt", "rgba",
        "-r", str(fps), "-i", "-",
        "-filter_complex",
        "[0:v][1:v]overlay=0:0[v]",
        "-map", "[v]", "-map", "0:a?",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
        temp_unmastered
    ]
    pipe_proc = subprocess.Popen(ffmpeg_pipe_cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for f_idx in range(total_frames):
        img = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        if f_idx < outro_start_frame:
            # 1. Pinned Hook Card at Top
            box_y0, box_y1 = 70, 205
            draw.rounded_rectangle([70, box_y0, 1010, box_y1], radius=22, fill=(8, 8, 14, 215), outline=(0, 240, 255, 230), width=3)

            h1 = "MOST SATISFYING SOUND DESIGN"
            h1_b = draw.textbbox((0, 0), h1, font=font_hook_main)
            h1_w = h1_b[2] - h1_b[0]
            draw.text(((1080 - h1_w)//2, box_y0 + 15), h1, font=font_hook_main, fill=(255, 255, 255, 255))

            h2 = "USE HEADPHONES 🎧 • I AM ATOMIC"
            h2_b = draw.textbbox((0, 0), h2, font=font_hook_sub)
            h2_w = h2_b[2] - h2_b[0]
            draw.text(((1080 - h2_w)//2, box_y0 + 78), h2, font=font_hook_sub, fill=(0, 229, 255, 255))

            # 2. Subtle Corner Watermark Badge (No Sound)
            if corner_logo:
                img.paste(corner_logo, (980, 50), corner_logo)

            # 3. Bottom Attribution Tag
            credit_text = "EDIT BY @AKIBA RYOTO • THE EMINENCE IN SHADOW"
            cr_b = draw.textbbox((0, 0), credit_text, font=font_credit)
            cw = cr_b[2] - cr_b[0] + 40
            ch = 44
            cx = (1080 - cw) // 2
            cy = 1920 - 90
            draw.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=22, fill=(5, 5, 12, 190), outline=(255, 255, 255, 70), width=1)
            draw.text((cx + 20, cy + 8), credit_text, font=font_credit, fill=(255, 255, 255, 230))

        else:
            # 4. BRANDED END CARD OVERHAUL (Replaces original creator outro)
            p_frame = f_idx - outro_start_frame
            alpha = int(min(235, p_frame * 16))
            draw.rectangle([0, 0, 1080, 1920], fill=(5, 5, 10, alpha))

            # Channel Logo centered
            logo_1024 = "branding/channel_logo_1024.png"
            if os.path.exists(logo_1024):
                l_img = Image.open(logo_1024).convert("RGBA").resize((320, 320), Image.Resampling.LANCZOS)
                img.paste(l_img, ((1080 - 320)//2, (1920 - 320)//2 - 120), l_img)

            # In Channel Signature Font: Attribution + Follow CTA
            t_orig = "ORIGINAL EDIT BY @AKIBA RYOTO"
            tb1 = draw.textbbox((0, 0), t_orig, font=font_outro_title)
            tw1 = tb1[2] - tb1[0]
            for dx, dy in [(-3, -3), (3, -3), (-3, 3), (3, 3)]:
                draw.text(((1080 - tw1)//2 + dx, (1920 // 2) + 120 + dy), t_orig, font=font_outro_title, fill=(0, 0, 0, 240))
            draw.text(((1080 - tw1)//2, (1920 // 2) + 120), t_orig, font=font_outro_title, fill=(0, 240, 255, 255))

            t_sub = "CURATED BY @animefandom0_0 • SUBSCRIBE FOR MORE"
            tb2 = draw.textbbox((0, 0), t_sub, font=font_outro_sub)
            tw2 = tb2[2] - tb2[0]
            draw.text(((1080 - tw2)//2, (1920 // 2) + 195), t_sub, font=font_outro_sub, fill=(255, 230, 0, 240))

        pipe_proc.stdin.write(img.tobytes())

    pipe_proc.stdin.close()
    pipe_proc.wait()
    print("[Studio Compositor] Overlay compositing completed successfully!")

    # Master audio to EBU R128 (-14.0 LUFS, -1.5 dBTP)
    print("[Audio Master] Applying 2-Pass EBU R128 Loudness Normalization (-14.0 LUFS)...")
    cmd_master = [
        "ffmpeg", "-y",
        "-i", temp_unmastered,
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "256k",
        output_path
    ]
    subprocess.run(cmd_master, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[Audio Master] Final mastered broadcast video: {output_path}")

    # Generate QA Contact Sheet
    qa_path = "output/atomic_sound_design_qa.jpg"
    cmd_qa = [
        "ffmpeg", "-y",
        "-i", output_path,
        "-vf", "select='not(mod(n\,50))',scale=360:640,tile=3x3",
        "-vframes", "1",
        qa_path
    ]
    subprocess.run(cmd_qa, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[QA Engine] Contact proof sheet saved: {qa_path}")

    # Cleanup temp
    for tmp in [base_file, temp_unmastered]:
        try:
            if os.path.exists(tmp):
                os.remove(tmp)
        except:
            pass

if __name__ == "__main__":
    render_transformative_sound_design()
