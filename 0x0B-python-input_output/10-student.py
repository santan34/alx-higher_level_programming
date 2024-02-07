#!/usr/bin/python3
"""
Student to json
"""


class Student:
    """
    A class for students
    """

    def __init__(self, first_name, last_name, age):
        """Initialisation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        gets a dict of the class
        :return: the dict
        """
        if attrs is None:
            return self.__dict__
        dicti = {}
        for attr in attrs:
            if hasattr(self, attr):
                dicti[attr] = getattr(self, attr)
        return dicti
