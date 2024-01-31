#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """
    A class called Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Instancete tha class
        both parameters should be integers
        :param width(optional): the width of the rectangle
        :param height(optional): the length of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        Getter for the class
        :return: the private width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        the setter for witdh
        :param value(int): the integer to set as width
        :return: Nothing
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Sets the height of the rectangle
        :return: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        The setter for the height variable
        :param value(int): the value to use as the height
        :return: Nothing
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        :return: the area of the rectangle
        """
        if (self.__height == 0) or (self.__width == 0):
            return 0
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        :return: the perimeter
        """
        if (self.__height == 0) or (self.__width == 0):
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        string streingj
        :return:
        """
        if (self.__height == 0) or (self.__width == 0):
            return ""
        return '\n'.join("#" * self.__width for x in range(self.__height))

    def __repr__(self):
        """modifies repr object

        """
        return "Rectangle({}, {})".format(self.width, self.height)
