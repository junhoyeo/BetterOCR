from threading import Thread
from queue import Queue
import easyocr
import pytesseract


def job_easy_ocr(_options):
    reader = easyocr.Reader(_options["lang"])
    text = reader.readtext(_options["path"], detail=0)
    text = "".join(text)
    print("[*] job_easy_ocr", text)
    return text


def convert_to_tesseract_lang_code(langs: list[str]) -> str:
    # Mapping from easyocr language codes to tesseract language codes.
    # You might need to expand this if you are using other languages.
    mapping = {
        "en": "eng",
        "ko": "kor",
    }
    return "+".join([mapping[lang] for lang in langs if lang in mapping])


def job_tesseract_ocr(_options):
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


def wrapper(func, args, queue):
    queue.put(func(args))


q1, q2 = Queue(), Queue()
options = {
    "path": "demo.png",
    "lang": ["ko", "en"],
    "tesseract": {
        # tesseract config
        "config": "--tessdata-dir ./tessdata"
    },
}

Thread(target=wrapper, args=(job_easy_ocr, options, q1)).start()
Thread(target=wrapper, args=(job_tesseract_ocr, options, q2)).start()

q1 = q1.get()
q2 = q2.get()

prompt = f"""Combine and correct OCR results [0] and [1], using \\n for line breaks. Answer in the JSON format {{data:<output:string>}}:
[0]: {q1}
[1]: {q2}"""

print("=====")
print(prompt)
