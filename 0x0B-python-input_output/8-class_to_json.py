#!/usr/bin/python3
"""Contains function that serializes a class object"""


def class_to_json(obj):
    """serializes an object"""
    return obj.__dict__
