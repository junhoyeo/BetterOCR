import cv2
import numpy as np
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


def job_tesseract_boxes(_options):
    lang = convert_to_tesseract_lang_code(_options["lang"])
    df = pytesseract.image_to_data(
        _options["path"],
        lang=lang,
        **_options["tesseract"],
        output_type=pytesseract.Output.DATAFRAME
        # pass rest of tesseract options here.
    )

    # https://stackoverflow.com/questions/74221064/draw-a-rectangle-around-a-string-of-words-using-pytesseract
    boxes = []
    for line_num, words_per_line in df.groupby("line_num"):
        words_per_line = words_per_line[words_per_line["conf"] >= 5]
        if len(words_per_line) == 0:
            continue

        words = words_per_line["text"].values
        line = " ".join(words)

        word_boxes = []
        for left, top, width, height in words_per_line[
            ["left", "top", "width", "height"]
        ].values:
            word_boxes.append((left, top))
            word_boxes.append((left + width, top + height))

        x, y, w, h = cv2.boundingRect(np.array(word_boxes))
        boxes.append(
            {
                "box": [[x, y], [x + w, y], [x + w, y + h], [x, y + h]],
                "text": line,
            }
        )

    return boxes
