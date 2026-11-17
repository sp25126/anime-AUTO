import cv2
import numpy as np

# Load the Dandadan raw clip and composite with the Unlimited Sky style layout
cap = cv2.VideoCapture("input/dandadan_maid_cafe_raw.mp4")
cap.set(cv2.CAP_PROP_POS_MSEC, 5000) # 5.0s
ret, frame = cap.read()
cap.release()

if ret:
    # Scale frame to 1080x608 (16:9 native centered)
    fg = cv2.resize(frame, (1080, 608))
    
    # Background: scale to 1080x1920, heavy blur
    bg = cv2.resize(frame, (1080, 1920))
    bg = cv2.GaussianBlur(bg, (51, 51), 25)
    bg = cv2.convertScaleAbs(bg, alpha=0.5, beta=-20) # darken

    # Paste fg in center: y starts at (1920 - 608) // 2 = 656
    y_offset = (1920 - 608) // 2
    bg[y_offset:y_offset+608, 0:1080] = fg

    # Overlay our header
    header = cv2.imread("assets/unlimited_style_overlay.png", cv2.IMREAD_UNCHANGED)
    alpha = header[:, :, 3] / 255.0
    for c in range(3):
        bg[:, :, c] = (1.0 - alpha) * bg[:, :, c] + alpha * header[:, :, c]

    cv2.imwrite("output/unlimited_style_preview.jpg", bg)
    print("Preview generated at output/unlimited_style_preview.jpg")
