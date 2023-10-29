from threading import Thread
import json
from queue import Queue
import os

from openai import OpenAI

from .parsers import extract_json, extract_list
from .ocr_engines import (
    job_easy_ocr,
    job_easy_ocr_boxes,
    job_tesseract,
    job_tesseract_boxes,
)


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


def detect_boxes(
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

    Thread(target=wrapper, args=(job_easy_ocr_boxes, options, q1)).start()
    Thread(target=wrapper, args=(job_tesseract_boxes, options, q2)).start()

    boxes_1 = q1.get()
    boxes_2 = q2.get()

    optional_context_prompt = (
        " " + "Please refer to the keywords and spelling in [context]"
        if options["context"]
        else ""
    )
    optional_context_prompt_data = (
        f"[context]: {options['context']}" if options["context"] else ""
    )

    boxes_1_json = json.dumps(boxes_1, ensure_ascii=False, default=int)
    boxes_2_json = json.dumps(boxes_2, ensure_ascii=False, default=int)

    prompt = f"""Merge and correct OCR data [0] and [1]. Langauge is in {'+'.join(options['lang'])}. Remove unintended noise.{optional_context_prompt} Answer in the JSON format. Ensure coordinates are integers (round based on confidence if necessary) and output in JSON format (indent=0): Array({{box:[[int,int],[int,int],[int,int],[int,int]],text:str}}):
    [0]: {boxes_1_json}
    [1]: {boxes_2_json}
    {optional_context_prompt_data}"""

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
    output = output.replace("\n", "")
    print("[*] LLM (1)", output)
    return extract_list(output)


def detect_boxes_async():
    """Unimplemented"""
    raise NotImplementedError
