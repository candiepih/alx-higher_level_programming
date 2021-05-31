#!/usr/bin/ython3
"""Contains a single method"""


def inherits_from(obj, a_class):
    """
        check if object is instance of a class inherited
        from directly or indirectly
    """
    return issubclass(type(obj), a_class) and type(obj) is a_class
