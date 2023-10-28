import pytesseract


def convert_to_tesseract_lang_code(langs: list[str]) -> str:
    # Mapping from easyocr language codes to tesseract language codes.
    # You might need to expand this if you are using other languages.
    mapping = {
        "en": "eng",
        "ko": "kor",
    }
    return "+".join([mapping[lang] for lang in langs if lang in mapping])


def job_tesseract(_options):
    lang = convert_to_tesseract_lang_code(_options["lang"])
    text = pytesseract.image_to_string(
        _options["path"],
        lang=lang,
        **_options["tesseract"]
        # pass rest of tesseract options here.
    )
    text = text.replace("\n", "\\n")
    print("[*] job_tesseract_ocr", text)
    return text
