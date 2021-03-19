import pandas as pd
from PIL import Image, ImageDraw, ImageFont

data = pd.read_excel(r'D:\Development\sertificate-generator-with-py\list.xlsx')
name_list = data["Name"].tolist()

for i in name_list:
    img = Image.open(
        r'D:\Development\sertificate-generator-with-py\sertificate.jpg')
    draw = ImageDraw.Draw(img)

    font_size = 200
    font = ImageFont.truetype("arial.ttf", font_size)
    text_width, _ = draw.textsize(i, font=font)

    center_x_position = (img.width-text_width)/2
    text_y_position = 800

    location = (center_x_position, text_y_position)
    # RGB color
    text_color = (0, 0, 0)

    draw.text(location, i, fill=text_color, font=font)
    img.save("certificate_" + i + ".pdf")
