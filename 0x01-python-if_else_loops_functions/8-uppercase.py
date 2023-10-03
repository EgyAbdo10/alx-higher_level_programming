#!/usr/bin/python3
def uppercase(str):
    """print strign in uppercase"""
    for c in str:
        i = ord(c)
        if (i >= 97 and i <= 122):
            i = ord(c) - 32
        else:
            pass
        print("{}".format(chr(i)), end="")
    print("\n")
