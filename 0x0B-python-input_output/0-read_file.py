#!/usr/bin/python3

"""this module has a function that reads text files"""


def read_file(filename=""):
    """read text files from the beginning to the end"""
    with open(filename, encoding="UTF8") as file:
        print(file.read(), end="")
