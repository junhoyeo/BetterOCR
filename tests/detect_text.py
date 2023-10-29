from betterocr import detect_text

text = detect_text(
    "demo.png",
    ["ko", "en"],
    context="",
    tesseract={"config": "--tessdata-dir ./tessdata"},
    openai={
        "model": "gpt-3.5-turbo",
    },
)
print(text)
