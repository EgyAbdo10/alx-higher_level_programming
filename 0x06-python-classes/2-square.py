#!/usr/bin/python3
"""
this module defines a class square
which is empty
"""


class Square:
    """
    this class is empty and just defines a square
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size