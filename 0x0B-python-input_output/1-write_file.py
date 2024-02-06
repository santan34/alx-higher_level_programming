#!/usr/bin/python3
"""
Write to file
"""


def write_file(filename="", text=""):
    """writes to a file"""
    with open(filename, mode="w", encoding="UTF*") as file:
        file.write(text)
        return len(text)
