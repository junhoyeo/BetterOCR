from ..easy_pororo_ocr import EasyPororoOcr, load_with_filter


def job_easy_pororo_ocr(_options):
    image = load_with_filter(_options["path"])
    m_ocr = EasyPororoOcr()
    text = m_ocr.run_ocr(image, debug=False)
    print("[*] job_easy_pororo_ocr", text)
    return text


# def job_easy_ocr_boxes(_options):
#     reader = easyocr.Reader(_options["lang"])
#     boxes = reader.readtext(_options["path"], output_format="dict")
#     for box in boxes:
#         box["box"] = box.pop("boxes")
#     return boxes
