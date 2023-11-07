#!/usr/bin/python3

"""json representation of objects"""


def class_to_json(obj):
    """get a dict from object attributes"""
    return str(obj.__dict__)
