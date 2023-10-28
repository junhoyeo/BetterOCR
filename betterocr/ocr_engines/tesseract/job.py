import pytesseract

from .mapping import LANG_CODE_MAPPING


def convert_to_tesseract_lang_code(langs: list[str]) -> str:
    return "+".join(
        [
            LANG_CODE_MAPPING[lang]
            for lang in langs
            if lang in LANG_CODE_MAPPING and LANG_CODE_MAPPING[lang] is not None
        ]
    )


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
