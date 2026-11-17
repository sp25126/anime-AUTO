import yt_dlp
import cv2
import os

os.makedirs("input/unlimited_ref", exist_ok=True)
url = "https://www.youtube.com/shorts/AQOqvkNZWS8"
out_video = "input/unlimited_ref/sample.mp4"

ydl_opts = {
    'format': 'bestvideo[height<=1080]+bestaudio/best',
    'outtmpl': out_video,
    'quiet': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# Sample 3 frames to see header styling exactly
cap = cv2.VideoCapture(out_video)
fps = cap.get(cv2.CAP_PROP_FPS)
for sec in [1.0, 5.0, 10.0]:
    cap.set(cv2.CAP_PROP_POS_FRAMES, int(sec * fps))
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f"input/unlimited_ref/frame_{int(sec)}s.jpg", frame)
cap.release()
print("Saved reference frames from @UnlimitedSkyyy")
