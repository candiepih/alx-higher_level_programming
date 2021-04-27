#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
            print("{:c}".format(65 + (ord(c) - 97)), end="")
        else:
            print("{}".format(c), end="")
    print()
