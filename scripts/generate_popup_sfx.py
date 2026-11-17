import numpy as np
import wave
import struct
import os

# Create an ear-catching, cinematic bass chime / whoosh riser popup sound
# Sample rate: 44100 Hz, Duration: 2.2 seconds
sr = 44100
dur = 2.2
total_samples = int(sr * dur)
t = np.linspace(0, dur, total_samples, endpoint=False)

# 1. Sub Bass Drop (80 Hz -> 40 Hz) with exponential decay
bass_freq = 85 * np.exp(-1.5 * t)
bass = np.sin(2 * np.pi * bass_freq * t) * np.exp(-2.2 * t)

# 2. Celestial Metallic Chime / Sparkle (F# major triad harmonics: 740 Hz, 1110 Hz, 1480 Hz)
chime1 = np.sin(2 * np.pi * 740 * t) * np.exp(-3.5 * t)
chime2 = np.sin(2 * np.pi * 1110 * t) * np.exp(-4.5 * t)
chime3 = np.sin(2 * np.pi * 1480 * t) * np.exp(-5.5 * t)
chime = 0.5 * chime1 + 0.3 * chime2 + 0.2 * chime3

# 3. Quick High-Pass Whoosh Swell into impact at t=0.15s
rise_env = np.where(t < 0.15, (t / 0.15)**2, np.exp(-6 * (t - 0.15)))
noise = np.random.uniform(-1, 1, total_samples) * rise_env * 0.25

# 4. Master combination & soft clipping
master = 0.65 * bass + 0.45 * chime + 0.35 * noise
master = np.tanh(master * 1.4) # analog saturation
master = master / np.max(np.abs(master)) * 0.92

# Stereo widening
left = master
right = np.roll(master, int(sr * 0.008)) # 8ms Haas effect delay for 3D width

os.makedirs("branding/audio", exist_ok=True)
out_wav = "branding/audio/logo_popup_sfx.wav"

with wave.open(out_wav, "w") as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2) # 16-bit
    wf.setframerate(sr)
    interleaved = np.empty((2 * total_samples,), dtype=np.int16)
    interleaved[0::2] = (left * 32767).astype(np.int16)
    interleaved[1::2] = (right * 32767).astype(np.int16)
    wf.writeframes(interleaved.tobytes())

print(f"Generated logo popup SFX: {out_wav} ({dur}s)")
