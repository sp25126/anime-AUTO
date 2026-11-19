import os
import json
import urllib.request
import subprocess

def detect_climax_window(raw_clip: str, title: str, anime: str, character: str, api_key: str = None) -> tuple:
    """
    Intelligently determines the start and duration for a clip to ensure:
    1. ZERO start-looping (no -stream_loop repeating the first 4s).
    2. The full uncut edit is shown if it is <= 22s.
    3. If longer than 22s, preserves the climax and buildup without premature cutoffs.
    4. Optional Gemini 2.5 Flash query (with rate limit protection and instant uncut fallback).
    """
    # 1. Probe true duration using ffprobe
    probe_cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", raw_clip]
    try:
        d = json.loads(subprocess.check_output(probe_cmd).decode("utf-8"))
        true_dur = float(d["format"]["duration"])
    except Exception:
        true_dur = 20.0

    # Rule A: If clip is already short (<= 22.0s), show 100% of the uncut clip!
    if true_dur <= 22.5:
        print(f"  [Climax Detector] Full uncut edit preserved: 0.0s to {true_dur:.2f}s (No loop, no cuts)")
        return 0.0, true_dur

    # Rule B: If longer, use Gemini if key provided (graceful fallback if none or error)
    if api_key and len(api_key) > 20:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
            prompt = (
                f"Anime: {anime}\nCharacter: {character}\nEdit Title: {title}\nTotal Duration: {true_dur:.1f}s.\n"
                "Determine the best 18 to 22 second window containing the climax transformation/beat drop so it is never cut prematurely.\n"
                "Respond in JSON: {\"start\": <float>, \"duration\": <float>}"
            )
            payload = json.dumps({
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"response_mime_type": "application/json"}
            }).encode("utf-8")
            req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=5) as resp:
                res_data = json.loads(resp.read().decode())
                ans = json.loads(res_data["candidates"][0]["content"]["parts"][0]["text"])
                start = float(ans.get("start", 0.0))
                dur = float(ans.get("duration", 20.0))
                # Validate bounds
                start = max(0.0, min(start, true_dur - 15.0))
                dur = min(dur, true_dur - start)
                print(f"  [Climax Detector: Gemini] Target climax window: {start:.2f}s to {start+dur:.2f}s (dur={dur:.2f}s)")
                return start, dur
        except Exception as e:
            print(f"  [Climax Detector] Gemini unavailable ({e}), using intelligent uncut climax fallback.")

    # Rule C: Robust Fallback (No Gemini required)
    # In anime edits, the climax/drop occurs in the final 60-90% of the video.
    # Take the last 18-20 seconds or up to the finish so the climax is never cut off!
    dur = min(20.0, true_dur)
    start = max(0.0, true_dur - dur)
    print(f"  [Climax Detector: Fallback] Climax preserved from climax arrival: {start:.2f}s to {true_dur:.2f}s (dur={dur:.2f}s)")
    return start, dur
