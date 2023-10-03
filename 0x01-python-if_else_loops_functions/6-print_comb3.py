#!/usr/bin/python3
for i in range(100):
    if (i < (int(i / 10) / 10 + (i % 10) * 10)):
        if (i != 89):
            print("{}{}".format(int(i / 10), (i % 10)), end=", ")
        else:
            print("{}".format(89))
