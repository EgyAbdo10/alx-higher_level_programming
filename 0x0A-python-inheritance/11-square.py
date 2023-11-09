#!/usr/bin/python3

"""define a square based on the rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """create a square based on a rectangle class"""
    def __init__(self, size):
        """initialze a square based on its size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
