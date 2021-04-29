#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    pass

argc = len(argv)
if argc == 1:
    print("0 arguments.")
else:
    print("{} {}:".format((argc - 1),
                          ("argument" if argc == 2 else "arguments")))
    for i, arg in enumerate(argv):
        if i == 0:
            continue
        print("{}: {}".format((i), arg))
