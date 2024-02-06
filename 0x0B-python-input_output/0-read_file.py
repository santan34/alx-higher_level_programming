#!/usr/bin/python3
"""
0.Read file
"""

def read_file(filename=""):
    """
    Read from a file
    :param filename: the file to read
    """
    with open(filename, mode="r", encoding="UTF8") as file:
        for line in file:
            print(line, end="")
