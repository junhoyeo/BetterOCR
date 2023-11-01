from .detect import (
    detect,
    detect_async,
    detect_text,
    detect_text_async,
    detect_boxes,
    detect_boxes_async,
    NoTextDetectedError,
)
from .wrappers import job_easy_ocr, job_tesseract
from .parsers import extract_json

__all__ = [
    "detect",
    "detect_async",
    "detect_text",
    "detect_text_async",
    "detect_boxes",
    "detect_boxes_async",
    "NoTextDetectedError",
    "job_easy_ocr",
    "job_tesseract",
    "extract_json",
]

__author__ = "junhoyeo"
