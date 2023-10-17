#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 0:
        print("{} arguments.".format(0))
    elif len(sys.argv) == 1:
        print("{} argument:".format(1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{}: arguments".format(len(sys.argv)))
        for i, v in enumerate(sys.argv):
            print("{}: {}".format(i, v))
