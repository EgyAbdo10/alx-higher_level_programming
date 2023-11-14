#!/usr/bin/python3
"""Module defining the Base class."""

import json


class Base:
    """
    This class will be the “base” of all other classes in this project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Creates a public instance attribute 'id' and assigns it a value.

        Args:
            id (int): Identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON representation of the list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of instances to a file in JSON format.

        Args:
            list_objs (list): List of instances.
        """
        my_list = []
        if list_objs is None:
            with open(cls.__name__ + ".json", "w") as f:
                json.dump([], f)
        else:
            for obj in list_objs:
                my_list.append(obj.to_dictionary())
            with open(cls.__name__ + ".json", "w") as f:
                f.write(Base.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance based on a dictionary.

        Args:
            dictionary (dict): Dictionary containing attributes.

        Returns:
            Base: Instance created from the dictionary.
        """
        if dictionary is not None and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_ins = cls(3, 3)
            else:
                new_ins = cls(3)
            new_ins.update(**dictionary)
            return new_ins
    
    @classmethod
    def load_from_file(cls):
        """
        Loads instances from a file in JSON format.

        Returns:
            list: List of instances.
        """
        try:
            with open(cls.__name__ + ".json", "r") as file: 
                data = file.read()
                if data.strip() == "":
                    return []
                dicts_list = cls.from_json_string(data)
                instances_list = []
                if isinstance(dicts_list, list) and dicts_list != []:
                    for dictionary in dicts_list:
                        instances_list.append(cls.create(**dictionary))
            return instances_list
        except FileNotFoundError:
            return []