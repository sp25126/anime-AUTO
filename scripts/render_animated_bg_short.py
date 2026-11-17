import subprocess
import os
import sys

def render_animated_bg_short(
    video_raw="input/dandadan_maid_cafe_raw.mp4",
    bg_image="assets/backgrounds/romcom_sunset.webp",
    header_card="assets/brand_header_card.png",
    bgm_path="assets/audio/trending_comedy_lofi_bed.mp3",
    outro_img="assets/dandadan_outro_card.png",
    output_master="output/dandadan_unlimited_master.mp4",
    duration=17.6
):
    os.makedirs("output", exist_ok=True)
    temp_main = "output/temp_unlimited_main.mp4"
    temp_outro = "output/temp_unlimited_outro.mp4"

    total_frames = int(duration * 30)

    # FAST & SMOOTH Filtergraph:
    # Notice: [1:v] has NO -loop 1 in input, zoompan reads 1 single frame and generates total_frames!
    # Zoom from 1.0 to 1.05 gently (subtle cinematic push-in)
    filtergraph = (
        f"[1:v]scale=1188:2112,zoompan=z='min(zoom+0.0002,1.05)':d={total_frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30[bg_anim];"
        f"[0:v]scale=1080:608,setsar=1,fps=30[fg_vid];"
        f"[bg_anim][2:v]overlay=0:456[bg_with_header];"
        f"[bg_with_header][fg_vid]overlay=0:656,format=yuv420p[v_main];"
        f"[0:a]asplit=2[voice_main][voice_sc];"
        f"[3:a]volume=0.28[bgm_base];"
        f"[bgm_base][voice_sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=500[ducked_bgm];"
        f"[ducked_bgm]asendcmd=c='10.8 volume volume 0'[muted_bgm];"
        f"[voice_main][muted_bgm]amix=inputs=2:duration=first:dropout_transition=0.2[a_mixed];"
        f"[a_mixed]loudnorm=I=-14:LRA=7:TP=-2.0,aresample=48000[a_main]"
    )

    print(f"Rendering main sequence ({duration}s) with animated background...")
    cmd_main = [
        "ffmpeg", "-y",
        "-ss", "0.0", "-t", str(duration), "-i", video_raw,
        "-i", bg_image,
        "-i", header_card,
        "-stream_loop", "-1", "-i", bgm_path,
        "-filter_complex", filtergraph,
        "-map", "[v_main]", "-map", "[a_main]",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        temp_main
    ]

    res_main = subprocess.run(cmd_main, capture_output=True, text=True)
    if res_main.returncode != 0:
        print("Main render error:", res_main.stderr[-400:])
        return False
    print("Main sequence rendered successfully.")

    # Render Outro Card at 30 fps
    print("Rendering 30fps outro sequence (2.4s)...")
    cmd_outro = [
        "ffmpeg", "-y",
        "-loop", "1", "-t", "2.4", "-i", outro_img,
        "-f", "lavfi", "-t", "2.4", "-i", "anullsrc=r=48000:cl=stereo",
        "-filter_complex", "[0:v]scale=1080:1920,setsar=1,fps=30,format=yuv420p[v_out]",
        "-map", "[v_out]", "-map", "1:a",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        temp_outro
    ]
    res_outro = subprocess.run(cmd_outro, capture_output=True, text=True)
    if res_outro.returncode != 0:
        print("Outro render error:", res_outro.stderr[-300:])
        return False
    print("Outro sequence rendered successfully.")

    # Concat with setsar=1 & aresample=48000
    print("Executing final seamless concat...")
    cmd_concat = [
        "ffmpeg", "-y",
        "-i", temp_main,
        "-i", temp_outro,
        "-filter_complex", (
            "[0:v]setsar=1,fps=30,scale=1080:1920[v0];"
            "[1:v]setsar=1,fps=30,scale=1080:1920[v1];"
            "[0:a]aresample=48000[a0];"
            "[1:a]aresample=48000[a1];"
            "[v0][a0][v1][a1]concat=n=2:v=1:a=1[v_final][a_final]"
        ),
        "-map", "[v_final]", "-map", "[a_final]",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        output_master
    ]
    res_concat = subprocess.run(cmd_concat, capture_output=True, text=True)

    if os.path.exists(temp_main): os.remove(temp_main)
    if os.path.exists(temp_outro): os.remove(temp_outro)

    if res_concat.returncode == 0:
        print(f"Master with animated background successfully rendered: {output_master}")
        return True
    else:
        print("Concat error:", res_concat.stderr[-300:])
        return False

if __name__ == "__main__":
    bg = sys.argv[1] if len(sys.argv) > 1 else "assets/backgrounds/romcom_sunset.webp"
    out = sys.argv[2] if len(sys.argv) > 2 else "output/dandadan_unlimited_master.mp4"
    render_animated_bg_short(bg_image=bg, output_master=out)
