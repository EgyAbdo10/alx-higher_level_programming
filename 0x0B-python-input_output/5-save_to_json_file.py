#!/usr/bin/python3

"""this module saves objects into files"""


import json


def save_to_json_file(my_obj, filename):
    """save objects into files by serializing them"""
    with open(filename, mode="w", encoding="UTF8") as file:
        file.write(json.dumps(my_obj))
