#!/usr/bin/python3
mul_by_2 = lambda x: x * 2
def multiply_by_2(a_dictionary):
    new_dict = {k: mul_by_2(v) for k, v in a_dictionary.items()}
    return new_dict
    
