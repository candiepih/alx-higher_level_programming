#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul_by_2 = lambda x: x * 2
    new_dict = {k: mul_by_2(v) for k, v in a_dictionary.items()}
    return new_dict
