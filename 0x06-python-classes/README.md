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
* Private instance attribute: `size`
* Instantiation with optional size: `def __init__(self, size=0):`
          
          * `size` must be an integer, otherwise raises a `TypeError` exception with the message `size must be an integer`
          * if `size` is less than `0`, raises a `ValueError` exception with the message `size must be >= 0`

* Public instance method: `def area(self):` that returns the current square area
