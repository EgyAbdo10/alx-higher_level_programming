#!/usr/bin/python3

"""define a class MyInt to revers the class Int"""


class MyInt(int):
    """revers the class int eq and ne dunder method"""
    def __eq__(self, value):
        """reverse the equal operator"""
        return super().__ne__(value)

    def __ne__(self, value):
        """reverse the not equal operator"""
        return super().__eq__(value)
