#!/usr/bin/python3

"""Defines JSON file to read in function."""
import json


def load_from_json_file(filename):
    """Create a python object from a JSON file."""
    with open(filename) as file:
        return json.load(file)
