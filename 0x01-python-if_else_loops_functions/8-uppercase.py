#!/usr/bin/python3
def uppercase(str):
    newtext = ""
    for c in str:
        if ord(c) in range(97, 123):
            newtext += chr(65 + (ord(c) - 97))
        else:
            newtext += c
    print("{}".format(newtext))
