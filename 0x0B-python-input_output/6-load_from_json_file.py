#!/usr/bin/python3
"""Contains functions that handle json"""
import json


def load_from_json_file(filename):
    """Returns deserialized data from file"""
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)
    return data
