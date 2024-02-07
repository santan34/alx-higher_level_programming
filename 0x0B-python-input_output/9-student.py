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

    def to_json(self):
        """
        gets a dict of the class
        :return: the dict
        """
        return self.__dict__
