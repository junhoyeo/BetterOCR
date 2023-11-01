from .easy_ocr import job_easy_ocr, job_easy_ocr_boxes
from .tesseract.job import job_tesseract, job_tesseract_boxes
from .easy_pororo_ocr import job_easy_pororo_ocr, job_easy_pororo_ocr_boxes

__all__ = [
    "job_easy_ocr",
    "job_easy_ocr_boxes",
    "job_tesseract",
    "job_tesseract_boxes",
    "job_easy_pororo_ocr",
    "job_easy_pororo_ocr_boxes",
]
