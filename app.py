import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# change directory with your excel and image file directory
xlsx_dir = r"D:\Development\sertificate-generator-with-py\list.xlsx"
sertificate_dir = r"D:\Development\sertificate-generator-with-py\sertificate.jpg"

data = pd.read_excel(xlsx_dir)
name_list = data["Name"].tolist()

for i in name_list:
    img = Image.open(sertificate_dir)
    draw = ImageDraw.Draw(img)

    font_size = 200
    font = ImageFont.truetype("arial.ttf", font_size)
    text_width, _ = draw.textsize(i, font=font)

    center_x_position = (img.width-text_width)/2
    text_y_position = 800

    location_x_y = (center_x_position, text_y_position)
    # RGB color
    text_color = (0, 0, 0)

    draw.text(location_x_y, i, fill=text_color, font=font)
    img.save("certificate_" + i + ".pdf")
