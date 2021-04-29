#!/usr/bin/python3
import sys.argv as argv

if __name__ == "__main__":
    pass

argc = len(argv)
if argc == 1:
    print("0 arguments.")
else:
    print("{} argument:".format(argc - 1))
    for i, arg in enumerate(argv):
        if i == 0:
            continue
        print("{}: {}".format((i), arg))
