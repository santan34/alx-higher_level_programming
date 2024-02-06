#!/usr/bin/python3
"""
Append  o file
"""


def append_write(filename="", text=""):
    """
    Appends to a file
    :param filename: the file to append to
    :param text: trhe text to append
    :return: nukber of characters added
    """
    with open(filename, mode="a", encoding="UTF*") as file:
        file.write(text)
        return len(text)
