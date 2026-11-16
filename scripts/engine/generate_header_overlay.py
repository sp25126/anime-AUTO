from PIL import Image, ImageDraw, ImageFont
import os

def create_cinematic_header(
    output_path="assets/dandadan_header_overlay.png",
    width=1080,
    height=1920,
    title_text="HER FIRST DAY AS A MAID",
    subtitle_text="DANDADAN • MOMO AYASE"
):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Gradient feather overlay at the top (0 to 380px)
    for y in range(380):
        alpha = int(180 * (1.0 - (y / 380.0)))
        draw.line([(0, y), (width, y)], fill=(0, 0, 0, alpha))

    # Gradient feather overlay at the bottom (1540 to 1920px)
    for y in range(1540, 1920):
        alpha = int(160 * ((y - 1540) / 380.0))
        draw.line([(0, y), (width, y)], fill=(0, 0, 0, alpha))

    # Font handling
    font_path = "C:/Windows/Fonts/impact.ttf"
    sub_font_path = "C:/Windows/Fonts/arialbd.ttf"
    
    font_title = ImageFont.truetype(font_path, 52)
    font_sub = ImageFont.truetype(sub_font_path, 28)

    # Render top title
    # Title centered at y = 140
    t_bbox = draw.textbbox((0, 0), title_text, font=font_title)
    t_w = t_bbox[2] - t_bbox[0]
    t_x = (width - t_w) // 2
    t_y = 120

    # Glow / stroke effect
    for dx in range(-4, 5):
        for dy in range(-4, 5):
            if abs(dx) + abs(dy) <= 6:
                draw.text((t_x + dx, t_y + dy), title_text, font=font_title, fill=(0, 0, 0, 240))

    # Main text in vibrant white / yellow gradient feel
    draw.text((t_x, t_y), title_text, font=font_title, fill=(255, 235, 60, 255))

    # Render subtle series subtitle
    s_bbox = draw.textbbox((0, 0), subtitle_text, font=font_sub)
    s_w = s_bbox[2] - s_bbox[0]
    s_x = (width - s_w) // 2
    s_y = t_y + 68

    for dx in range(-2, 3):
        for dy in range(-2, 3):
            draw.text((s_x + dx, s_y + dy), subtitle_text, font=font_sub, fill=(0, 0, 0, 200))
    draw.text((s_x, s_y), subtitle_text, font=font_sub, fill=(230, 230, 230, 240))

    # Save overlay
    img.save(output_path, "PNG")
    print(f"Cinematic header overlay saved to {output_path}")

if __name__ == "__main__":
    create_cinematic_header()
