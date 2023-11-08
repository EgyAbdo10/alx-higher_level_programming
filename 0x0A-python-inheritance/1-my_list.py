#!/usr/bin/python3

"""look up object attributes"""


class MyList(list):
    """this class inherits from list"""
    def print_sorted(self):
        """print a list sorted without affecting the list"""
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
