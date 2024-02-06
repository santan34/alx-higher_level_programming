#!/usr/bin/python3
"""
Exact same object
"""


def is_same_class(obj, a_class):
    """
    returns true if the object is exactly an instance of a class
    :param obj: the object to test
    :param a_class: the class to see if the object belongs to the class
    :return: True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
