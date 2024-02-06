#!/usr/bin/python3
"""
Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    loads an object from json file
    :param filename: the file to load from
    """
    with open(filename, mode="r", encoding="UTF8") as f:
        return json.loads(f)
