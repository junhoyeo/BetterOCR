from ..engines.easy_pororo_ocr import EasyPororoOcr, load_with_filter


def parse_languages(lang: list[str]):
    languages = []
    for l in lang:
        if l in ["ko", "en"]:
            languages.append(l)

    if len(languages) == 0:
        languages = ["ko"]

    return languages


def default_ocr(_options):
    lang = parse_languages(_options["lang"])
    return EasyPororoOcr(lang)


def job_easy_pororo_ocr(_options):
    image = load_with_filter(_options["path"])

    ocr = _options.get("ocr")
    if not ocr:
        ocr = default_ocr(_options)

    text = ocr.run_ocr(image, debug=False)

    if isinstance(text, list):
        text = "\\n".join(text)

    print("[*] job_easy_pororo_ocr", text)
    return text


def job_easy_pororo_ocr_boxes(_options):
    ocr = default_ocr(_options)
    job_easy_pororo_ocr({**_options, "ocr": ocr})
    return ocr.get_boxes()
