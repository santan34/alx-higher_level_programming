#!/usr/bin/python3
class Square:
    """
    class to hold squares
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        """
        initilisation of the class
        Args:
            size(int): size of the square
            size must be posistive and integer type
        """
