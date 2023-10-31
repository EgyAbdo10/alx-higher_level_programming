#!/usr/bin/python3
def magic_string():
    magic_string.nth = getattr(magic_string, "nth", 0) + 1
    return ("BestSchool, " * (magic_string.nth - 1) + "BestSchool")
