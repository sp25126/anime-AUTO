import cv2
import numpy as np

# Load background (Romcom sunset Shinkai clouds)
bg = cv2.imread("assets/backgrounds/romcom_sunset.webp")
bg = cv2.resize(bg, (1080, 1920))

# Load Dandadan raw clip frame
cap = cv2.VideoCapture("input/dandadan_maid_cafe_raw.mp4")
cap.set(cv2.CAP_PROP_POS_MSEC, 5000)
ret, frame = cap.read()
cap.release()

if ret:
    # 16:9 video scaled to 1080 width -> 1080x608
    fg = cv2.resize(frame, (1080, 608))
    
    # Position video in the center: y = 656 to 1264
    y_video = (1920 - 608) // 2
    
    # Place header card right above video or at y = 200:
    # In Unlimited Sky, the header card sits above the video (e.g. y = 380 to 580)
    header_img = cv2.imread("assets/brand_header_card.png", cv2.IMREAD_UNCHANGED)
    h_h, h_w, _ = header_img.shape
    y_header = y_video - h_h - 40 # 40px gap or flush

    # Composite header card
    alpha = header_img[:, :, 3] / 255.0
    for c in range(3):
        bg[y_header:y_header+h_h, 0:1080, c] = (
            (1.0 - alpha) * bg[y_header:y_header+h_h, 0:1080, c] + alpha * header_img[:, :, c]
        )

    # Composite centered video with clean border
    bg[y_video:y_video+608, 0:1080] = fg
    cv2.line(bg, (0, y_video), (1080, y_video), (45, 75, 120), 2)
    cv2.line(bg, (0, y_video+608), (1080, y_video+608), (45, 75, 120), 2)

    cv2.imwrite("output/custom_bg_unlimited_preview.jpg", bg)
    print("Generated preview with custom generated background!")
