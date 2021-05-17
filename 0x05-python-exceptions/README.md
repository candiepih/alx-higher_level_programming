# Python - Exceptions
This topic's aim was understanding the following:-

* The difference between errors and exceptions
* What are exceptions and how to use them
* When we need to use exceptions
* How to correctly handle an exception
* Understanding the purpose of catching exceptions
* How to raise a builtin exception
* When is it needed to implement a clean-up action after an exception

I understood that an `Error` indicates serious problems that a reasonable application should not try to catch while an `Exception` indicates conditions that a reasonable application might want to catch. Below task files helped in understanding various concepts of the topic.

# FILES

[0-safe_print_list.py](../0x05-python-exceptions/0-safe_print_list.py)

Prototype: `def safe_print_list(my_list=[], x=0):`

A Function that prints x elements of a list.

[1-safe_print_integer.py](../0x05-python-exceptions/1-safe_print_integer.py)

Prototype: `def safe_print_integer(value):`

A function that prints an integer with `"{:d}".format()`. Returns `True` if value has been correctly printed (it means the value is an integer)
Otherwise, returns `False`

[2-safe_print_list_integers.py](../0x05-python-exceptions/2-safe_print_list_integers.py)

Prototype: `def safe_print_list_integers(my_list=[], x=0):`

A Function that prints the first `x` elements of a list and only integers. `x` represents the number of elements to access in `my_list`, `x` can be bigger than the length of `my_list`, if it’s the case, an exception will occur. Returns the real number of integers printed.
