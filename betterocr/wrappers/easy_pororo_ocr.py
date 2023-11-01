from ..engines.easy_pororo_ocr import EasyPororoOcr, load_with_filter


def job_easy_pororo_ocr(_options):
    image = load_with_filter(_options["path"])
    languages = _options["lang"]

    lang = []
    for l in languages:
        if l in ["ko", "en"]:
            lang.append(l)

    if len(lang) == 0:
        lang = ["ko"]

    ocr = EasyPororoOcr(lang)
    text = ocr.run_ocr(image, debug=False)

    if isinstance(text, list):
        text = "\\n".join(text)

    print("[*] job_easy_pororo_ocr", text)
    return text
