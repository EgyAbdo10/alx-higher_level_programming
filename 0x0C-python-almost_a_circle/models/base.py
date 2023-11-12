#!/usr/bin/python3
"""this the base class module where the base class is defined"""


class Base:
    """This class will be the “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """create public instanece attr id
        and assign it to a value"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

if __name__ == "__main__":
    a1 = Base(20)
    print(a1.id)