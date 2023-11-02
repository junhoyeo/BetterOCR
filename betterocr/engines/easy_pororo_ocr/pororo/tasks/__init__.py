"""
this code is adapted from https://github.com/black7375/korean_ocr_using_pororo

Apache License 2.0 @yunwoong7
Apache License 2.0 @black7375
"""

# flake8: noqa
"""
__init__.py for import child .py files

    isort:skip_file
"""

# Utility classes & functions
# import pororo.tasks.utils
from .utils.download_utils import download_or_load
from .utils.base import (
    PororoBiencoderBase,
    PororoFactoryBase,
    PororoGenerationBase,
    PororoSimpleBase,
    PororoTaskGenerationBase,
)

# Factory classes
from .optical_character_recognition import PororoOcrFactory
