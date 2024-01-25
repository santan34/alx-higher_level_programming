#!/usr/bin/python3
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
    def area(self):
        return self.__size * self.__size
        """
        Calculates the area of a sqaure object
        Returns:
            The area of the square object
        """
