"""
Autonomous Stream Harvester
Implements Section 2 of the Comprehensive Architectural Blueprint:
- JA4 TLS Fingerprint bypass using curl_cffi Chrome131 impersonation
- Obfuscated iframe decryption via yt-dlp module
- Remote HLS stream slicing using FFmpeg (-avoid_negative_ts make_zero)
"""

import subprocess
import os
import sys
from curl_cffi import requests as cffi_requests

class StreamHarvester:
    def __init__(self, user_agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"):
        self.user_agent = user_agent
        # Impersonate Chrome JA4 TLS fingerprint to bypass Cloudflare WAF natively
        self.session = cffi_requests.Session(impersonate="chrome131")

    def resolve_m3u8_playlist(self, target_iframe_url: str) -> str:
        """
        Uses yt-dlp to extract the raw .m3u8 URL from an obfuscated iframe, 
        handling AES-128 decryption and token exchange inherently.
        """
        command = [
            sys.executable, "-m", "yt_dlp",
            "--get-url",
            "--force-ipv4",
            "--add-header", f"User-Agent:{self.user_agent}",
            "--add-header", f"Referer:{target_iframe_url}",
            target_iframe_url
        ]
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"yt-dlp extraction failed: {e.stderr}")

    def extract_lossless_clip(self, m3u8_url: str, start_time: str, end_time: str, output_path: str, referer: str = ""):
        """
        Performs a remote stream seek to pull a specific 15-second clip losslessly.
        Uses avoid_negative_ts to reset presentation timestamps (PTS) to zero.
        """
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        headers_arg = f"User-Agent: {self.user_agent}"
        if referer:
            headers_arg = f"Referer: {referer}\r\n" + headers_arg

        ffmpeg_cmd = [
            "ffmpeg",
            "-hide_banner",
            "-headers", headers_arg,
            "-ss", str(start_time),      # Fast input seek pre-decode
            "-to", str(end_time),
            "-i", m3u8_url,              # Remote HLS master playlist
            "-c", "copy",                # Lossless stream remux
            "-avoid_negative_ts", "make_zero", # Shift timestamps to non-negative
            "-map", "0:v:0",             # Map highest quality video stream
            "-map", "0:a:0",             # Map corresponding audio stream
            "-y",                        # Overwrite existing output
            output_path
        ]
        
        try:
            subprocess.run(ffmpeg_cmd, check=True, stderr=subprocess.PIPE)
            print(f"[SUCCESS] Extracted and synchronized clip to {output_path}")
            return output_path
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] FFmpeg stream extraction failed: {e.stderr.decode('utf-8')}")
            return None

    def fast_harvest_direct(self, search_query: str, start_time: float, duration: float, output_path: str):
        """
        Direct micro-clipper utilizing yt-dlp native download sections to harvest exact 1080p clip.
        Handles container extensions (.webm, .mkv, .mp4) and converts cleanly to .mp4 if needed.
        """
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        end_time = start_time + duration
        
        # Remove any stale output or intermediate files
        base_no_ext = os.path.splitext(output_path)[0]
        for candidate_ext in [".mp4", ".webm", ".mkv", ".mp4.webm", ".mp4.mkv"]:
            p = base_no_ext + candidate_ext
            if os.path.exists(p):
                try:
                    os.remove(p)
                except Exception:
                    pass
        if os.path.exists(output_path):
            try:
                os.remove(output_path)
            except Exception:
                pass

        cmd = [
            sys.executable, "-m", "yt_dlp",
            f"ytsearch1:{search_query}",
            "--download-sections", f"*{start_time}-{end_time}",
            "-f", "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
            "-o", output_path,
            "--force-keyframes-at-cuts",
            "--no-warnings"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        
        # Check if output exists directly
        if os.path.exists(output_path) and os.path.getsize(output_path) > 100000:
            print(f"[SUCCESS] Harvested direct clip: {output_path}")
            return output_path
            
        # Check if yt-dlp appended an extension like .webm or .mkv
        parent = os.path.dirname(output_path)
        base_name = os.path.basename(output_path)
        for fname in os.listdir(parent):
            if fname.startswith(base_name) and fname != base_name:
                alt_path = os.path.join(parent, fname)
                if os.path.getsize(alt_path) > 100000:
                    print(f"[Transcode] Remuxing {alt_path} to {output_path}...")
                    remux_cmd = [
                        "ffmpeg", "-y", "-i", alt_path,
                        "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                        "-c:a", "aac", "-b:a", "192k",
                        output_path
                    ]
                    subprocess.run(remux_cmd, capture_output=True)
                    if os.path.exists(output_path) and os.path.getsize(output_path) > 100000:
                        try:
                            os.remove(alt_path)
                        except Exception:
                            pass
                        print(f"[SUCCESS] Harvested & Transcoded direct clip: {output_path}")
                        return output_path

        print(f"[ERROR] Direct harvest failed for query: '{search_query}'")
        return None

if __name__ == "__main__":
    harvester = StreamHarvester()
    print("StreamHarvester initialized.")
