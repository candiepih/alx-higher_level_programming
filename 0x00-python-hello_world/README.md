# Python - Hello, World
Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
Guido van Rossum was a Dutch programmer who created the Python programming language in 1991.
### This topic aim was to understand:-
* Using the Python Interpreter
* How To Use String Formatters in Python 3
* How to print text and variables using print
* What are indexing and slicing in Python
* What is the official Holberton Python coding style and how to check your code with PEP 8
Below task files were used to achieve learning objectives and grasp concepts.
## [0-run](../0x00-python-hello_world/0-run)
Shell script that runs a Python script with the Python file name saved in the environment variable `$PYFILE`
## [1-run_inline](../0x00-python-hello_world/1-run_inline)
Shell script that runs Python code with the Python code saved in the environment variable `$PYCODE`
## [2-print.py](../0x00-python-hello_world/2-print.py)
Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
## [3-print_number.py](../0x00-python-hello_world/3-print_number.py)
You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py). 
The output of the script should be:
* the number, followed by Battery street,
* followed by a new line
* You are not allowed to cast the variable number into a string
* Your code must be 3 lines long
* You have to use the new print numbers tips (with .format(...))

## [4-print_float.py](../0x00-python-hello_world/4-print_float.py)
Completes the [source code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable number with a precision of 2 digits.
## [5-print_string.py](../0x00-python-hello_world/5-print_string.py)
Completes [this](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py) source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
* The output of the program should be:
* 3 times the value of str

    * followed by a new line
    * followed by the 9 first characters of str
    * followed by a new line
* You are not allowed to use any loops or conditional statement
* Your program should be maximum 5 lines long
## [6-concat.py](../0x00-python-hello_world/6-concat.py)
Completes [this](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py) source code to print `Welcome to Holberton School!`
* You are not allowed to use any loops or conditional statements.
* You have to use the variables `str1` and `str2` in your new line of code
* Your program should be exactly 5 lines long
## [7-edges.py](../0x00-python-hello_world/7-edges.py)
Completes [this](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py) source code
* You are not allowed to use any loops or conditional statements
* Your program should be exactly 8 lines long
* `word_first_3` should contain the first 3 letters of the variable word
* `word_last_2` should contain the last 2 letters of the variable word
* `middle_word` should contain the value of the variable word without the first and last letters
## [8-concat_edges.py](../0x00-python-hello_world/8-concat_edges.py)
Complete [this](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) source code to print object-oriented programming with Python, followed by a new line.
* You are not allowed to use any loops or conditional statements
* Your program should be exactly 5 lines long
* You are not allowed to create new variables
* You are not allowed to use string literals
## [9-easter_egg.py](../0x00-python-hello_world/9-easter_egg.py)
Python script that prints `“The Zen of Python”`, by TimPeters, followed by a new line.
```

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

```
## [10-check_cycle.c](../0x00-python-hello_world/10-check_cycle.c)
Function in C that checks if a singly linked list has a cycle in it.
* Prototype: int check_cycle(listint_t *list);
* Returns: `0` if there is no cycle, `1` if there is a cycle

Using floyd's cycle finding algorithm here is a sketch of how I implemented it. 
![sketch](https://user-images.githubusercontent.com/44834632/116272335-7f1e9180-a789-11eb-994b-be1999aefb38.png)


## [lists.h](../0x00-python-hello_world/lists.h)
Contains function prototypes and list data structure
## [100-write.py](../0x00-python-hello_world/100-write.py)
Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.
* Use of `write` from the `sys` module is allowed
* You are not allowed to use `print`
* Your script should print to `stderr`
* Your script should exit with the status code `1`
## [101-compile](../0x00-python-hello_world/101-compile)
Script that compiles a Python script file. The Python file name is stored in the environment variable `$PYFILE` and the output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)
