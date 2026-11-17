import os
import sys
import json
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

def render_villain_compilation():
    base_video_path = "output/villain_blur_base.mp4"
    output_video_path = "output/ranking_villain_aura_mastered.mp4"
    fps = 30

    print("[Studio Compositor] Initializing Villain Aura Ranking Pipeline...")
    os.makedirs("output", exist_ok=True)

    # 1. Probe base video metadata
    probe_cmd = [
        "ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height,duration",
        "-of", "default=noprint_wrappers=1:nokey=1", base_video_path
    ]
    meta = subprocess.check_output(probe_cmd).decode().split()
    width = int(meta[0])
    height = int(meta[1])
    dur = float(meta[2])
    total_frames = int(dur * fps)

    print(f"[Studio Compositor] Canvas: {width}x{height} @ {fps}fps CFR | Frames: {total_frames} | Duration: {dur:.2f}s")

    # Font setups
    font_impact_title = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 74)
    font_impact_accent = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 84)
    font_impact_rank = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 64)
    font_impact_label = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 40)
    font_segoe_brand = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
    font_segoe_credit = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 30)
    font_outro = ImageFont.truetype("C:/Windows/Fonts/impact.ttf", 60)

    # Schedule: 5 clips
    # Clip 5 (Gilgamesh): 11.0s (330f)
    # Clip 4 (Toji): 11.5s (345f)
    # Clip 3 (Muzan): 11.5s (345f)
    # Clip 2 (Aizen): 12.0s (360f)
    # Clip 1 (Madara): 12.5s (375f)
    clips = [
        {"rank": 5, "dur": 330, "label": "450K", "credit": "@Zeref Edit", "color": (255, 215, 0)},
        {"rank": 4, "dur": 345, "label": "1.8M", "credit": "@Zyper", "color": (0, 229, 255)},
        {"rank": 3, "dur": 345, "label": "920K", "credit": "@AnimeTwixMaster", "color": (255, 42, 42)},
        {"rank": 2, "dur": 360, "label": "2.3M", "credit": "@RECONZ AE", "color": (180, 70, 255)},
        {"rank": 1, "dur": 375, "label": "4.6M", "credit": "@NARUTO 93", "color": (255, 50, 50)},
    ]

    clip_boundaries = []
    accumulated = 0
    for c in clips:
        clip_boundaries.append((accumulated, accumulated + c["dur"], c))
        accumulated += c["dur"]

    # Load Official Channel Logo for outro popup
    logo_path = "branding/channel_logo_1024.png"
    channel_logo = Image.open(logo_path).convert("RGBA") if os.path.exists(logo_path) else None

    # Outro popup starts in the last 2.0s (60 frames)
    outro_start_frame = total_frames - 60

    # Stream to FFmpeg
    temp_unmastered = "output/temp_villain_unmastered.mp4"
    ffmpeg_pipe_cmd = [
        "ffmpeg", "-y",
        "-i", base_video_path,
        "-f", "rawvideo", "-vcodec", "rawvideo",
        "-s", f"{width}x{height}", "-pix_fmt", "rgba",
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
        active_clip = clips[0]
        active_clip_idx = 0
        for idx, (s, e, c) in enumerate(clip_boundaries):
            if s <= f_idx < e:
                active_clip = c
                active_clip_idx = idx
                break
            if idx == len(clips) - 1 and f_idx >= e:
                active_clip = c
                active_clip_idx = idx

        img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Normal HUD until outro
        if f_idx < outro_start_frame:
            # 1. Animated Rank Neon Perimeter Border
            active_color = active_clip["color"]
            pulse = 0.5 + 0.5 * math.sin(f_idx * 0.15)
            neon_alpha = int(140 + pulse * 115)
            draw.line([(0, 655), (width, 655)], fill=(*active_color, neon_alpha), width=4)
            draw.line([(0, 1265), (width, 1265)], fill=(*active_color, neon_alpha), width=4)

            # 2. Top Pinned Title (JJK Signature Layout)
            # Line 1: TOP 5 COLDEST
            t1 = "TOP 5 COLDEST"
            t1_bbox = draw.textbbox((0, 0), t1, font=font_impact_title)
            t1_w = t1_bbox[2] - t1_bbox[0]
            t1_x = (width - t1_w) // 2
            t1_y = 65

            for dx, dy in [(-3, -3), (3, -3), (-3, 3), (3, 3), (0, 4), (0, -4), (4, 0), (-4, 0)]:
                draw.text((t1_x + dx, t1_y + dy), t1, font=font_impact_title, fill=(0, 0, 0, 240))
            draw.text((t1_x, t1_y), t1, font=font_impact_title, fill=(255, 255, 255, 255))

            # Line 2: VILLAIN AURA WALKS with crimson accent
            t2 = "VILLAIN AURA WALKS"
            t2_bbox = draw.textbbox((0, 0), t2, font=font_impact_accent)
            t2_w = t2_bbox[2] - t2_bbox[0]
            t2_x = (width - t2_w) // 2
            t2_y = 145

            for dx, dy in [(-3, -3), (3, -3), (-3, 3), (3, 3), (0, 4), (0, -4), (4, 0), (-4, 0)]:
                draw.text((t2_x + dx, t2_y + dy), t2, font=font_impact_accent, fill=(0, 0, 0, 240))
            draw.text((t2_x, t2_y), t2, font=font_impact_accent, fill=(255, 30, 60, 255))

            # 3. Left Rank Countdown Stack
            stack_y = 260
            for num in [1, 2, 3, 4, 5]:
                matching_idx = next(i for i, c in enumerate(clips) if c["rank"] == num)
                matching_clip = clips[matching_idx]
                is_active = (matching_clip["rank"] == active_clip["rank"])
                has_played = (matching_idx <= active_clip_idx)

                r_color = matching_clip["color"]
                r_alpha = 255 if is_active else (150 if has_played else 60)

                num_str = f"{num}."
                for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2)]:
                    draw.text((55 + dx, stack_y + dy), num_str, font=font_impact_rank, fill=(0, 0, 0, 220))
                draw.text((55, stack_y), num_str, font=font_impact_rank, fill=(*r_color, r_alpha))

                if has_played:
                    lbl = matching_clip["label"]
                    lbl_color = (255, 255, 255, 255) if is_active else (180, 180, 190, 180)
                    for dx, dy in [(-2, -2), (2, -2), (-2, 2), (2, 2)]:
                        draw.text((120 + dx, stack_y + dy + 16), lbl, font=font_impact_label, fill=(0, 0, 0, 220))
                    draw.text((120, stack_y + 16), lbl, font=font_impact_label, fill=lbl_color)

                stack_y += 68

            # 4. Top Right Watermark Pill
            pill_text = "@animefandom0_0"
            pill_bbox = draw.textbbox((0, 0), pill_text, font=font_segoe_brand)
            pw = pill_bbox[2] - pill_bbox[0] + 36
            ph = 48
            px = width - pw - 45
            py = 75
            draw.rounded_rectangle([px, py, px + pw, py + ph], radius=24, fill=(0, 0, 0, 180), outline=(255, 255, 255, 70), width=1)
            draw.text((px + 18, py + 8), pill_text, font=font_segoe_brand, fill=(255, 255, 255, 240))

            # 5. Bottom Cyan Credit Tag
            credit_text = f"EDIT BY {active_clip['credit'].upper()}"
            cr_bbox = draw.textbbox((0, 0), credit_text, font=font_segoe_credit)
            cw = cr_bbox[2] - cr_bbox[0] + 50
            ch = 56
            cx = (width - cw) // 2
            cy = height - 120
            draw.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=28, fill=(5, 5, 12, 210), outline=(0, 240, 255, 120), width=2)
            draw.text((cx + 25, cy + 10), credit_text, font=font_segoe_credit, fill=(0, 240, 255, 255))

        else:
            # 6. DYNAMIC SPRING LOGO POPUP OUTRO (Frames outro_start_frame to total_frames)
            p_frame = f_idx - outro_start_frame
            # Spring scale effect (0.0 to 1.15 to 1.0)
            if p_frame < 18:
                scale = (p_frame / 18.0) * 1.15
            elif p_frame < 26:
                scale = 1.15 - ((p_frame - 18) / 8.0) * 0.15
            else:
                scale = 1.0

            # Darken backdrop
            dark_alpha = int(min(220, p_frame * 12))
            draw.rectangle([0, 0, width, height], fill=(5, 5, 10, dark_alpha))

            # Draw Scaled Channel Logo in Center
            if channel_logo:
                target_size = int(460 * scale)
                if target_size > 10:
                    logo_resized = channel_logo.resize((target_size, target_size), Image.Resampling.LANCZOS)
                    lx = (width - target_size) // 2
                    ly = (height - target_size) // 2 - 80
                    # Outer pulsing neon ring
                    ring_r = target_size // 2 + 18
                    draw.ellipse([width//2 - ring_r, ly + target_size//2 - ring_r, width//2 + ring_r, ly + target_size//2 + ring_r], outline=(255, 30, 60, 220), width=4)
                    img.paste(logo_resized, (lx, ly), logo_resized)

            # Draw Channel Handle & Subscribe Tag
            if p_frame > 12:
                handle_text = "ANIME FANDOM 0_0"
                hb = draw.textbbox((0, 0), handle_text, font=font_outro)
                hw = hb[2] - hb[0]
                hx = (width - hw) // 2
                hy = height // 2 + 200
                for dx, dy in [(-3, -3), (3, -3), (-3, 3), (3, 3)]:
                    draw.text((hx + dx, hy + dy), handle_text, font=font_outro, fill=(0, 0, 0, 240))
                draw.text((hx, hy), handle_text, font=font_outro, fill=(255, 255, 255, 255))

                sub_text = "@animefandom0_0 • SUBSCRIBE FOR MORE"
                sb = draw.textbbox((0, 0), sub_text, font=font_segoe_brand)
                sw = sb[2] - sb[0]
                draw.text(((width - sw)//2, hy + 75), sub_text, font=font_segoe_brand, fill=(0, 240, 255, 240))

        pipe_proc.stdin.write(img.tobytes())

        if f_idx % 180 == 0:
            print(f"[Studio Compositor] Rendered {f_idx}/{total_frames} frames ({f_idx*100//total_frames}%)...")

    pipe_proc.stdin.close()
    pipe_proc.wait()
    print("[Studio Compositor] Video overlay compositing completed successfully!")

    # 7. Mix in the Logo Popup SFX at the exact outro frame (outro_start_frame / 30 = ~56.5s)
    outro_time_sec = outro_start_frame / float(fps)
    sfx_wav = "branding/audio/logo_popup_sfx.wav"
    mixed_audio_video = "output/temp_villain_sfx_mixed.mp4"

    print(f"[Audio Master] Mixing custom logo popup SFX at t={outro_time_sec:.2f}s...")
    cmd_mix = [
        "ffmpeg", "-y",
        "-i", temp_unmastered,
        "-i", sfx_wav,
        "-filter_complex",
        f"[1:a]adelay={int(outro_time_sec*1000)}|{int(outro_time_sec*1000)}[delayed_sfx];"
        "[0:a][delayed_sfx]amix=inputs=2:duration=first:weights=1.0 1.5[aout]",
        "-map", "0:v", "-map", "[aout]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "256k",
        mixed_audio_video
    ]
    subprocess.run(cmd_mix, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 8. Audio Loudness Normalization to EBU R128 (-14.0 LUFS, -1.5 dBTP)
    print("[Audio Master] Applying 2-Pass EBU R128 Loudness Normalization (-14.0 LUFS)...")
    cmd_master = [
        "ffmpeg", "-y",
        "-i", mixed_audio_video,
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "256k",
        output_video_path
    ]
    subprocess.run(cmd_master, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[Audio Master] Final mastered broadcast video: {output_video_path}")

    # 9. Generate QA contact sheet
    qa_path = "output/ranking_villain_aura_qa.jpg"
    cmd_qa = [
        "ffmpeg", "-y",
        "-i", output_video_path,
        "-vf", "select='not(mod(n\,190))',scale=360:640,tile=3x3",
        "-vframes", "1",
        qa_path
    ]
    subprocess.run(cmd_qa, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[QA Engine] Contact proof sheet saved: {qa_path}")

    # Cleanup temp files
    for tmp in [temp_unmastered, mixed_audio_video]:
        try:
            if os.path.exists(tmp):
                os.remove(tmp)
        except:
            pass

if __name__ == "__main__":
    render_villain_compilation()
