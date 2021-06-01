#!/usr/bin/python3
"""Contains functions involved in json handling"""
import json


def from_json_string(my_str):
    """change string to json objects"""
    deserialized_json = json.loads(my_str)
    return deserialized_json
