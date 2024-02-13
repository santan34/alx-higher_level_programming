"""
the first rectangle
"""
Base = __import__('base').Base


class Rectangle(Base):
    """
    A class to store rectangles
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instanceate the class"""
        super().__init__(id)
        self.validate_all(width, height, x, y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def validate(self, val, name):
        """
        Validate a particular setter
        :param val: the value
        :param name: the setter
        """
        if type(val) is not int:
            raise TypeError(f"{name} must be an integer")
        if (name == "width") or (name == "height"):
            if val <= 0:
                raise ValueError(f"{name} must be > 0")
        if (name == "x") or (name == "y"):
            if val < 0:
                raise ValueError(f"{name} must be >= 0")

    def validate_all(self, width, height, x, y):
        """
        Validate upon instanciation
        :param width: the witdh
        :param height: the height
        :param x: the x coordinates
        :param y: the y coordinates
        """
        self.validate(width, "width")
        self.validate(height, "height")
        self.validate(x, "x")
        self.validate(y, "y")

    @property
    def width(self):
        """
        Getter for width
        :return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        :param value: the value to set
        """
        self.validate(value, "width")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        :return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height
        :param value: th value to set
        """
        self.validate(value, "height")
        self.__height = value

    @property
    def x(self):
        """
        getter for x
        :return: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for x
        :param value: the value to set
        :return:
        """
        self.validate(value, "x")
        self.__x = value

    @property
    def y(self):
        """
        getter for y
        :return: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for y
        :param value: teh value
        :return:
        """
        self.validate(value, "y")
        self.__y = value

    def area(self):
        """
        area of a class
        :return: 
        """
        return self.__width * self.__height

    def display(self):
        """
        print square
        :return: 
        """
        lnth = self.__height
        wid = self.__width
        for i in range(lnth):
            print("#" * wid)

    def __str__(self):
        """
        __str__ 
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
