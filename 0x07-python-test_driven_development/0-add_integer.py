#!/usr/bin/python3
"""
    Defines a function that calculates addition
    of two integers
"""


def add_integer(a, b=98):
    """Calculates sum of two integers"""

    if not isinstance(a, (int, float)) or a is NaN:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b is NaN:
        raise TypeError("b must be an integer")

    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return (a + b)
