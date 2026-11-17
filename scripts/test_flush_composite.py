import cv2
import numpy as np

# Load the background image
bg = cv2.imread("assets/backgrounds/romcom_sunset.webp")
bg = cv2.resize(bg, (1080, 1920))

# Load Dandadan raw clip
cap = cv2.VideoCapture("input/dandadan_maid_cafe_raw.mp4")
cap.set(cv2.CAP_PROP_POS_MSEC, 5000)
ret, frame = cap.read()
cap.release()

if ret:
    fg = cv2.resize(frame, (1080, 608))
    
    # 1. Video Position: centered vertically (y: 656 to 1264)
    y_video = (1920 - 608) // 2
    
    # 2. Header Card Position: exactly flush above video (y: 456 to 656)
    header_img = cv2.imread("assets/brand_header_card.png", cv2.IMREAD_UNCHANGED)
    h_h, h_w, _ = header_img.shape
    y_header = y_video - h_h

    # Composite Header Card
    alpha = header_img[:, :, 3] / 255.0
    for c in range(3):
        bg[y_header:y_header+h_h, 0:1080, c] = (
            (1.0 - alpha) * bg[y_header:y_header+h_h, 0:1080, c] + alpha * header_img[:, :, c]
        )

    # Composite Video
    bg[y_video:y_video+608, 0:1080] = fg

    # Clean border lines separating Header and Video
    cv2.line(bg, (0, y_header), (1080, y_header), (45, 75, 120), 2)
    cv2.line(bg, (0, y_video), (1080, y_video), (45, 75, 120), 2)
    cv2.line(bg, (0, y_video+608), (1080, y_video+608), (45, 75, 120), 2)

    cv2.imwrite("output/custom_bg_unlimited_preview_flush.jpg", bg)
    print("Flush preview generated at output/custom_bg_unlimited_preview_flush.jpg")
