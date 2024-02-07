#!/usr/bin/python3
"""
To json string
"""
import json


def to_json_string(my_obj):
    """
    returns json representation of a object
    :param my_obj: the string
    :return: jason representation
    """
    return json.dumps(my_obj)
