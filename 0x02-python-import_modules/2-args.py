#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("{} arguments.".format(0))
    elif len(sys.argv) == 2:
        print("{} argument:".format(1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format((len(sys.argv) - 1)))
        for i, v in enumerate(sys.argv):
            if (i > 0):
                print("{}: {}".format(i, v))
