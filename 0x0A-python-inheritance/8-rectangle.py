#!/usr/bin/python3

"""define a Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """create a rectangle with width and height"""
    def __init__(self, width, height):
        """initialize a rectangle object"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
