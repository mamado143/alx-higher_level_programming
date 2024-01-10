#!/usr/bin/python3

"""Defines function that returns jsoni."""

def to_json_string(my_obj):
    """Returns the JSON representation of a string object.

    Args:
        my_obj (object): object to be converted to JSON.
    """
    import json
    json_string = json.dumps(my_obj)
    return json_string
