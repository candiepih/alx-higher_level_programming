# Python - import & modules
Simply, a `module` is a file consisting of Python code. A module can define functions, classes and variables. We can import the definitions inside a module to another module by using the `import` command. For better concepts grasping, the following task files were used:-
## [0-add.py](../0x02-python-import_modules/0-add.py)
Program that imports the function def add(a, b): from other file and prints the result of the addition 1 + 2 = 3 with 1 and 2 stored in variables a and b
## [1-calculation.py](../0x02-python-import_modules/1-calculation.py)
Program that imports functions from the file another file, does some Maths, and prints the result. Content of file being imported:-
```python
candiepih@ubuntu:~/0x02$ cat calculator_1.py

#!/usr/bin/python3
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
