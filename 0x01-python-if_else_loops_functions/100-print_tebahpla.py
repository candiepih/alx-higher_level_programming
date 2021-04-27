#!/usr/bin/python3
for i in reversed(range(97, 123)):
    print(chr(i) if i % 2 is 0 else chr(65 + (i - 97)), end="")
