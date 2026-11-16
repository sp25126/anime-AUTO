from PIL import Image, ImageDraw, ImageFont
import os

def generate_perfect_unlimited_header(
    output_path="assets/unlimited_style_overlay.png",
    logo_path="branding/channel_logo_1024.png",
    width=1080,
    height=1920
):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)

    header_top = 220
    header_bottom = 440
    
    # Deep midnight card
    draw.rectangle([(0, header_top), (width, header_bottom)], fill=(8, 12, 22, 255))
    draw.line([(0, header_top), (width, header_top)], fill=(40, 60, 95, 255), width=3)
    draw.line([(0, header_bottom), (width, header_bottom)], fill=(40, 60, 95, 255), width=3)

    # Circular Avatar
    avatar_size = 160
    avatar_x = 90
    avatar_y = header_top + (header_bottom - header_top - avatar_size) // 2

    if os.path.exists(logo_path):
        logo_img = Image.open(logo_path).convert("RGBA").resize((avatar_size, avatar_size), Image.Resampling.LANCZOS)
        mask = Image.new("L", (avatar_size, avatar_size), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse((0, 0, avatar_size, avatar_size), fill=255)

        canvas.paste(logo_img, (avatar_x, avatar_y), mask)

        # Subtle neon cyan ring
        ring_draw = ImageDraw.Draw(canvas)
        ring_draw.ellipse((avatar_x - 3, avatar_y - 3, avatar_x + avatar_size + 3, avatar_y + avatar_size + 3), outline=(100, 180, 255, 240), width=4)

    # Fonts
    font_title = ImageFont.truetype("C:/Windows/Fonts/segoescb.ttf", 60)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 30)

    title_text = "Anime Fandom"
    sub_text = "* @animefandom0_0 *"

    text_x = avatar_x + avatar_size + 45
    title_y = header_top + 42
    sub_y = title_y + 75

    # Glowing title
    for dx in range(-3, 4):
        for dy in range(-3, 4):
            if abs(dx) + abs(dy) <= 4:
                draw.text((text_x + dx, title_y + dy), title_text, font=font_title, fill=(60, 140, 255, 180))
    draw.text((text_x, title_y), title_text, font=font_title, fill=(255, 255, 255, 255))

    # Clean subtext
    draw.text((text_x, sub_y), sub_text, font=font_sub, fill=(180, 215, 255, 240))

    canvas.save(output_path, "PNG")
    print("Regenerated clean header.")

if __name__ == "__main__":
    generate_perfect_unlimited_header()
