#!/usr/bin/python3
"""
The base class
"""


class Base:
    """
    the base class for whatever we are going to be doing
    """

    _nb_objects = 0

    def __init__(self, id=None):
        """
        Instanciate the class
        :param id: the id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_dictionary(self):
        """dictionary"""
        dic = {'id': self.id, 'size': self.size,
               'x': self.x, 'y': self.y}
        return dic  # !/usr/bin/python3


"""
The base class
"""


class Base:
    """
    the base class for whatever we are going to be doing
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instanciate the class
        :param id: the id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_dictionary(self):
        """dictionary"""
        dic = {'id': self.id, 'size': self.size,
               'x': self.x, 'y': self.y}
        return dic
