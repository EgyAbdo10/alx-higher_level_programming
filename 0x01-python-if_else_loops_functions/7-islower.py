#!/usr/bin/python3
def islower(c):
    if (ord(c) >= 97 and ord(c) <= 122):
        return True
    elif (ord(c) < 97 or ord(c) > 122) :
        return False
print(islower("a"))
