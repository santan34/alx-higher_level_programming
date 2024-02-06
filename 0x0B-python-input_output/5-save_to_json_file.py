#!/usr/bin/python3
"""
Saves object to a file
"""
import json

def save_to_json_file(my_obj, filename):
    """
    saves a json object to a file
    :param my_obj: the object to save
    :param filename: the file to save to
    :return: Nothing
    """
    with open(filename, encoding="UTF8", mode="w") as file:
        file.write(json.dumps(my_obj))
