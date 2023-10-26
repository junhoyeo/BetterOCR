import easyocr
import subprocess

from threading import Thread
from queue import Queue


def easy_ocr():
    reader = easyocr.Reader(["ko", "en"])
    text = reader.readtext("demo.png", detail=0)
    text = "".join(text)
    print(text)
    return text


def tesseract_wasm():
    output = subprocess.check_output(["node", "dist"], shell=False).decode("utf-8")
    output = output.replace("\n", "\\n")
    print(output)
    return output


def wrapper(func, queue):
    queue.put(func())


q1, q2 = Queue(), Queue()
Thread(target=wrapper, args=(easy_ocr, q1)).start()
Thread(target=wrapper, args=(tesseract_wasm, q2)).start()

q1 = q1.get()
q2 = q2.get()

prompt = f"""Combine and correct OCR results [0] and [1], using \\n for line breaks. Answer in the JSON format {{data:<output:string>}}:
[0]: {q1}
[1]: {q2}"""
print(prompt)
