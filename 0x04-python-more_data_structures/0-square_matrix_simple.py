#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    new_matrix = [list(map(lambda x: x ** 2, my_list))
                  for my_list in new_matrix]
    return new_matrix
