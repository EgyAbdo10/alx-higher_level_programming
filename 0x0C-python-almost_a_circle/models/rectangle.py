#!/usr/bin/python3

"""
this module has the rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """rectangle class creates instances of rectangles
    with specific characteristics"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """define the rec instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width of the shape"""
        return self.__width

    @width.setter
    def width(self, new_width):
        """set the width of the shape"""
        if type(new_width) != int:
            raise TypeError("width must be an integer")
        elif new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    @property
    def height(self):
        """get the height of the shape"""
        return self.__height

    @height.setter
    def height(self, new_height):
        """set the height of the shape"""
        if type(new_height) != int:
            raise TypeError("height must be an integer")
        elif new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    @property
    def x(self):
        """get the x coor of the shape"""
        return self.__x

    @x.setter
    def x(self, new_x):
        """set the x coor of the shape"""
        if type(new_x) != int:
            raise TypeError("x must be an integer")
        elif new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @property
    def y(self):
        """set the y coor of the shape"""
        return self.__y

    @y.setter
    def y(self, new_y):
        """set the y coor of the shape"""
        if type(new_y) != int:
            raise TypeError("y must be an integer")
        elif new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        """get the area of teh shape"""
        return (self.width * self.height)

    def display(self):
        """display the shape in terms of #"""
        i = 0
        while (i < self.y):
            print()
            i += 1
        for x in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """arguments are in the following order
        id, width, height, x, y"""
        my_args = ["id", "width", "height", "x", "y"]
        if len(args) != 0:
            for i in range(len(args)): 
                setattr(self, my_args[i], args[i])
        else:
            for item in kwargs.items():
                if (hasattr(self, item[0])) == False:
                    raise AttributeError(f"""{self.__class__.__name__}"""
                               f""" object has n attribute {item[0]}""")
                setattr(self, item[0], item[1])
    
    def to_dictionary(self):
        """turn the shape into a dict of attrs"""
        return {"id" : self.id, "width" : self.width,
                "height" : self.height, "x" : self.x, "y" : self.y}

    def __str__(self):
        """get the str repr of the shape which reoresent all the attrs"""
        return (f"""[Rectangle] ({self.id}) {self.x}/{self.y}"""
        f""" - {self.width}/{self.height}""")