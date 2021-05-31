#!/usr/bin/python3
"""Contains `MyClass` class"""


class MyList(list):
    """Class that extends the list base class"""
    def __init__(self):
        """Initialize inherited data"""
        self.__init__()

    def print_sorted(self):
        """
            Prints a sorted list
        """
        print(sorted(self))
