#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        val = 0
        try:
            val = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            val = 0
        except TypeError:
            print("wrong type")
            val = 0
        except ZeroDivisionError:
            print("division by 0")
            val = 0
        finally:
            new_list.append(val)
    return new_list
