#!/usr/bin/python3
"""
inherits from
"""


def inherits_from(obj, a_class):
    """
    returns true if  the obj is a sub class of a_class
    :param obj: the obj to examine
    :param a_class: the class to be checked
    :return: True or false
    """
    if obj is type(a_class):
        return False
    return (issubclass(type(obj), a_class))
