#!/usr/bin/python3
"""Contains `MyClass` class"""


class MyList(list):
    """Class that extends the list base class"""
    def print_sorted(self):
        """
            Prints a sorted list
        """
        new_list = self[:]
        new_list.sort()
        print(new_list)
