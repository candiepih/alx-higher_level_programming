#!/usr/bin/python3
"""Module contains only a lookup function"""

def lookup(obj):
    """
       Returns list of available objets and methods
       in an object
    """
    return dir(obj)
