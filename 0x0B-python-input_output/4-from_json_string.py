#!/usr/bin/python3

"""this module has a function that deserializes objects"""


import json


def from_json_string(my_str):
    """deserialize objects by using json"""
    return json.loads(my_str)
