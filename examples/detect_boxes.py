import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

from betterocr import detect_boxes

image_path = ".github/images/demo-1.png"
result = detect_boxes(
    image_path,
    ["ko", "en"],
    context="퍼멘테이션 펩타인 아이케어 크림",  # product name
    tesseract={
        "config": "--psm 6 --tessdata-dir ./tessdata -c tessedit_create_boxfile=1"
    },
)
print(result)

font_path = ".github/examples/Pretendard-Medium.ttf"
font_size = 36
font = ImageFont.truetype(font_path, size=font_size, encoding="unic")

img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(
    img, cv2.COLOR_BGR2RGB
)  # Convert from BGR to RGB for correct color display in matplotlib

for item in result:
    box = item["box"]
    pt1, pt2, pt3, pt4 = box
    top_left, bottom_right = tuple(pt1), tuple(pt3)

    # Draw rectangle
    cv2.rectangle(img_rgb, top_left, bottom_right, (0, 255, 0), 2)

    # For text
    pil_img = Image.fromarray(img_rgb)
    draw = ImageDraw.Draw(pil_img)

    # Get text dimensions
    text_width = draw.textlength(item["text"], font=font)
    text_height = font_size  # line height = font size

    # Position the text just above the rectangle
    text_pos = (top_left[0], top_left[1] - text_height)

    # Draw text background rectangle
    draw.rectangle(
        [text_pos, (text_pos[0] + text_width, text_pos[1] + text_height)],
        fill=(0, 255, 0),
    )

    # Draw text
    draw.text(text_pos, item["text"], font=font, fill=(0, 0, 0))

    # Convert the PIL image back to an OpenCV image
    img_rgb = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)


height, width, _ = img.shape

# Convert pixel dimensions to inches
dpi = 80  # Assuming default matplotlib dpi
fig_width = width / dpi
fig_height = height / dpi

plt.figure(figsize=(fig_width, fig_height))
plt.imshow(img_rgb)
plt.axis("off")
plt.show()
