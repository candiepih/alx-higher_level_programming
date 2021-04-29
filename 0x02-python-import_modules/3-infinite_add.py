#!/usr/bin/python3
import sys

if __name__ == "__main__":
    pass

argv = sys.argv
summation = 0
for i, arg in enumerate(argv):
    if i == 0:
        continue
    summation += int(arg)
print(summation)
