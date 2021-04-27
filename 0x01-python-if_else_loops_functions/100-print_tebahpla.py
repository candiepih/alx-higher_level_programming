#!/usr/bin/python3
for i in range(122, 96, -1):
    print(chr(i) if i % 2 is 0 else chr(65 + (i - 97)), end="")
