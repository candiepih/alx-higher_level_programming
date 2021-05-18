#!/usr/bin/python3
"""Defination classes of singly linked list"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes node data
        Args:
            data (int): value to be assigned to `data`
            next_node (Node): object of type Node
        Raises:
	    TypeError: `data` isn't an integer or `next_node` not a
	                node object
        """
        if not isinstance(data, int):
	    raise TypeError("data must be an integer")
        if not isinstance(next_node, Node) and next_node != None:
	    raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """retrieves value of data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets a new value to `data` attribute
        Args:
            value (int): number to assign to `data`
        Raises:
            TypeError: if data isn't an integer
	"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
	self.__data = value

    @property
    def next_node(self):
        """retrieves value of `next_node`"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
	"""Sets a new value to `next_node`
        Args:
            value (Node): object of Noden to assign to `next_node`
        Raises:
            TypeError: if value is not a Node object
	"""
        if not isinstance(value, Node) and value != None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        head = self.__head
        values = []
        while head != None:
            values.append("{}".format(head.data))
            head = head.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        head = self.__head
        if head == None or (head != None and head.data >= value):
            new_node = Node(value, head)
            self.__head = new_node
            return
        while head != None:
            next_node = head.next_node
            if next_node == None or next_node.data >= value:
                new_node = Node(value, next_node)
                head.next_node = new_node
                break
            head = next_node
