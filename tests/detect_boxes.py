from betterocr import detect_boxes

text = detect_boxes(
    "demo.png",
    ["ko", "en"],
    context="",
    tesseract={
        "config": "--psm 6 --tessdata-dir ./tessdata -c tessedit_create_boxfile=1"
    },
    openai={
        "model": "gpt-3.5-turbo",
    },
)
print(text)
