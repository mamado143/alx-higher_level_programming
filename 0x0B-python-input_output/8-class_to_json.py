#!/usr/bin/python3

"""Define a python class to json."""

def class_to_json(obj):
    """Return the dictionary which represent data."""
    return obj.__dict__
