#!/usr/bin/python3
def no_c(my_string):
    s = list(my_string)
    for i, char in enumerate(s):
        if (char == "c" or char == "C"):
            s.pop(i)
    s = "".join(s)
    return s
