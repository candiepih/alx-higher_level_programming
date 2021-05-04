#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = 0 if len(tuple_a) == 0 else tuple_a[0]
    a2 = 0 if len(tuple_a) <= 1 else tuple_a[1]
    b1 = 0 if len(tuple_b) == 0 else tuple_b[0]
    b2 = 0 if len(tuple_b) <= 1 else tuple_b[1]
    sum1 = a1 + b1
    sum2 = a2 + b2
    summation = (sum1, sum2)
    return summation
