#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as exception:
        print("Exception: {}".format(exception), file=stderr)
        return False
