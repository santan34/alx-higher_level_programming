#!/usr/bin/python3
"""
Prints text with two lines after each ., ? and :
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i in [".", "?", ":"]:
            print(f"{i}", end="")
            print()
            print()
        else:
            print(f"{i}", end="")
    """
    prints out the given string adding two lines when we get to "." or "?" and ":"
    Args:
        text(str): the string to be printed out
    """
