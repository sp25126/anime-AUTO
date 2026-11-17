import whisper
import json

model = whisper.load_model("tiny")
res = model.transcribe("input/dandadan_maid_cafe_raw.mp4")

print("=== Transcribed Segments ===")
for seg in res.get("segments", [])[:15]:
    start = seg["start"]
    end = seg["end"]
    text = seg["text"]
    print(f"[{start:.2f}s -> {end:.2f}s] {text}")
