#!/usr/bin/python3
"""Contains function  that appends to file"""


def append_write(filename="", text=""):
    """Handles content appending to file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
