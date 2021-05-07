#!/usr/bin/python3
def weight_average(my_list=[]):
    div1 = 0
    divisor = 0
    if not my_list:
        return 0
    for tupp in my_list:
        div1 += tupp[0] * tupp[1]
        divisor += tupp[1]
    return (div1/divisor)
