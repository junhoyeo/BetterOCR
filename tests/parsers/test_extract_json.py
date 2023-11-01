from betterocr.parsers import extract_json
import json


def is_same_dict(dict1, dict2):
    return json.dumps(dict1) == json.dumps(dict2)


def test_extract_json__default():
    assert is_same_dict(extract_json('{"data": "hello"}'), {"data": "hello"})
    assert is_same_dict(
        extract_json(
            """
            Using the provided context and both OCR data sets, I'll merge, correct, and provide the result:
            {"data": "{Optical Character Recognition}"}
            """
        ),
        {"data": "{Optical Character Recognition}"},
    )


def test_extract_json__newlines():
    assert is_same_dict(
        extract_json('{"data": "hello\nworld"}'), {"data": "hello\nworld"}
    )


def test_extract_json__newlines_escaped():
    assert is_same_dict(
        extract_json('{"data": "hello\\nworld"}'), {"data": "hello\nworld"}
    )


def test_extract_json__multiple_dicts_should_return_first_occurrence():
    assert is_same_dict(
        extract_json(
            """
            {"data": "JSON Data 1"}
            {"data": "JSON Data 2"}
            """
        ),
        {"data": "JSON Data 1"},
    )
    assert is_same_dict(
        extract_json(
            """
            {"invalid_key": "JSON Data 1"}
            {"data": "JSON Data 2"}
            """
        ),
        {"data": "JSON Data 2"},
    )
