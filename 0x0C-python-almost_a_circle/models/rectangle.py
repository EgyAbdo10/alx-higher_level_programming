#!/usr/bin/python3
from models.base import Base

"""
This module contains the Rectangle class.
"""

class Rectangle(Base):
    """
    Rectangle class creates instances of rectangles
    with specific characteristics.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle.
            y (int): Y-coordinate of the rectangle.
            id (int): Identifier for the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getter method for the width property.
        """
        return self.__width

    @width.setter
    def width(self, new_width):
        """
        Setter method for the width property.

        Args:
            new_width (int): New width value.

        Raises:
            TypeError: If new_width is not an integer.
            ValueError: If new_width is not greater than 0.
        """
        if type(new_width) != int:
            raise TypeError("width must be an integer")
        elif new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    @property
    def height(self):
        """
        Getter method for the height property.
        """
        return self.__height

    @height.setter
    def height(self, new_height):
        """
        Setter method for the height property.

        Args:
            new_height (int): New height value.

        Raises:
            TypeError: If new_height is not an integer.
            ValueError: If new_height is not greater than 0.
        """
        if type(new_height) != int:
            raise TypeError("height must be an integer")
        elif new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    @property
    def x(self):
        """
        Getter method for the x property.
        """
        return self.__x

    @x.setter
    def x(self, new_x):
        """
        Setter method for the x property.

        Args:
            new_x (int): New x value.

        Raises:
            TypeError: If new_x is not an integer.
            ValueError: If new_x is less than 0.
        """
        if type(new_x) != int:
            raise TypeError("x must be an integer")
        elif new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @property
    def y(self):
        """
        Getter method for the y property.
        """
        return self.__y

    @y.setter
    def y(self, new_y):
        """
        Setter method for the y property.

        Args:
            new_y (int): New y value.

        Raises:
            TypeError: If new_y is not an integer.
            ValueError: If new_y is less than 0.
        """
        if type(new_y) != int:
            raise TypeError("y must be an integer")
        elif new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Displays the rectangle using '#' characters.
        """
        i = 0
        while i < self.y:
            print()
            i += 1
        for x in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle.

        Args:
            *args: Variable arguments in the order (id, width, height, x, y).
            **kwargs: Variable keyword arguments.

        Raises:
            AttributeError: If an invalid attribute is provided.
        """
        my_args = ["id", "width", "height", "x", "y"]
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, my_args[i], args[i])
        else:
            for item in kwargs.items():
                if not hasattr(self, item[0]):
                    raise AttributeError(f"{self.__class__.__name__} object has no attribute {item[0]}")
                setattr(self, item[0], item[1])

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle.

        Returns:
            dict: Dictionary representation of the rectangle.
        """
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
