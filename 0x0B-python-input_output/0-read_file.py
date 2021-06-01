#!/usr/bin/python3
"""Contains a single function that reads fiels"""


def read_file(filename=""):
    """Reads and prints content of tile"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
