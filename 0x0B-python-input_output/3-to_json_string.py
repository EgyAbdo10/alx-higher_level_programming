#!/usr/bin/python3

"""this module has a function that serializes objects"""


import json


def to_json_string(my_obj):
    """serialize objects by using json"""
    return json.dumps(my_obj)
