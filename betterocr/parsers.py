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
