#!/usr/bin/python3
"""
From json to object
"""
import json


def from_json_string(my_str):
    """
    returns an object from a json string
    :param my_str: the string to turn to an pbject
    :return: thes object
    """
    return json.loads(my_str)
