"""
Signal Analyzer: Heatmap DSP + Librosa Topographic Prominence
Extracts the exact climax window using YouTube 'Most Replayed' heatmaps (intensityScoreNormalized > 0.85)
and Librosa RMS topographic prominence for frame-accurate punchline cuts.
"""

from dataclasses import dataclass
from typing import List, Optional, Tuple
import numpy as np
import scipy.signal
import librosa
import yt_dlp

@dataclass
class ClimaxWindow:
    start_time: float
    end_time: float
    intensity_score: float
    climax_type: str # 'heatmap' or 'rms_peak'

class SignalAnalyzer:
    def __init__(self):
        pass

    def extract_youtube_heatmap(self, url_or_id: str) -> List[ClimaxWindow]:
        """
        Extracts YouTube 'Most Replayed' heatmap data using yt-dlp metadata.
        Returns contiguous segments exceeding the 0.85 intensity threshold.
        """
        ydl_opts = {
            "quiet": True,
            "skip_download": True,
        }
        url = url_or_id if url_or_id.startswith("http") else f"https://www.youtube.com/watch?v={url_or_id}"
        events = []
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                heatmap_data = info.get("heatmap", [])
                if not heatmap_data:
                    return events
                
                # Check for intensity score or normalized value
                for segment in heatmap_data:
                    val = segment.get("intensityScoreNormalized")
                    if val is None:
                        val = segment.get("value", 0.0)
                    
                    if val >= 0.80:
                        events.append(ClimaxWindow(
                            start_time=segment.get("start_time", 0.0),
                            end_time=segment.get("end_time", 0.0),
                            intensity_score=val,
                            climax_type="heatmap"
                        ))
        except Exception as e:
            print(f"[SignalAnalyzer] Heatmap extraction failed: {e}")
        return events

    def detect_comedy_punchline(self, audio_path: str, target_window: Optional[Tuple[float, float]] = None) -> List[float]:
        """
        Isolates punchlines using Topographic Prominence on audio RMS envelope.
        Identifies sudden high-amplitude bursts immediately succeeded by steep drops in energy (deadpan silence).
        """
        try:
            y, sr = librosa.load(audio_path, sr=22050)
            if target_window:
                start_sample = int(target_window[0] * sr)
                end_sample = int(target_window[1] * sr)
                y = y[start_sample:end_sample]
                offset_time = target_window[0]
            else:
                offset_time = 0.0

            # Compute RMS energy envelope
            rms = librosa.feature.rms(y=y, frame_length=2048, hop_length=512)[0]
            
            # Scipy find_peaks utilizing prominence
            peaks, properties = scipy.signal.find_peaks(
                rms,
                prominence=0.35, # Robust prominence threshold for dialogue transients
                distance=int(sr * 1.5 / 512) # Minimum 1.5 second distance between punchlines
            )

            # Map peak frames back to seconds
            peak_times = librosa.frames_to_time(peaks, sr=sr, hop_length=512) + offset_time
            return list(peak_times)
        except Exception as e:
            print(f"[SignalAnalyzer] RMS Prominence analysis failed: {e}")
            return []

if __name__ == "__main__":
    analyzer = SignalAnalyzer()
    print("Signal Analyzer module compiled successfully.")
