# Python - More Classes and Objects
Topic's aim was to understand more about classes and also understand the following concepts:-

* What is OOP
* What “first-class everything” means
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is self
* What is a method
* What is the special __init__ method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* What are the special __str__ and __repr__ methods and how to use them
* What is the difference between __str__ and __repr__
* What is a class attribute
* What is the difference between a object attribute and a class attribute
* What is a class method
* What is a static method
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain __dict__ of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the getattr function

The below task files were used to test my understanding on various concept on the topic.

The following files are used to create a single class based on the following attributes and methods:-

    Contains class `Rectangle` with:-

    Private instance attribute: `width`
    property setter `def width(self, value):` to set it

    Private instance attribute: `height`
    property setter `def height(self, value):` to set it

    Public instance method: `def area(self):` that returns the rectangle area
    Public instance method: `def perimeter(self):` that returns the rectangle perimeter

    `print()` and `str()` should print the rectangle with the character `#`
    `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`

    Public class attribute `number_of_instances`
    Public class attribute `print_symbol`

    Static method `def bigger_or_equal(rect_1, rect_2):`  that returns the biggest rectangle based on the area
    Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`

    and instantiation as `def __init__(self, width=0, height=0):`

# Files

[0-rectangle.py](../0x08-python-more_classes/0-rectangle.py)

Creates an empty class Rectangle that defines a rectangle:

[1-rectangle.py](../0x08-python-more_classes/1-rectangle.py)

adds the following based on [0-rectangle.py](../0x08-python-more_classes/0-rectangle.py)

width:

* Private instance attribute: `width`:
* property `def width(self):` to retrieve it
* property setter `def width(self, value):` to set it:

height:

* Private instance attribute: `height`:
* property `def height(self):` to retrieve it
* property setter `def height(self, value):` to set it:

[2-rectangle.py](../0x08-python-more_classes/2-rectangle.py)

adds the following based on [1-rectangle.py](../0x08-python-more_classes/1-rectangle.py)

* Public instance method: `def area(self):` that returns the rectangle area
* Public instance method: `def perimeter(self):` that returns the rectangle perimeter

[3-rectangle.py](../0x08-python-more_classes/3-rectangle.py)

adds the following based on [2-rectangle.py](../0x08-python-more_classes/2-rectangle.py)

* `print()` and `str()` should print the rectangle with the character `#`

[4-rectangle.py](../0x08-python-more_classes/4-rectangle.py)

adds the following based on [3-rectangle.py](../0x08-python-more_classes/3-rectangle.py)

* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`

[5-rectangle.py](../0x08-python-more_classes/5-rectangle.py)

adds the following based on [4-rectangle.py](../0x08-python-more_classes/4-rectangle.py)

* Print the message Bye `rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted

[6-rectangle.py](../0x08-python-more_classes/6-rectangle.py)

adds the following based on [5-rectangle.py](../0x08-python-more_classes/5-rectangle.py)

* Public class attribute `number_of_instances` used to count instances, decrements on deletion and increments on addition

[7-rectangle.py](../0x08-python-more_classes/7-rectangle.py)

adds the following based on [6-rectangle.py](../0x08-python-more_classes/6-rectangle.py)

* Public class attribute `print_symbol` that changes `#` to print something else instead


[8-rectangle.py](../0x08-python-more_classes/8-rectangle.py)

adds the following based on [7-rectangle.py](../0x08-python-more_classes/7-rectangle.py)

Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area

[9-rectangle.py](../0x08-python-more_classes/9-rectangle.py)

adds the following based on [8-rectangle.py](../0x08-python-more_classes/8-rectangle.py)

Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`
