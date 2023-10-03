#!/usr/bin/python3
def uppercase(str):
    """print a string in uppercase"""
    for c in str:
        i = ord(c)
        if (i >= 97 and i <= 122):
            i = ord(c) - 32
        print("{}".format(chr(i)), end="")
    print("{}".format("\n"), end="")
