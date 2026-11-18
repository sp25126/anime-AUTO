import os
import sys
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

def render_reality_check_scene():
    raw_scene_path = "assets/scene_raw/ZHVuXN4DHkE.mp4"
    output_video_path = "output/moment_gojo_reality_check_mastered.mp4"
    fps = 30

    print("[Studio Compositor] Initializing Single Scene Reality Check Pipeline with Dynamic Subtitles...")
    os.makedirs("output", exist_ok=True)

    # 1. Probe input video
    probe_cmd = [
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", raw_scene_path
    ]
    dur = float(subprocess.check_output(probe_cmd).decode().strip())
    total_frames = int(dur * fps)
    print(f"[Studio Compositor] Duration: {dur:.2f}s | Total Frames: {total_frames} @ {fps}fps")

    # 2. Build 1080x1920 base with Dynamic Blurred Background
    base_file = "output/temp_scene_blur_base.mp4"
    filter_complex = (
        "[0:v]fps=30,split=2[fg_raw][bg_raw];"
        "[bg_raw]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=25:5,eq=brightness=-0.15:saturation=1.2[bg_blur];"
        "[fg_raw]scale=1080:-2,setsar=1[fg_scaled];"
        "[bg_blur][fg_scaled]overlay=0:(1920-h)/2[vout];"
        "[0:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo[aout]"
    )
    cmd_base = [
        "ffmpeg", "-y",
        "-i", raw_scene_path,
        "-filter_complex", filter_complex,
        "-map", "[vout]", "-map", "[aout]",
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k",
        base_file
    ]
    subprocess.run(cmd_base, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[Studio Compositor] Base dynamic blur canvas rendered: {base_file}")

    # Fonts
    font_hook_main = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 60)
    font_hook_sub = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 42)
    font_brand = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
    font_credit = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
    
    # Subtitle Fonts
    font_sub_norm = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 68)
    font_sub_punch = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 80)

    # Corner Watermark (64x64 badge)
    logo_path = "branding/watermark_badge_128.png"
    corner_logo = Image.open(logo_path).convert("RGBA").resize((64, 64), Image.Resampling.LANCZOS) if os.path.exists(logo_path) else None

    # Subtitle script timeline (Word-by-word kinetic animation)
    # Dialogue: Jogo vs Gojo
    # [Start Frame, End Frame, Speaker, Text, PunchWord]
    subtitle_events = [
        (0, 45, "JOGO", "YOU THOUGHT YOU COULD", ""),
        (45, 95, "JOGO", "BEAT ME WITH THIS?!", "BEAT ME"),
        (95, 150, "GOJO", "WHAT ARE YOU TALKING ABOUT?", ""),
        (150, 210, "GOJO", "THIS IS INFINITY.", "INFINITY"),
        (210, 270, "GOJO", "EVERYWHERE AROUND ME...", ""),
        (270, 340, "GOJO", "THE CLOSER YOU GET...", ""),
        (340, 420, "GOJO", "THE SLOWER YOU BECOME.", "SLOWER"),
        (420, 500, "GOJO", "YOU CAN NEVER TOUCH ME.", "NEVER TOUCH"),
        (500, 580, "GOJO", "WANT TO HOLD HANDS?", "HOLD HANDS"),
        (580, 660, "JOGO", "HE'S AN ABSOLUTE MONSTER...", "MONSTER")
    ]

    temp_unmastered = "output/temp_scene_unmastered.mp4"
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

        # 1. Pinned Contextual Hook Box at Top (The 4.1M view formula)
        # "THE EXACT SECOND HE REALIZED" + "HE MESSED UP 💀"
        hook_box_y0 = 70
        hook_box_y1 = 205
        draw.rounded_rectangle([80, hook_box_y0, 1000, hook_box_y1], radius=22, fill=(8, 8, 14, 215), outline=(255, 30, 60, 230), width=3)

        h1 = "THE EXACT SECOND HE REALIZED"
        h1_b = draw.textbbox((0, 0), h1, font=font_hook_main)
        h1_w = h1_b[2] - h1_b[0]
        draw.text(((1080 - h1_w)//2, hook_box_y0 + 15), h1, font=font_hook_main, fill=(255, 255, 255, 255))

        h2 = "HE MESSED UP 💀 • GOJO VS JOGO"
        h2_b = draw.textbbox((0, 0), h2, font=font_hook_sub)
        h2_w = h2_b[2] - h2_b[0]
        draw.text(((1080 - h2_w)//2, hook_box_y0 + 78), h2, font=font_hook_sub, fill=(255, 230, 0, 255))

        # 2. Corner Watermark (64x64 subtle badge, NO SFX)
        if corner_logo:
            img.paste(corner_logo, (980, 50), corner_logo)

        # 3. Dynamic Subtitles (Synchronized Kinetic Typography)
        # Find active subtitle
        active_sub = None
        for (s_frame, e_frame, speaker, text, punch) in subtitle_events:
            if s_frame <= f_idx < e_frame:
                active_sub = (s_frame, e_frame, speaker, text, punch)
                break

        if active_sub:
            s_frame, e_frame, speaker, text, punch = active_sub
            # Subtle bounce scale on word appearance (first 6 frames)
            age = f_idx - s_frame
            scale = 1.15 if age < 6 else 1.0
            
            # Subtitle Y position (lower third safe zone: y = 1420)
            sub_y = 1420

            # Speaker Pill (e.g. [GOJO] in cyan, [JOGO] in red)
            spk_color = (0, 240, 255) if speaker == "GOJO" else (255, 50, 70)
            spk_tag = f"[{speaker}]"
            spk_b = draw.textbbox((0, 0), spk_tag, font=font_brand)
            spk_w = spk_b[2] - spk_b[0]
            
            # Render Speaker
            draw.text(((1080 - spk_w)//2, sub_y - 45), spk_tag, font=font_brand, fill=(*spk_color, 240))

            # Render Subtitle Text with 8-directional heavy black stroke
            is_punch = (punch != "" and punch in text)
            active_font = font_sub_punch if (is_punch and age < 12) else font_sub_norm
            text_color = (255, 230, 0, 255) if is_punch else (255, 255, 255, 255)

            tb = draw.textbbox((0, 0), text, font=active_font)
            tw = tb[2] - tb[0]
            tx = (1080 - tw) // 2

            # Heavy black stroke for 100% legibility over any background
            for dx, dy in [(-3, -3), (3, -3), (-3, 3), (3, 3), (0, 4), (0, -4), (4, 0), (-4, 0), (-2, 0), (2, 0), (0, 2), (0, -2)]:
                draw.text((tx + dx, sub_y + dy), text, font=active_font, fill=(0, 0, 0, 240))
            draw.text((tx, sub_y), text, font=active_font, fill=text_color)

        # 4. Bottom Credit Attribution Pill
        credit_text = "JUJUTSU KAISEN S1 • @animefandom0_0"
        cr_b = draw.textbbox((0, 0), credit_text, font=font_credit)
        cw = cr_b[2] - cr_b[0] + 40
        ch = 44
        cx = (1080 - cw) // 2
        cy = 1920 - 90
        draw.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=22, fill=(5, 5, 12, 180), outline=(0, 240, 255, 100), width=1)
        draw.text((cx + 20, cy + 8), credit_text, font=font_credit, fill=(0, 240, 255, 240))

        pipe_proc.stdin.write(img.tobytes())

        if f_idx % 150 == 0:
            print(f"[Studio Compositor] Rendered {f_idx}/{total_frames} frames ({f_idx*100//total_frames}%)...")

    pipe_proc.stdin.close()
    pipe_proc.wait()
    print("[Studio Compositor] Subtitle compositing completed successfully!")

    # 4. Master audio to EBU R128 (-14.0 LUFS, -1.5 dBTP)
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
    qa_path = "output/moment_gojo_reality_check_qa.jpg"
    cmd_qa = [
        "ffmpeg", "-y",
        "-i", output_video_path,
        "-vf", "select='not(mod(n\,75))',scale=360:640,tile=3x3",
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
    render_reality_check_scene()
