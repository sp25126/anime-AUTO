"""
Autonomous Forensic DSP Rendering Engine (Production Calibrated)
Uses exact single-image zoompan with total_frames duration limit,
avoiding infinite loop lockup and completing a 30s master in ~25-35s.
"""

import subprocess
import json
import re
import os
import sys

class ForensicDSPEngine:
    def __init__(self, use_gpu: bool = False):
        self.use_gpu = use_gpu

    def render_group_c_short(
        self,
        clip_path: str,
        bg_path: str,
        header_path: str,
        bgm_path: str,
        output_path: str,
        duration: float = 30.0,
        mute_timestamps: tuple = None
    ) -> str:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        total_frames = int(duration * 30)
        
        # Deadpan mute filter setup
        mute_cmd = ""
        if mute_timestamps:
            m_start, _ = mute_timestamps
            mute_cmd = f"asendcmd=c='{m_start} volume volume 0',"

        # Single-pass filtergraph with zoompan governed by d={total_frames}
        filtergraph = (
            f"[1:v]scale=1188:2112,zoompan=z='min(zoom+0.0001,1.05)':d={total_frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x1920:fps=30[bg_anim];"
            f"[0:v]scale=1080:608,setsar=1,fps=30[fg_vid];"
            f"[bg_anim][2:v]overlay=0:456[bg_with_header];"
            f"[bg_with_header][fg_vid]overlay=0:656,format=yuv420p[v_main];"
            f"[0:a]asplit=2[vox][ctrl];"
            f"[3:a]volume=0.28[bgm_base];"
            f"[bgm_base][ctrl]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=500[ducked_bgm];"
            f"[ducked_bgm]{mute_cmd}volume=1.0[final_bgm];"
            f"[vox][final_bgm]amix=inputs=2:duration=first:dropout_transition=0.2[a_mixed];"
            f"[a_mixed]loudnorm=I=-14.0:LRA=7.0:TP=-1.5,aresample=48000[a_main]"
        )

        cmd = [
            "ffmpeg", "-y",
            "-ss", "0.0", "-t", str(duration), "-i", clip_path,
            "-i", bg_path,
            "-i", header_path,
            "-stream_loop", "-1", "-i", bgm_path,
            "-filter_complex", filtergraph,
            "-map", "[v_main]", "-map", "[a_main]",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            "-avoid_negative_ts", "make_zero",
            output_path
        ]

        print(f"[DSP Engine] Rendering 30s Master via Fast Zoompan Engine...")
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"[DSP Engine] Render Success: {output_path}")
            return output_path
        else:
            print(f"[DSP Engine] Render Error: {res.stderr[:400]}")
            return None

if __name__ == "__main__":
    dsp = ForensicDSPEngine()
    print("ForensicDSPEngine ready.")
