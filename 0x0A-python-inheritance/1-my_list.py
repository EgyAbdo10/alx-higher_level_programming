#!/usr/bin/python3

"""look up object attributes"""


class MyList(list):
    """this class inherits from list"""
    def print_sorted(self):
        """print a list sorted without affecting the list"""
        print(sorted(self))
