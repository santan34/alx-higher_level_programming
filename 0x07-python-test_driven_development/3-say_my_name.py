#!/usr/bin/python3
"""
prints out the full name of the person
"""


def say_my_name(first_name, last_name=""):
    """
    a function that prints out the first and last name of a person
    the function only takes strings as input
    Args:
        first_name(str): the first name
        last_name(str): the last name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
