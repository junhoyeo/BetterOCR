from betterocr.parsers import extract_list
import json


def is_same_list(dict1, dict2):
    return json.dumps(dict1) == json.dumps(dict2)


def test_extract_list__default():
    assert is_same_list(
        extract_list('[{"box":[],"text":""}]'),
        [{"box": [], "text": ""}],
    )
    assert is_same_list(
        extract_list(
            """
            Using the provided context and both OCR data sets, I'll merge, correct, and provide the result:
            [
                {
                    "box": [123, 456, 789, 101112],
                    "text": "Hello World!"
                }
            ]
            """
        ),
        [{"box": [123, 456, 789, 101112], "text": "Hello World!"}],
    )
