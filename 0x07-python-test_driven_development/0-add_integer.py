#!/usr/bin/python3
"""
Adds two integers together
"""


def add_integer(a, b=98):
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return int(a+b)
    """
    the function two add the two numbers
    floats will be cast to int
    Args:
        a(int): an integer to add
        b(int):the second integer(default is 98)
    """
