#!/usr/bin/python3

"""this module deserializes objects from json files"""


import json


def load_from_json_file(filename):
    """deserialize objects from json files"""
    with open(filename, encoding="UTF8") as file:
        return json.loads(file.read())
