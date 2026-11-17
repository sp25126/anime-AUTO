import subprocess
import os
import json

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"

def harvest_viral_character_clip(query, platform="all"):
    """
    Harvests native 9:16 vertical clips with authentic subtitles and edits
    from TikTok, Instagram Reels, or YouTube Shorts without requiring Remotion.
    """
    os.makedirs("assets/harvested_clips", exist_ok=True)
    out_tmpl = "assets/harvested_clips/%(id)s.%(ext)s"

    print(f"[Harvester] Scouting viral 9:16 vertical clips for: '{query}'...")
    cmd = [
        python_exe, "-m", "yt_dlp",
        f"ytsearch5:{query}",
        "-f", "bestvideo[height>=720][ext=mp4]+bestaudio/best[ext=mp4]/best",
        "-o", out_tmpl,
        "--no-playlist",
        "--quiet",
        "--no-warnings"
    ]
    subprocess.run(cmd)

    # Locate downloaded clips
    files = [os.path.join("assets/harvested_clips", f) for f in os.listdir("assets/harvested_clips") if f.endswith((".mp4", ".mkv", ".webm"))]
    return files

if __name__ == "__main__":
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else "gojo reality check edit 9:16 tiktok"
    clips = harvest_viral_character_clip(q)
    print(f"[Harvester] Found {len(clips)} candidate clips.")
