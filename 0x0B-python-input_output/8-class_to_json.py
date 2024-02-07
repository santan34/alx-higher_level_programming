#!/usr/bin/python3
"""
class to json
"""


def class_to_json(obj):
    """
    gives the dictionary description with the simple data structure
    :param obj: the class
    :return: a dict of the class
    """
    return obj.__dict__
