#!/usr/bin/python3

"""this module has a function that write text into files"""


def write_file(filename="", text=""):
    """write text into files"""
    with open(filename, mode="w", encoding="UTF8") as file:
        return file.write(text)
