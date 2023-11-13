#!/usr/bin/python3
"""this the base class module where the base class is defined"""


import json

class Base:
    """This class will be the “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """create public instanece attr id
        and assign it to a value"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        my_list = []
        if list_objs is None:
            with open(cls.__name__ +".json", "w") as f:
                json.dump([]), f
        else:
            for obj in list_objs:
                my_list.append(obj.to_dictionary())
            with open(cls.__name__ + ".json", "w") as f:
                f.write(Base.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary is not None and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_ins = cls(3, 3)
            else:
                new_ins = cls(3)
            new_ins.update(**dictionary)
            return new_ins
    
    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + ".json", "r") as file: 
                data = file.read()
                if data.strip() == "":
                    return []
                dicts_list = cls.from_json_string(data)
                instances_list = []
                if type(dicts_list) == list and dicts_list != []:
                    for dict in dicts_list:
                        instances_list.append(cls.create(**dict))
            return instances_list
        except FileNotFoundError:
            return []
        



if __name__ == "__main__":
    # print(json.dumps("[]"))
    pass