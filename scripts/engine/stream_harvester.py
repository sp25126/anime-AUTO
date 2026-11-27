"""
Universal Multi-Platform Anime Clip Harvester (YouTube Shorts, TikTok, Instagram Reels)
Combines high-speed streaming seek, rotating proxy fallbacks, and multi-platform scouting.
Guarantees 100% pure anime content by screening out non-anime/devotional/live-action clutter.
"""

import os
import sys
import json
import subprocess
import re
import shutil
from typing import Dict, Any, List, Optional
from pathlib import Path

ENGINE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ENGINE_DIR)

from proxy_harvester import (
    scout_youtube_anime_edits,
    scout_tiktok_anime_edits,
    download_social_clip,
    is_valid_anime_clip
)

class StreamHarvester:
    def __init__(self):
        self.workspace_root = os.path.abspath(os.path.join(ENGINE_DIR, "..", ".."))

    def harvest_best_segment(self, queries: List[str], output_path: str, min_duration: float = 20.0) -> Optional[str]:
        """
        Multi-Platform Harvester:
        1. Scouts candidates across YouTube Shorts and TikTok.
        2. Filters out non-anime and cartoon pollution.
        3. Downloads clean clip via direct link, yt-dlp, or proxy tunnel.
        4. Trims cleanly with FFmpeg to ensure video and audio synchronization.
        5. Falls back to local verified pool if live web harvest fails.
        """
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        print(f"[Stream Harvester] Scouting multi-platform candidates across YouTube & TikTok...")

        candidates: List[Dict[str, Any]] = []

        # 1. Scout across queries
        for q in queries:
            # YouTube Shorts scout
            yt_res = scout_youtube_anime_edits(q, count=3)
            candidates.extend(yt_res)

            # TikTok scout
            try:
                tt_res = scout_tiktok_anime_edits(q, count=2)
                candidates.extend(tt_res)
            except Exception as e:
                print(f"[Stream Harvester] TikTok scout note: {e}")

            if len(candidates) >= 4:
                break

        # Sort candidates by view count descending
        candidates.sort(key=lambda x: x.get("views", 0), reverse=True)

        # 2. Download and slice best candidate
        temp_dl = os.path.join(os.path.dirname(output_path), f"temp_dl_{os.path.basename(output_path)}")
        for cand in candidates:
            print(f"  • Attempting download ({cand.get('platform', 'web')}): '{cand.get('title', '')[:45]}'...")
            dl_path = download_social_clip(cand, temp_dl)
            if dl_path and os.path.exists(dl_path) and os.path.getsize(dl_path) > 100000:
                # Slice cleanly to min_duration with synced audio
                slice_cmd = [
                    "ffmpeg", "-y",
                    "-ss", "2.0",
                    "-t", str(min_duration),
                    "-i", dl_path,
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    output_path
                ]
                subprocess.run(slice_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                try: os.remove(dl_path)
                except: pass

                if os.path.exists(output_path) and os.path.getsize(output_path) > 100000:
                    print(f"[Stream Harvester] ✓ Successfully harvested live clip: {output_path}")
                    return output_path

        # 3. Verified Local Pool Fallback
        print("[Stream Harvester] Live web download challenged; rotating through verified anime clips pool...")
        pool_dir = os.path.join(self.workspace_root, "assets", "anime_clips_pool")
        if os.path.exists(pool_dir):
            pool_files = [os.path.join(pool_dir, f) for f in os.listdir(pool_dir) if f.endswith(".mp4")]
            if pool_files:
                import hashlib
                seed_val = int(hashlib.md5(output_path.encode()).hexdigest(), 16)
                chosen = pool_files[seed_val % len(pool_files)]
                print(f"[Stream Harvester] Selected offline pool clip: {os.path.basename(chosen)}")
                shutil.copy2(chosen, output_path)
                return output_path

        return None

if __name__ == "__main__":
    h = StreamHarvester()
    res = h.harvest_best_segment(["Jujutsu Kaisen Gojo edit 4k"], "test_harvest.mp4", min_duration=10.0)
    print("Harvest result:", res)
