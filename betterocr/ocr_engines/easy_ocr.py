import easyocr


def job_easy_ocr(_options):
    reader = easyocr.Reader(_options["lang"])
    text = reader.readtext(_options["path"], detail=0)
    text = "".join(text)
    print("[*] job_easy_ocr", text)
    return text
