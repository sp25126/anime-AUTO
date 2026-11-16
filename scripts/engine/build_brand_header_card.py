from PIL import Image, ImageDraw, ImageFont
import os

def build_unlimited_brand_header(
    output_path="assets/brand_header_card.png",
    logo_path="branding/channel_logo_1024.png",
    card_width=1080,
    card_height=200
):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    card = Image.new("RGBA", (card_width, card_height), (8, 12, 22, 255))
    draw = ImageDraw.Draw(card)

    # Accent top and bottom borders
    draw.line([(0, 0), (card_width, 0)], fill=(45, 75, 120, 255), width=3)
    draw.line([(0, card_height - 1), (card_width, card_height - 1)], fill=(45, 75, 120, 255), width=3)

    # Circular Avatar on Left
    avatar_size = 150
    avatar_x = 70
    avatar_y = (card_height - avatar_size) // 2

    if os.path.exists(logo_path):
        logo_img = Image.open(logo_path).convert("RGBA").resize((avatar_size, avatar_size), Image.Resampling.LANCZOS)
        mask = Image.new("L", (avatar_size, avatar_size), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse((0, 0, avatar_size, avatar_size), fill=255)

        card.paste(logo_img, (avatar_x, avatar_y), mask)

        # Subtle neon cyan ring
        ring_draw = ImageDraw.Draw(card)
        ring_draw.ellipse((avatar_x - 3, avatar_y - 3, avatar_x + avatar_size + 3, avatar_y + avatar_size + 3), outline=(90, 175, 255, 240), width=4)

    # Typography (Script / Aesthetic Title + Clean Subtitle)
    font_title = ImageFont.truetype("C:/Windows/Fonts/segoescb.ttf", 56)
    font_sub = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)

    title_text = "Anime Fandom"
    sub_text = "* @animefandom0_0 *"

    text_x = avatar_x + avatar_size + 40
    title_y = 35
    sub_y = title_y + 72

    # Glowing title
    for dx in range(-3, 4):
        for dy in range(-3, 4):
            if abs(dx) + abs(dy) <= 4:
                draw.text((text_x + dx, title_y + dy), title_text, font=font_title, fill=(50, 130, 255, 180))
    draw.text((text_x, title_y), title_text, font=font_title, fill=(255, 255, 255, 255))

    # Clean subtext
    draw.text((text_x, sub_y), sub_text, font=font_sub, fill=(180, 220, 255, 240))

    card.save(output_path, "PNG")
    print(f"Header card saved to {output_path}")

if __name__ == "__main__":
    build_unlimited_brand_header()
