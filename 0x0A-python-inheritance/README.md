# Python - Inheritance

Aim of this topic was to understand:-

* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

The following task files helped understand the various concepts:-

[0-lookup.py](../0x0A-python-inheritance/0-lookup.py)

Function that returns the list of available attributes and methods of an object

[1-my_list.py](../0x0A-python-inheritance/1-my_list.py)

Class `MyList` that inherits from `list`

* Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)

[2-is_same_class.py](../0x0A-python-inheritance/2-is_same_class.py)

Function that returns `True` if the object is exactly an instance of the specified class; otherwise `False`.

[3-is_kind_of_class.py](../0x0A-python-inheritance/3-is_kind_of_class.py)

Function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.

[4-inherits_from.py](../0x0A-python-inheritance/4-inherits_from.py)

Function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.

[5-base_geometry.py](../0x0A-python-inheritance/5-base_geometry.py)

Defines an empty class `BaseGeometry`.

[6-base_geometry.py](../0x0A-python-inheritance/6-base_geometry.py)

class `BaseGeometry` (based on [5-base_geometry.py](../0x0A-python-inheritance/5-base_geometry.py)).

* Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`

[7-base_geometry.py](../0x0A-python-inheritance/7-base_geometry.py)

class `BaseGeometry` (based on [6-base_geometry.py](../0x0A-python-inheritance/6-base_geometry.py)).

* Public instance method: `def integer_validator(self, name, value):` that validates `value`
* if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
* if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`

[8-rectangle.py](../0x0A-python-inheritance/8-rectangle.py)

class Rectangle that inherits from `BaseGeometry` ([7-base_geometry.py](../0x0A-python-inheritance/7-base_geometry.py)).

* Instantiation with `width` and `height`: `def __init__(self, width, height):`
* `width` and `height` must be private. No getter or setter
* `width` and `height` must be positive integers, validated by `integer_validator`

[9-rectangle.py](../0x0A-python-inheritance/9-rectangle.py)

class Rectangle that inherits from `BaseGeometry` ([7-base_geometry.py](../0x0A-python-inheritance/7-base_geometry.py). ([8-rectangle.py](../0x0A-python-inheritance/8-rectangle.py))
