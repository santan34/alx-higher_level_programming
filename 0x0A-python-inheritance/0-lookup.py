#!/usr/bin/python3
"""
returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    returns the returns of available attributes and methods of an object
    :param obj: the object
    :return: the list
    """
    return ([x for x in dir(obj)])
