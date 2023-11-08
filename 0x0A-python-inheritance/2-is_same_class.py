#!/usr/bin/python3

"""check if an object is instance of a given class"""


def is_same_class(obj, a_class):
    """check if an object is instance of a given class
    return true if yes and false otherwise"""
    if a_class == object:
        return False
    return isinstance(obj, a_class)
