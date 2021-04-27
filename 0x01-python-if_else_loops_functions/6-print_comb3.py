#!/usr/bin/python3
for i in range(1, 100):
    if int(str(i)[::-1]) < i or int(str(i)[::-1]) == i and i > 9:
        continue
    print("{:02d}".format(i), end=", " if i < 89 else "")
print()
