#!/usr/bin/python3
"""Contains a class `Base`"""


class Base:
    """
        Defines the class `Base`

        Attributes:
            id (int): instance attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initializes class and object data

            Args:
                id (int): integer passed on object creation
        """
        self.id = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
