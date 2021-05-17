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

A function that prints x elements of a list.

[1-safe_print_integer.py](../0x05-python-exceptions/1-safe_print_integer.py)

Prototype: `def safe_print_integer(value):`

A function that prints an integer with `"{:d}".format()`. Returns `True` if value has been correctly printed (it means the value is an integer)
Otherwise, returns `False`

[2-safe_print_list_integers.py](../0x05-python-exceptions/2-safe_print_list_integers.py)

Prototype: `def safe_print_list_integers(my_list=[], x=0):`

A function that prints the first `x` elements of a list and only integers. `x` represents the number of elements to access in `my_list`, `x` can be bigger than the length of `my_list`, if it’s the case, an exception will occur. Returns the real number of integers printed.

[3-safe_print_division.py](../0x05-python-exceptions/3-safe_print_division.py)

Prototype: `def safe_print_division(a, b):`

A function that divides 2 integers and prints the result. Assuming `a` and `b` are integers the result of the division is printed on the `finally:` section preceded by Inside `result:`. Returns the value of the division, otherwise: `None`

[4-list_division.py](../0x05-python-exceptions/4-list_division.py)

Prototype: `def list_division(my_list_1, my_list_2, list_length):`

A function that divides element by element 2 lists. `my_list_1` and `my_list_2` can contain any type (integer, string, etc). `list_length` can be bigger than the length of both lists. Returns a new list (length = `list_length`) with all divisions otherwise if division fails the value is replaced by `0`.

[5-raise_exception.py](../0x05-python-exceptions/5-raise_exception.py)

Prototype: `def raise_exception():`

A function that raises a type exception.

[6-raise_exception_msg.py](../0x05-python-exceptions/6-raise_exception_msg.py)

Prototype: `def raise_exception_msg(message=""):`

A function that raises a name exception with a message.

[100-safe_print_integer_err.py](../0x05-python-exceptions/100-safe_print_integer_err.py)

Prototype: `def safe_print_integer_err(value):`

A function that prints an integer. `value` can be any type (integer, string, etc). Returns `True` if value has been correctly printed (it means the value is an integer)
Otherwise, returns `False` and prints in `stderr` the error precede by `Exception: `

[101-safe_function.py](../0x05-python-exceptions/101-safe_function.py)

Prototype: `def safe_function(fct, *args):`

Assuming fct will be always a pointer to a function returns the result of the function, otherwise, returns `None` if something happens during the function and prints in `stderr` the error precede by `Exception: `
