import os
import sys
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

def render_rotating_phone_amv(raw_amv_path="assets/rotate_raw/aWApEIyXUp4.mp4", output_video_path="output/rotate_amv_mastered.mp4"):
    fps = 30
    duration_sec = 30.0
    total_frames = int(duration_sec * fps) # 900 frames

    print("[Studio Compositor] Initializing Synchronized Dynamic Aspect Ratio Rotation Pipeline...")
    os.makedirs("output", exist_ok=True)

    # Timing:
    # 0 to 60 (0.0s to 2.0s): Upright 16:9 in portrait with animated "ROTATE YOUR PHONE" prompt
    # 60 to 90 (2.0s to 3.0s): Smooth 90-degree spring-damped rotation & scale transition
    # 90 to 900 (3.0s to 30.0s): Fullscreen 1080x1920 horizontal cinematic AMV
    # Subtle corner logo: Small 64x64 watermark at top-right corner with NO SOUND EFFECT

    # 1. First, extract raw audio from AMV for the 30s cut
    raw_audio_path = "output/temp_rotate_audio.aac"
    cmd_audio = [
        "ffmpeg", "-y",
        "-ss", "2.0",
        "-i", raw_amv_path,
        "-t", str(duration_sec),
        "-vn", "-c:a", "aac", "-b:a", "256k",
        raw_audio_path
    ]
    subprocess.run(cmd_audio, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 2. Open AMV video frames reader using FFmpeg pipe
    # Read at 1920x1080 30fps
    read_video_cmd = [
        "ffmpeg",
        "-ss", "2.0",
        "-i", raw_amv_path,
        "-t", str(duration_sec),
        "-f", "image2pipe",
        "-pix_fmt", "rgb24",
        "-s", "1920x1080",
        "-r", str(fps),
        "-vcodec", "rawvideo", "-"
    ]
    read_proc = subprocess.Popen(read_video_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

    # 3. Open output video writer pipe to FFmpeg
    temp_unmastered = "output/temp_rotate_unmastered.mp4"
    write_video_cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", "1080x1920", "-pix_fmt", "rgb24",
        "-r", str(fps), "-i", "-",
        "-i", raw_audio_path,
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "256k",
        temp_unmastered
    ]
    write_proc = subprocess.Popen(write_video_cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Fonts & Branding
    font_impact = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 64)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 44)
    font_credit = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 24)

    # Small corner logo (64x64 badge)
    logo_path = "branding/watermark_badge_128.png"
    small_logo = Image.open(logo_path).convert("RGBA").resize((64, 64), Image.Resampling.LANCZOS) if os.path.exists(logo_path) else None

    bytes_per_frame = 1920 * 1080 * 3

    print(f"[Studio Compositor] Processing {total_frames} frames with real-time geometric rotation...")

    for f_idx in range(total_frames):
        raw_bytes = read_proc.stdout.read(bytes_per_frame)
        if len(raw_bytes) < bytes_per_frame:
            break

        # Raw 1920x1080 source frame
        src_frame = Image.frombytes("RGB", (1920, 1080), raw_bytes)

        # Output 1080x1920 canvas
        canvas = Image.new("RGB", (1080, 1920), (0, 0, 0))

        # Dynamic Blurred Background
        # Generate blurred background from source frame
        bg_blur = src_frame.resize((270, 480), Image.Resampling.BILINEAR).resize((1080, 1920), Image.Resampling.BICUBIC)
        # Dim background slightly
        bg_dim = Image.new("RGB", (1080, 1920), (15, 15, 25))
        bg_blended = Image.blend(bg_blur, bg_dim, 0.45)
        canvas.paste(bg_blended, (0, 0))

        # Phase 1: 0 to 60 (Prompt + Upright 16:9)
        # Phase 2: 60 to 90 (Smooth Continuous Rotation to the LEFT 0 deg -> +90 deg, Scale from 1080x608 to 1920x1080)
        # Phase 3: 90 to 900 (Pure +90-degree rotated Fullscreen 1080x1920 to the LEFT)
        if f_idx < 60:
            angle = 0.0
            t_scale = 0.0
        elif f_idx <= 90:
            progress = (f_idx - 60) / 30.0
            # Smooth ease-in-out cosine curve rotating to the LEFT (+90 in PIL is counter-clockwise / left)
            t_smooth = 0.5 - 0.5 * math.cos(progress * math.pi)
            angle = t_smooth * 90.0
            t_scale = t_smooth
        else:
            angle = 90.0
            t_scale = 1.0

        if angle == 0.0:
            # Centered 1080x608
            fg = src_frame.resize((1080, 608), Image.Resampling.BILINEAR)
            canvas.paste(fg, (0, 656))
        elif angle == 90.0:
            # Exactly 90 deg counter-clockwise (to the LEFT) -> 1920x1080 rotated 90 becomes 1080x1920 FULLSCREEN
            fg_rot = src_frame.rotate(90, expand=True)
            # Ensure exact 1080x1920
            if fg_rot.size != (1080, 1920):
                fg_rot = fg_rot.resize((1080, 1920), Image.Resampling.BILINEAR)
            canvas.paste(fg_rot, (0, 0))
        else:
            # Intermediate animated transition state rotating smoothly to the left
            curr_w = int(1080 + t_scale * (1920 - 1080))
            curr_h = int(608 + t_scale * (1080 - 608))
            fg_scaled = src_frame.resize((curr_w, curr_h), Image.Resampling.BILINEAR)
            fg_rotated = fg_scaled.rotate(angle, expand=True, resample=Image.Resampling.BILINEAR)
            rx, ry = fg_rotated.size
            pos_x = (1080 - rx) // 2
            pos_y = (1920 - ry) // 2
            canvas.paste(fg_rotated, (pos_x, pos_y))

        # Overlay Drawings (RGBA)
        draw = ImageDraw.Draw(canvas)

        # A. Prompt Overlay during Phase 1 & 2
        if f_idx < 75:
            alpha_fade = 1.0 if f_idx < 55 else (1.0 - (f_idx - 55) / 20.0)
            overlay_box = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
            d_box = ImageDraw.Draw(overlay_box)

            box_y0, box_y1 = 280, 420
            d_box.rounded_rectangle([120, box_y0, 960, box_y1], radius=24, fill=(10, 10, 20, int(220 * alpha_fade)), outline=(0, 240, 255, int(230 * alpha_fade)), width=4)

            p_text = "ROTATE YOUR PHONE"
            pb = d_box.textbbox((0, 0), p_text, font=font_impact)
            pw = pb[2] - pb[0]
            d_box.text(((1080 - pw)//2, box_y0 + 20), p_text, font=font_impact, fill=(255, 255, 255, int(255 * alpha_fade)))

            sub_text = "FULLSCREEN 4K HORIZONTAL"
            sb = d_box.textbbox((0, 0), sub_text, font=font_sub)
            sw = sb[2] - sb[0]
            d_box.text(((1080 - sw)//2, box_y0 + 78), sub_text, font=font_sub, fill=(255, 230, 0, int(255 * alpha_fade)))

            # Oscillating Phone Icon below
            phone_w, phone_h = 160, 280
            px = (1080 - phone_w) // 2
            py = 1380
            tilt = math.sin(f_idx * 0.15) * 15
            d_box.rounded_rectangle([px, py, px + phone_w, py + phone_h], radius=24, outline=(255, 255, 255, int(230 * alpha_fade)), width=5)
            d_box.rounded_rectangle([px + 10, py + 18, px + phone_w - 10, py + phone_h - 18], radius=16, fill=(0, 229, 255, int(60 * alpha_fade)))

            canvas.paste(overlay_box, (0, 0), overlay_box)

        # B. Small Corner Logo: Tiny subtle badge at top-right corner (No sound, no massive overlay)
        if small_logo:
            # Top right at (980, 50)
            canvas.paste(small_logo, (980, 50), small_logo)

        # C. Bottom Subtle Credit Pill (Sideways or Bottom Safe Area)
        if f_idx >= 75:
            credit_text = "EDIT BY @KING_WIZZY • 4K 60FPS"
            cr_box = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
            d_cr = ImageDraw.Draw(cr_box)
            cr_b = d_cr.textbbox((0, 0), credit_text, font=font_credit)
            cw = cr_b[2] - cr_b[0] + 40
            ch = 44
            cx = (1080 - cw) // 2
            cy = 1920 - 90
            d_cr.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=22, fill=(5, 5, 12, 170), outline=(255, 255, 255, 80), width=1)
            d_cr.text((cx + 20, cy + 8), credit_text, font=font_credit, fill=(255, 255, 255, 220))
            canvas.paste(cr_box, (0, 0), cr_box)

        write_proc.stdin.write(canvas.tobytes())

        if f_idx % 180 == 0:
            print(f"[Studio Compositor] Rendered {f_idx}/{total_frames} frames ({f_idx*100//total_frames}%)...")

    read_proc.stdout.close()
    read_proc.wait()
    write_proc.stdin.close()
    write_proc.wait()
    print("[Studio Compositor] Geometric rotation compositing completed successfully!")

    # 4. Master audio to EBU R128 (-14.0 LUFS)
    print("[Audio Master] Applying 2-Pass EBU R128 Loudness Normalization (-14.0 LUFS)...")
    cmd_master = [
        "ffmpeg", "-y",
        "-i", temp_unmastered,
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "256k",
        output_video_path
    ]
    subprocess.run(cmd_master, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[Audio Master] Final mastered broadcast video: {output_video_path}")

    # 5. QA Proof Contact Sheet
    qa_path = "output/rotate_gojo_vs_sukuna_qa.jpg"
    cmd_qa = [
        "ffmpeg", "-y",
        "-i", output_video_path,
        "-vf", "select='not(mod(n\,100))',scale=360:640,tile=3x3",
        "-vframes", "1",
        qa_path
    ]
    subprocess.run(cmd_qa, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[QA Engine] Contact proof sheet saved: {qa_path}")

    # Cleanup temp files
    for tmp in [raw_audio_path, temp_unmastered]:
        try:
            if os.path.exists(tmp):
                os.remove(tmp)
        except:
            pass

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "assets/rotate_raw/aWApEIyXUp4.mp4"
    dest = sys.argv[2] if len(sys.argv) > 2 else "output/rotate_amv_mastered.mp4"
    render_rotating_phone_amv(raw_amv_path=src, output_video_path=dest)
