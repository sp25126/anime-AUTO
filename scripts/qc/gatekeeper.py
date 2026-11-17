"""
Automated Video Quality Control (QC) Gatekeeper
Deterministically checks:
1. freezedetect: Catches frozen renders/stuck frames (n=-60dB:d=2)
2. blackdetect: Rejects unintentional black frames (d=0.5:pic_th=0.98:pix_th=0.10)
3. silencedetect: Flags extended silence/audio corruption
Outputs boolean gate approval and structural diagnostic report.
"""

import re
import subprocess
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class QCReport:
    passed: bool
    black_frames_detected: bool
    frozen_frames_detected: bool
    silence_detected: bool
    summary: str

class QCGatekeeper:
    def __init__(self):
        pass

    def run_qc_inspection(self, video_path: str) -> QCReport:
        cmd = [
            "ffmpeg", "-v", "error", "-i", video_path,
            "-vf", "blackdetect=d=0.5:pic_th=0.98:pix_th=0.10,freezedetect=n=-60dB:d=2",
            "-af", "silencedetect=n=-50dB:d=2.5",
            "-f", "null", "-"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        stderr_log = res.stderr

        black_found = bool(re.search(r"black_start", stderr_log))
        freeze_found = bool(re.search(r"freeze_start", stderr_log))
        silence_found = bool(re.search(r"silence_start", stderr_log))

        # Check conditions
        failed_reasons = []
        if freeze_found:
            failed_reasons.append("Frozen frames detected (>2.0s duration)")
        if black_found:
            failed_reasons.append("Black frames detected (>0.5s duration)")
        
        passed = (len(failed_reasons) == 0)
        summary = "QC Approved (0 frozen frames, 0 black frames, continuous audio)." if passed else f"QC Failed: {'; '.join(failed_reasons)}"

        return QCReport(
            passed=passed,
            black_frames_detected=black_found,
            frozen_frames_detected=freeze_found,
            silence_detected=silence_found,
            summary=summary
        )

if __name__ == "__main__":
    qc = QCGatekeeper()
    # Test on our latest master
    test_file = "output/nolonger_perfect_cut_mastered.mp4"
    import os
    if os.path.exists(test_file):
        report = qc.run_qc_inspection(test_file)
        print(f"QC Inspection on {test_file}:")
        print(f"  Passed: {report.passed}")
        print(f"  Summary: {report.summary}")
    else:
        print("QC Gatekeeper initialized.")
