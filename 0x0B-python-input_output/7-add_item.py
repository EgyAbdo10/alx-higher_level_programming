#!/usr/bin/python3

"""this module deserializes objects from json files"""


import json
import sys


def load_from_json_file(filename):
    """deserialize objects from json files"""
    with open(filename, encoding="UTF8") as file:
        return json.loads(file.read())


def save_to_json_file(my_obj, filename):
    """save objects into files by serializing them"""
    with open(filename, mode="w", encoding="UTF8") as file:
        file.write(json.dumps(my_obj))


my_input = sys.argv[1:]
my_list = []
try:
    my_list += load_from_json_file("add_item.json")
except (json.decoder.JSONDecodeError, FileNotFoundError):
    save_to_json_file(my_input, "add_item.json")
else:
    my_list += my_input
    save_to_json_file(my_list, "add_item.json")
