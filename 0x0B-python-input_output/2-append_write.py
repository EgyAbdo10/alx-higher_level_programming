#!/usr/bin/python3

"""this module has a function that append text to files"""


def append_write(filename="", text=""):
    """append text to files"""
    with open(filename, mode="a", encoding="UTF8") as file:
        return file.write(text)
