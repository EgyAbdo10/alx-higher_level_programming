# !/usr/bin/python3

"""define a geometry class"""


class BaseGeometry:
    """an empty class BaseGeometry"""
    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate an integer and its value"""
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
