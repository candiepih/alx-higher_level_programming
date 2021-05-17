#!?usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    subtract_count = 0;
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            subtract_count += 1
            continue
    print()
    return ((i - subtract_count) + 1)
