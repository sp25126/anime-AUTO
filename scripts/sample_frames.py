import cv2
import os

video_path = "input/dandadan_maid_cafe_raw.mp4"
out_dir = "input/samples"
os.makedirs(out_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)

sample_times = [0.5, 3.0, 7.0, 12.0, 18.0, 25.0, 32.0, 40.0, 50.0]
for t in sample_times:
    frame_idx = int(t * fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f"{out_dir}/frame_{int(t)}s.jpg", frame)
        print(f"Saved frame at {t}s")
cap.release()
