import re
import json


def extract_json(input_string):
    # Find the JSON in the string
    matches = re.findall(r'{\s*"data"\s*:\s*"(.*?)"\s*}', input_string, re.DOTALL)
    if matches:
        # Correctly escape special characters
        matches = [m.replace("\n", "\\n").replace('"', '\\"') for m in matches]
        for match in matches:
            # Construct JSON string
            json_string = f'{{"data": "{match}"}}'
            try:
                # Load the JSON and return the data
                json_obj = json.loads(json_string)
                return json_obj
            except json.decoder.JSONDecodeError:
                continue

    # If no JSON found, return None
    return None


def extract_list(s):
    stack = []
    start_position = None

    # Iterate through each character in the string
    for i, c in enumerate(s):
        if c == "[":
            if start_position is None:  # First '[' found
                start_position = i
            stack.append(c)

        elif c == "]":
            if stack:
                stack.pop()

            # If stack is empty and start was marked
            if not stack and start_position is not None:
                substring = s[start_position : i + 1]
                try:
                    list_obj = json.loads(substring)
                    for item in list_obj:
                        if "box" in item and "text" in item:
                            return list_obj
                except json.decoder.JSONDecodeError:
                    # Reset the stack and start position as this isn't a valid JSON
                    stack = []
                    start_position = None
                    continue

    # If no valid list found, return None
    return None


def rectangle_corners(rect):
    x, y, w, h = rect
    return [[x, y], [x + w, y], [x + w, y + h], [x, y + h]]
