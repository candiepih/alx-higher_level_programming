#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{:c}".format(i) if i % 2 == 0 else
          "{:c}".format(65 + (i - 97)), end="")
