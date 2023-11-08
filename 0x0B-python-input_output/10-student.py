#!/usr/bin/python3

"""json representation of objects"""


class Student:
    """create a student base on first, last name and age"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get a dict from object attributes"""
        if attrs == None:
            return self.__dict__
        else:
            attr_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    attr_dict[attr] = getattr(self, attr)
            return attr_dict
