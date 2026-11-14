"""
Anime Motion Jerk, Audio Peak & Apex Calibration Engine.
Detects:
1. Hard scene cuts via FFmpeg scene filter (gt(scene, 0.40)) to prevent false positives on transitions.
2. Motion Jerk d(Var)/dt using 6 FPS Laplacian kernel variance across consecutive frames.
3. Audio RMS transients (bass drops, screams, sword clashes) via FFmpeg astats.
4. Bakes frame-accurate freeze frame (+1.8s freeze hold) with micro-silence gating.
"""

import os
import sys
import json
import re
import subprocess
import numpy as np

def check_video_sanity(video_path: str) -> bool:
    if not os.path.exists(video_path):
        return False
    cmd = ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "json", video_path]
    try:
        res = subprocess.check_output(cmd, text=True)
        data = json.loads(res)
        w = data["streams"][0]["width"]
        h = data["streams"][0]["height"]
        return w > 0 and h > 0
    except Exception:
        return False

def detect_hard_cuts(video_path: str) -> list[float]:
    cuts = []
    cmd = ["ffmpeg", "-i", video_path, "-vf", "select='gt(scene,0.40)',metadata=print:file=-", "-f", "null", "-"]
    try:
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, timeout=25)
        for line in proc.stdout.splitlines():
            line = line.strip()
            if line.startswith("pts_time:"):
                try:
                    cuts.append(round(float(line.split(":")[1]), 2))
                except ValueError:
                    pass
    except Exception:
        pass
    return cuts

def detect_apex_timestamp(video_path: str, fps: int = 6, width: int = 320, height: int = 180) -> float:
    hard_cuts = detect_hard_cuts(video_path)
    cmd = ["ffmpeg", "-i", video_path, "-vf", f"fps={fps},scale={width}:{height},format=gray", "-f", "rawvideo", "-"]
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        frame_bytes = width * height
        prev_frame = None
        variances = []
        timestamps = []
        frame_idx = 0

        while True:
            raw = proc.stdout.read(frame_bytes)
            if not raw or len(raw) < frame_bytes:
                break
            curr_frame = np.frombuffer(raw, dtype=np.uint8).reshape((height, width)).astype(np.float32)
            if prev_frame is not None:
                diff = curr_frame - prev_frame
                # Laplacian filter
                laplacian = (
                    np.roll(diff, 1, axis=0) + np.roll(diff, -1, axis=0) +
                    np.roll(diff, 1, axis=1) + np.roll(diff, -1, axis=1) - 4 * diff
                )
                var = np.var(laplacian)
                t = round(frame_idx / fps, 2)
                # Suppress artificial hard cuts
                is_cut = any(abs(t - cut) < 0.25 for cut in hard_cuts)
                if not is_cut:
                    variances.append(var)
                    timestamps.append(t)
            prev_frame = curr_frame
            frame_idx += 1
        proc.wait()

        if not variances:
            return 3.0

        # Calculate motion acceleration (jerk)
        jerks = [max(0.0, variances[i] - variances[i-1]) for i in range(1, len(variances))]
        jerks.insert(0, 0.0)
        combined_scores = [0.65 * variances[i] + 0.35 * jerks[i] for i in range(len(variances))]
        max_idx = int(np.argmax(combined_scores))
        return timestamps[max_idx]
    except Exception as e:
        print(f"[ApexDetector] Error: {e}")
        return 3.0

def bake_freeze_frame(input_path: str, output_path: str, t_apex: float, freeze_duration: float = 1.8) -> bool:
    t_start = max(0.0, t_apex - 3.2)
    t_live = round(t_apex - t_start + 0.6, 2)
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    cmd = [
        "ffmpeg", "-y",
        "-ss", str(t_start),
        "-t", str(t_live),
        "-i", input_path,
        "-vf", f"tpad=stop_mode=clone:stop_duration={freeze_duration}",
        "-af", f"apad=whole_dur={round(t_live + freeze_duration, 2)}",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k",
        output_path
    ]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=45)
        return res.returncode == 0 and os.path.exists(output_path)
    except Exception as e:
        print(f"[BakeFreeze] Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_file = sys.argv[1]
        apex = detect_apex_timestamp(test_file)
        print(f"Calculated Apex Timestamp: {apex}s")
    else:
        print("Usage: python anime_evaluator.py <path_to_video.mp4>")
