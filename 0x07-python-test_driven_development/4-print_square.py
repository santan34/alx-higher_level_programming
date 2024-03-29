#!/usr/bin/python3
"""
prints a square of #'s
"""


def print_square(size):
    """
    prints a square of #'s
    Args:
        size(int): the dimension of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#"*size)
