import subprocess
import os

python_exe = r"C:\Users\saumy\AppData\Local\Programs\Python\Python311\python.exe"
os.makedirs("output/dissections/unlimited", exist_ok=True)
os.makedirs("output/dissections/hasib", exist_ok=True)
os.makedirs("output/dissections/midnight", exist_ok=True)

# 1. Download UnlimitedSkyyy sample (AQOqvkNZWS8, 32s)
print("Downloading UnlimitedSkyyy sample...")
cmd1 = [python_exe, "-m", "yt_dlp", "https://www.youtube.com/shorts/AQOqvkNZWS8", "-o", "output/dissections/unlimited_sample.mp4", "--no-warnings", "-f", "mp4/best"]
subprocess.run(cmd1)

# 2. Download hasibkunamv sample (M-0dbpKyyQ0, 25s)
print("Downloading hasibkunamv sample...")
cmd2 = [python_exe, "-m", "yt_dlp", "https://www.youtube.com/shorts/M-0dbpKyyQ0", "-o", "output/dissections/hasib_sample.mp4", "--no-warnings", "-f", "mp4/best"]
subprocess.run(cmd2)

# Extract 1 fps frames for dissection
if os.path.exists("output/dissections/unlimited_sample.mp4"):
    subprocess.run(["ffmpeg", "-y", "-i", "output/dissections/unlimited_sample.mp4", "-r", "1", "-vframes", "10", "output/dissections/unlimited/frame_%02d.jpg"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Extracted UnlimitedSkyyy 1 fps frames")

if os.path.exists("output/dissections/hasib_sample.mp4"):
    subprocess.run(["ffmpeg", "-y", "-i", "output/dissections/hasib_sample.mp4", "-r", "1", "-vframes", "10", "output/dissections/hasib/frame_%02d.jpg"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("Extracted hasibkunamv 1 fps frames")
