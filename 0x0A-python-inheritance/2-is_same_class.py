#!/usr/bin/python3

"""check if an object is instance of a given class"""


def is_same_class(obj, a_class):
    """check if an object is instance of a given class
    return true if yes and false otherwise"""
    if type(obj) == a_class:
        return True
    return False
