import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

# === CONFIGURATION ===
spreadsheet = "Tier List Maker.xlsx"          # or "Tier List Maker.csv"
character_img_folder = "characters/"          # folder with character PNGs
output_folder = "output/"
background_path = "background.png"            # must be 200x200
font_path = "Tolyer Bold no.1.ttf"            # or another TTF font
font_size = 46                                 # larger size for visibility
canvas_size = (200, 200)

# Create output folder if needed
os.makedirs(output_folder, exist_ok=True)

# Load spreadsheet
df = pd.read_excel(spreadsheet)  # use read_csv() if CSV

for index, row in df.iterrows():
    username = row["Username"]
    character = row["Character"]

    # Step 1: Load background
    try:
        bg = Image.open(background_path).convert("RGBA").resize(canvas_size)
    except Exception as e:
        print(f"Could not load background: {e}")
        continue

    # Step 2: Load and paste character image
    char_path = os.path.join(character_img_folder, f"{character.lower()}.png")
    if not os.path.exists(char_path):
        print(f"[!] Character image not found: {char_path}")
        continue

    char_img = Image.open(char_path).convert("RGBA").resize(canvas_size)
    bg.alpha_composite(char_img)

    # Step 3: Draw username text at bottom center
    draw = ImageDraw.Draw(bg)
    text = username.upper()

    # Start with a big font size and shrink until it fits
    max_width = canvas_size[0] - 10  # 5px padding on each side
    font_size_dynamic = 70
    while font_size_dynamic > 10:
        try:
            font = ImageFont.truetype(font_path, font_size_dynamic)
        except:
            font = ImageFont.load_default()
            break

        bbox = draw.textbbox((0, 0), text, font=font, stroke_width=2)
        text_width = bbox[2] - bbox[0]
        if text_width <= max_width:
            break
        font_size_dynamic -= 1

    text_height = bbox[3] - bbox[1]
    x = (canvas_size[0] - text_width) // 2
    y = canvas_size[1] - text_height - 15  # Raised 10 pixels higher

    draw.text(
        (x, y), text, font=font,
        fill=(255, 255, 255, 255),
        stroke_width=2,
        stroke_fill=(0, 0, 0)
    )


    # Step 4: Export final image
    output_path = os.path.join(output_folder, f"{username}.png")
    bg.save(output_path)
    print(f"[✓] Saved {output_path}")
