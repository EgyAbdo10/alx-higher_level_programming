#!/usr/bin/python3

"""define a rectangle class"""


class Rectangle(BaseGeometry):
    """create a rectangle with width and height"""
    def __init__(self, width, height):
        """initialize a rectangle object"""
        BaseGeometry.integer_validator("width", width)
        BaseGeometry.integer_validator("height", height)
        self.__width = width
        self.__height = height
