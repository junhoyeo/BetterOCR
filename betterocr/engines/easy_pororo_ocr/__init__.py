"""
this code is adapted from https://github.com/black7375/korean_ocr_using_pororo

Apache License 2.0 @yunwoong7
Apache License 2.0 @black7375
"""

import cv2
from abc import ABC, abstractmethod
from .pororo import Pororo
from .utils.image_util import plt_imshow, put_text
from .utils.image_convert import convert_coord, crop
from .utils.pre_processing import load_with_filter, roi_filter
from easyocr import Reader
import warnings

warnings.filterwarnings("ignore")


class BaseOcr(ABC):
    def __init__(self):
        self.img_path = None
        self.ocr_result = {}

    def get_ocr_result(self):
        return self.ocr_result

    def get_img_path(self):
        return self.img_path

    def show_img(self):
        plt_imshow(img=self.img_path)

    def show_img_with_ocr(self, bounding, description, vertices, point):
        img = (
            cv2.imread(self.img_path)
            if isinstance(self.img_path, str)
            else self.img_path
        )
        roi_img = img.copy()
        color = (0, 200, 0)

        x, y = point
        ocr_result = self.ocr_result if bounding is None else self.ocr_result[bounding]
        for text_result in ocr_result:
            text = text_result[description]
            rect = text_result[vertices]

            topLeft, topRight, bottomRight, bottomLeft = [
                (round(point[x]), round(point[y])) for point in rect
            ]

            cv2.line(roi_img, topLeft, topRight, color, 2)
            cv2.line(roi_img, topRight, bottomRight, color, 2)
            cv2.line(roi_img, bottomRight, bottomLeft, color, 2)
            cv2.line(roi_img, bottomLeft, topLeft, color, 2)
            roi_img = put_text(roi_img, text, topLeft[0], topLeft[1] - 20, color=color)

        plt_imshow(["Original", "ROI"], [img, roi_img], figsize=(16, 10))

    @abstractmethod
    def run_ocr(self, img_path: str, debug: bool = False):
        pass


class EasyPororoOcr(BaseOcr):
    def __init__(self, lang: list[str] = ["ko", "en"], gpu=True, **kwargs):
        super().__init__()
        self._detector = Reader(lang_list=lang, gpu=gpu, **kwargs).detect
        self.detect_result = None
        self.languages = lang

    def create_result(self, points):
        roi = crop(self.img, points)
        result = self._ocr(roi_filter(roi))
        text = " ".join(result)

        return [points, text]

    def run_ocr(self, img_path: str, debug: bool = False, **kwargs):
        self.img_path = img_path
        self.img = cv2.imread(img_path) if isinstance(img_path, str) else self.img_path

        lang = "ko" if "ko" in self.languages else "en"
        self._ocr = Pororo(task="ocr", lang=lang, model="brainocr", **kwargs)

        self.detect_result = self._detector(self.img, slope_ths=0.3, height_ths=1)
        if debug:
            print(self.detect_result)

        horizontal_list, free_list = self.detect_result

        rois = [convert_coord(point) for point in horizontal_list[0]] + free_list[0]

        self.ocr_result = list(
            filter(
                lambda result: len(result[1]) > 0,
                [self.create_result(roi) for roi in rois],
            )
        )

        if len(self.ocr_result) != 0:
            ocr_text = list(map(lambda result: result[1], self.ocr_result))
        else:
            ocr_text = "No text detected."

        if debug:
            self.show_img_with_ocr(None, 1, 0, [0, 1])

        return ocr_text

    def get_boxes(self):
        x, y = [0, 1]
        ocr_result = self.ocr_result
        description = 1
        vertices = 0

        items = []

        for text_result in ocr_result:
            text = text_result[description]
            rect = text_result[vertices]
            rect = [[round(point[x]), round(point[y])] for point in rect]
            items.append({"box": rect, "text": text})

        return items


__all__ = ["EasyPororoOcr", "load_with_filter"]
