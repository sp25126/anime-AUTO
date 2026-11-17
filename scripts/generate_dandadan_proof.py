import cv2
import numpy as np
import os

video_path = "output/dandadan_maid_cafe_broadcast.mp4"
out_img = "output/dandadan_proof_sheet.jpg"

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps

sample_times = [1.0, 5.0, 9.5, 14.0, 18.5]
frames = []

for t in sample_times:
    f_idx = min(int(t * fps), total_frames - 1)
    cap.set(cv2.CAP_PROP_POS_FRAMES, f_idx)
    ret, frame = cap.read()
    if ret:
        resized = cv2.resize(frame, (360, 640))
        # Draw label
        cv2.putText(resized, f"{t:.1f}s", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)
        frames.append(resized)
cap.release()

if len(frames) == 5:
    montage = np.hstack(frames)
    cv2.imwrite(out_img, montage)
    print("Proof sheet generated successfully:", out_img)
