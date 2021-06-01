#!/usr/bin/python3
"""Contain functions that andles json files"""
import json


def save_to_json_file(my_obj, filename):
    """saves content of json to file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
