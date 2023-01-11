#!/usr/bin/python3
import json


def from_json_string(my_str):
    try:
        json_obj = json.loads(my_str)
    except json.decoder.JSONDecodeError as e:
        raise ValueError("Invalid JSON string: {}".format(e))
    if not isinstance(json_obj, (dict, list)):
        raise ValueError("JSON string must represent an object or an array")
    return json_obj
