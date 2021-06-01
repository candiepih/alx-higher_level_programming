#!/usr/bin/python3
"""Contains function involved in json handling"""
import json


def to_json_string(my_obj):
    """serializes and object to json"""
    serialized_json = json.dumps(my_obj)
    return serialized_json
