from threading import Thread
from queue import Queue
import os

from openai import OpenAI

from .parsers import extract_json
from .ocr_engines import job_easy_ocr, job_tesseract


def wrapper(func, args, queue):
    queue.put(func(args))


# custom error
class NoTextDetectedError(Exception):
    pass


def detect():
    """Unimplemented"""
    raise NotImplementedError


def detect_async():
    """Unimplemented"""
    raise NotImplementedError


def detect_text(
    image_path: str,
    lang: list[str],
    context: str = "",
    tesseract: dict = {},
    openai: dict = {"model": "gpt-4"},
):
    """Detect text from an image using EasyOCR and Tesseract, then combine and correct the results using OpenAI's LLM."""
    q1, q2 = Queue(), Queue()
    options = {
        "path": image_path,  # "demo.png",
        "lang": lang,  # ["ko", "en"]
        "context": context,
        "tesseract": tesseract,
        "openai": openai,
    }

    Thread(target=wrapper, args=(job_easy_ocr, options, q1)).start()
    Thread(target=wrapper, args=(job_tesseract, options, q2)).start()

    q1 = q1.get()
    q2 = q2.get()

    optional_context_prompt = (
        f"[context]: {options['context']}" if options["context"] else ""
    )

    prompt = f"""Combine and correct OCR results [0] and [1], using \\n for line breaks. Langauge is in {'+'.join(options['lang'])}. Remove unintended noise. Refer to the [context] keywords. Answer in the JSON format {{data:<output:string>}}:
    [0]: {q1}
    [1]: {q2}
    {optional_context_prompt}"""

    prompt = prompt.strip()

    print("=====")
    print(prompt)

    api_key = os.environ["OPENAI_API_KEY"]
    if "API_KEY" in options["openai"] and options["openai"]["API_KEY"] != "":
        api_key = options["openai"]["API_KEY"]
    client = OpenAI(
        api_key=api_key,
    )

    print("=====")

    completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt},
        ],
        **options["openai"],
    )
    output = completion.choices[0].message.content
    print("[*] LLM", output)

    result = extract_json(output)
    print(result)

    if "data" in result:
        return result["data"]
    if isinstance(result, str):
        return result
    raise NoTextDetectedError("No text detected")


def detect_text_async():
    """Unimplemented"""
    raise NotImplementedError


def detect_boxes():
    """Unimplemented"""
    raise NotImplementedError


def detect_boxes_async():
    """Unimplemented"""
    raise NotImplementedError
