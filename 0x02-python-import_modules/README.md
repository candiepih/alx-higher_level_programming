# Python - import & modules
Simply, a `module` is a file consisting of Python code. A module can define functions, classes and variables. We can import the definitions inside a module to another module by using the `import` command. For better concepts grasping, the following task files were used:-
## [0-add.py](../0x02-python-import_modules/0-add.py)
Program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3` with `1` and `2` stored in variables `a` and `b`. Content of import file:-
```python
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

```
## [1-calculation.py](../0x02-python-import_modules/1-calculation.py)
Program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result. Content of file being imported:-
```python

def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)
 
```
## [2-args.py](../0x02-python-import_modules/2-args.py)
Program that prints the number and the list of its arguments passed to the program
## [3-infinite_add.py](../0x02-python-import_modules/3-infinite_add.py)
Program that prints the result of the addition of all arguments passed to program assuming that all arguments can be casted into integers
## [4-hidden_discovery.py](../0x02-python-import_modules/4-hidden_discovery.py)
Program that prints all the names defined by the compiled module `hidden_4.pyc`.
## [5-variable_load.py](../0x02-python-import_modules/5-variable_load.py)
Program that imports the variable `a` from the file `variable_load_5.py` and prints its value. Contents of `variable_load_5.py` are:-

```python

a = 98
"""Simple variable
"""

```

## [100-my_calculator.py](../0x02-python-import_modules/100-my_calculator.py)
Program that imports all functions from the file `calculator_1.py` and handles basic operations.
* Usage: `./100-my_calculator.py a operator b`
* You can cast `a` and `b` into integers by using `int()` (assuming that all arguments will be castable into integers)

operator can be:
* + for addition
* - for subtraction
* * for multiplication
* / for division
Contents of file `calculator_1.py` are:-

```python

def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

```
## [101-easy_print.py](../0x02-python-import_modules/101-easy_print.py)
Program that prints `#pythoniscool`, followed by a new line, in the standard output without using `print` or `eval` or `open` or `import sys`
## [103-fast_alphabet.py](../0x02-python-import_modules/103-fast_alphabet.py)
program that prints the alphabet in uppercase, followed by a new line without use of any loops, conditional statements, str.join(), string literal or system calls.
