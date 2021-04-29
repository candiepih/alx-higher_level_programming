#!/usr/bin/python3
import sys

if __name__ == "__main__":
    pass

argv = sys.argv
argc = len(argv)
if argc == 1:
    print("0 arguments.")
else:
    print("{} argument:".format(argc - 1))
    for i, arg in enumerate(argv):
        if i == 0:
            continue
        print("{}: {}".format((i), arg))
