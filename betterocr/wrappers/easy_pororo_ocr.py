from ..engines.easy_pororo_ocr import EasyPororoOcr, load_with_filter


def job_easy_pororo_ocr(_options):
    image = load_with_filter(_options["path"])
    m_ocr = EasyPororoOcr()
    text = m_ocr.run_ocr(image, debug=False)

    if isinstance(text, list):
        text = "\\n".join(text)

    print("[*] job_easy_pororo_ocr", text)
    return text
