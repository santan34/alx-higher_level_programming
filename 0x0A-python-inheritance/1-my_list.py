#!/usr/bin/python3
"""
firts inheritance
"""


class MyList(list):
    """
    A class that inherits from list
    """
    def print_sorted(self):
        """
        prinnts a sorted list
        """
        print(sorted(self))
