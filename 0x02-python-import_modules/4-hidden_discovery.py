#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    pass

list_names = dir(hidden_4)

for names in list_names:
    if names[0] == "_":
        continue
    print(names)
