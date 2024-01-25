#!/usr/bin/python3
"""
working with the square class
"""


class Square:
    """
       a class for square object
       """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """
        Initialises the size instance of square
        Args:
            size(int): size of the square
            size must be greater than 0
        """

    @property
    def size(self):
        return self.__size
    """
    Gets the value of a private instance
    Returns:
        the size of the square
        """
    @property
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        """
        sets the value of size
        Args:
            value(int): the value to set size to
        """
    def area(self):
        return self.__size * self.__size
        """
        Calculates the area of a sqaure object
        Returns:
            The area of the square object
        """
