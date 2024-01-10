#!/usr/bin/python3
"""This fuctions is saving json into file."""
import json


def save_to_json_file(my_obj, filename):
    """This fuctions is saving json into file."""
    with open(filename, "w")  as file:
              return json.dump(my_obj, file)