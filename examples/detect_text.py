from betterocr import detect_text

text = detect_text(
    ".github/images/demo-1.png",
    ["ko", "en"],
    context="퍼멘테이션 펩타인 아이케어 크림",  # product name
    tesseract={"config": "--tessdata-dir ./tessdata"},
    openai={
        "model": "gpt-3.5-turbo",
    },
)
print("\n")
print(text)
