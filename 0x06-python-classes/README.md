# Python - Classes and Objects
This topic's aim was to understand object oriented programming in python. I understood various concepts which are:-

* What OOP is
* What “first-class everything” means
* What a class is
* What's an object and an instance
* Difference between a class and an object or instance
* What an attribute is
* What are and how to use public, protected and private attributes
* What's `self`
* What's a method
* Special `__init__` method and how to use it
* Data Abstraction, Data Encapsulation, and Information Hiding
* What a property is
* Difference between an attribute and a property in Python
* Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What's the `__dict__` of a class and/or instance of a class and what does it contain
* How Python find the attributes of an object or class
* How to use the `getattr` function

After grasping concepts the following task files were used the test my understanding on object oriented programming.
# Files
[0-square.py](../0x06-python-classes/0-square.py)

Creation of an empty class `Square` that defines a square

[1-square.py](../0x06-python-classes/1-square.py)

Class `Square` that defines a square by: based on [0-square.py](../0x06-python-classes/0-square.py)
* Private instance attribute: `size`
* Instantiation with `size` (no type/value verification)

[2-square.py](../0x06-python-classes/2-square.py)

Class `Square` that defines a square by: based on [1-square.py](../0x06-python-classes/1-square.py)
* Private instance attribute: `size`
* Instantiation with optional size: `def __init__(self, size=0):`


          * `size` must be an integer, otherwise raises a `TypeError` exception with the message `size must be an integer`
          * if `size` is less than `0`, raises a `ValueError` exception with the message `size must be >= 0`

[3-square.py](../0x06-python-classes/3-square.py)

Class `Square` that defines a square by: based on [2-square.py](../0x06-python-classes/2-square.py)

* Public instance method: `def area(self):` that returns the current square area

[4-square.py](../0x06-python-classes/4-square.py)

Class `Square` that defines a square by: based on [3-square.py](../0x06-python-classes/3-square.py)
* Instantiation with optional `size: def __init__(self, size=0):`

[5-square.py](../0x06-python-classes/5-square.py)

Class `Square` that defines a square by: based on [4-square.py](../0x06-python-classes/4-square.py)
* Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
* if `size` is equal to 0, print an empty line

[6-square.py](../0x06-python-classes/6-square.py)

Class `Square` that defines a square by: based on [5-square.py](../0x06-python-classes/5-square.py)
* Private instance attribute: `position:`

       * property `def position(self):` to retrieve it
       * property setter `def position(self, value):` to set it:
       * `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError`
          exception with the message `position must be a tuple of 2 positive integers`

* Instantiation with optional size and optional `position: def __init__(self, size=0, position=(0, 0)):`
* Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:

         * if size is equal to 0, print an empty line
         * `position` should be use by using space - `Don’t fill lines by spaces` when `position[1] > 0`

[100-singly_linked_list.py](../0x06-python-classes/100-singly_linked_list.py)

Class `Node` that defines a node of a singly linked list by:
* Private instance attribute: `data`:

         * property `def data(self):` to retrieve it
         * property setter `def data(self, value):` to set it:
         * `data` must be an integer, otherwise raise a `TypeError` exception with the message `data must be an integer`

* Private instance attribute: `next_node`:

         * property `def next_node(self):` to retrieve it
         * property setter `def next_node(self, value):` to set it:
         * `next_node` can be None or must be a Node, otherwise raise a `TypeError` exception with the message
           `next_node must be a Node object`

* Instantiation with data and next_node: `def __init__(self, data, next_node=None):`


Class `SinglyLinkedList` that defines a singly linked list by:
* Private instance attribute: `head` (no setter or getter)
* Simple instantiation: `def __init__(self):`
* Should be printable:

      * print the entire list in stdout
      * one node number by line

* Public instance method: `def sorted_insert(self, value):` that inserts a new `Node` into the correct sorted position in the list (increasing order)

[101-square.py](../0x06-python-classes/101-square.py)

Class `Square` that defines a square by: based on [6-square.py](../0x06-python-classes/6-square.py)
* Printing a `Square` instance should have the same behavior as `my_print()` method


[102-square.py](../0x06-python-classes/102-square.py)

Class `Square` that defines a square by: based on [4-square.py](../0x06-python-classes/4-square.py)
* `Square` instance can answer to comparators: `==, !=, >, >=, <` and `<=` based on the square area
