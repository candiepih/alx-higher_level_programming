#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        result = 0
    finally:
        new_result = None if result == 0 else result
        print("Inside result: {}".format(new_result))
    return new_result
