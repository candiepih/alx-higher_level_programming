#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = []

nb_print = safe_print_list(my_list, -11)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
