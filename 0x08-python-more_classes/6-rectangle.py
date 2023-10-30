#!/usr/bin/python3
"""
this module is for creating the rectangle class
"""


class Rectangle:
    """
    this is a class for creating rectangle objects
    """
#     Public class attribute number_of_instances:
# Initialized to 0
# Incremented during each new instance instantiation
# Decremented during each instance deletion
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.area() == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        if self.area() == 0:
            return ""
        else:
            rec = ""
            for i in range(self.height):
                rec += ("#" * self.width)
                if i != self.height - 1:
                    rec += "\n"
            return rec

    def __repr__(self):
        string = f"Rectangle({self.width}, {self.height})"
        return string

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
