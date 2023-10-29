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

    def area(self):
        """
        this function calculates the area of a square
        """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        if type(new_size) != int:
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = new_size
