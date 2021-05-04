#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    for i, num in enumerate(my_list):
        if ((i + 1) < len(my_list)):
            num2 = my_list[i + 1]
            if num > num2:
                my_list[i], my_list[i + 1] = num2, num
    return my_list[-1]
