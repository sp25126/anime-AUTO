"""
Background Library Generator for Aesthetic Anime Shorts.
Provides procedurally generated and curated painterly anime atmospheric backgrounds
(Golden Hour Sunset, Twilight Shinkai Sky, Midnight Aurora, Rainy Tokyo Dusk).
No phone UI, no app overlays - 100% clean 1080x1920 vertical anime atmosphere.
"""

import os
import cv2
import numpy as np

WORKSPACE = os.path.dirname(os.path.dirname(__file__))
BG_DIR = os.path.join(WORKSPACE, "public", "backgrounds")
os.makedirs(BG_DIR, exist_ok=True)

def generate_golden_hour_sky():
    # 1080 x 1920 sunset gradient: deep twilight blue top -> vibrant amber orange -> soft warm pink horizon
    h, w = 1920, 1080
    bg = np.zeros((h, w, 3), dtype=np.uint8)

    # Gradient colors (BGR format)
    top_color = np.array([120, 45, 25], dtype=np.float32)       # Deep Indigo
    mid_color = np.array([80, 110, 240], dtype=np.float32)      # Warm Amber Coral
    bottom_color = np.array([130, 175, 255], dtype=np.float32)  # Golden Glow

    for y in range(h):
        ratio = y / float(h)
        if ratio < 0.5:
            local_r = ratio / 0.5
            color = (1.0 - local_r) * top_color + local_r * mid_color
        else:
            local_r = (ratio - 0.5) / 0.5
            color = (1.0 - local_r) * mid_color + local_r * bottom_color
        bg[y, :] = color.astype(np.uint8)

    # Add soft painted cloud patches
    cv2.circle(bg, (int(w*0.3), int(h*0.35)), 400, (110, 140, 245), -1)
    cv2.circle(bg, (int(w*0.75), int(h*0.42)), 450, (120, 150, 250), -1)
    cv2.circle(bg, (int(w*0.5), int(h*0.75)), 550, (140, 190, 255), -1)

    # Heavy bilateral + Gaussian blur for painterly studio feel
    blurred = cv2.GaussianBlur(bg, (181, 181), 0)
    out_path = os.path.join(BG_DIR, "golden_hour_sky.jpg")
    cv2.imwrite(out_path, blurred)
    print("Generated:", out_path)

def generate_shinkai_twilight():
    # Makoto Shinkai style twilight: Deep navy top -> violet -> cyan glow horizon
    h, w = 1920, 1080
    bg = np.zeros((h, w, 3), dtype=np.uint8)

    top_color = np.array([80, 20, 15], dtype=np.float32)       # Deep Night Navy
    mid_color = np.array([180, 50, 120], dtype=np.float32)     # Vivid Violet
    bottom_color = np.array([240, 180, 60], dtype=np.float32)  # Turquoise Cyan

    for y in range(h):
        ratio = y / float(h)
        if ratio < 0.6:
            local_r = ratio / 0.6
            color = (1.0 - local_r) * top_color + local_r * mid_color
        else:
            local_r = (ratio - 0.6) / 0.4
            color = (1.0 - local_r) * mid_color + local_r * bottom_color
        bg[y, :] = color.astype(np.uint8)

    # Ambient cloud puffs
    cv2.circle(bg, (int(w*0.2), int(h*0.5)), 450, (200, 70, 140), -1)
    cv2.circle(bg, (int(w*0.8), int(h*0.6)), 500, (220, 120, 90), -1)

    blurred = cv2.GaussianBlur(bg, (199, 199), 0)
    out_path = os.path.join(BG_DIR, "shinkai_twilight.jpg")
    cv2.imwrite(out_path, blurred)
    print("Generated:", out_path)

if __name__ == "__main__":
    generate_golden_hour_sky()
    generate_shinkai_twilight()
