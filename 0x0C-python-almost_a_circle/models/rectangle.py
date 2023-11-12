#!/usr/bin/python3
"""this module has the rectangle class"""


from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if type(new_width) != int:
            raise TypeError("width must be an integer")
        elif new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if type(new_height) != int:
            raise TypeError("height must be an integer")
        elif new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        if type(new_x) != int:
            raise TypeError("x must be an integer")
        elif new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        if type(new_y) != int:
            raise TypeError("y must be an integer")
        elif new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        return (self.width * self.height)

    def display(self):
        i = 0
        while (i < self.y):
            print()
            i += 1
        for x in range(self.height):
            print(" " * self.width, end="")
            print("#" * self.width)

    def update(self, *args):
        my_args = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, my_args[i], args[i])

    def __str__(self):
        # [Rectangle] (<id>) <x>/<y> - <width>/<height>
        return (f"""[Rectangle] ({self.id}) {self.x}/{self.y}"""
        f""" - {self.width}/{self.height}""")