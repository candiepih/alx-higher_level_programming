#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as exception:
        print("Exception: {}".format(exception), file=stderr)
        return None
