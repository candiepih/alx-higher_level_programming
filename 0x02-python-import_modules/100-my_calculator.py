#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    pass

argc = len(argv)
if argc != 4:
    print("Usage: {} <a> <operator> <b>".format(argv[0]))
    exit(1)

operators = [
    {
        "sign": "+",
        "func": add
    },
    {
        "sign": "-",
        "func": sub
    },
    {
        "sign": "*",
        "func": mul
    },
    {
        "sign": "/",
        "func": div
    },
]


def get_operator(operator):
    for operation in operators:
        if operation["sign"] == operator:
            return (operation["func"])
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

operator = argv[2]
a = int(argv[1])
b = int(argv[3])

operation = get_operator(operator)
print("{} {} {} = {}".format(a, operator, b, operation(a, b)))
