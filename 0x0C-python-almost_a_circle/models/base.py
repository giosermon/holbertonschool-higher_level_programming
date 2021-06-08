#!/usr/bin/python3
""" Create a new class Base """


import os
import json


class Base:

    """New class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation function for Base instance
        Args:
            id (int): the id of the instance
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list_dictionaries
        Args:
            list_dictionaries (list): the list of dictionaries
        Returns:
            the JSON representation of list_dictionaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation to a file
        Args:
            list_objs (list): list of instances who inherits from Base
        """

        file = "{}.json".format(cls.__name__)
        new_list = []
        with open(file, 'w') as f:
            if list_objs is None or len(list_objs) is 0:
                f.write("[]")
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation argument
        Args:
            json_string (str): the JSON object representation of a list
            of dictionaries
        """

        if json_string is None or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            dictionary (dict): dictionary of attributes to set
        Returns:
            the instance with all attributes set
        """

        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        if cls.__name__ == "Square":
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return (new_instance)


    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file with JSON object
        Returns:
            the instance list object with all instances initialized
        """

        list = []
        filename = "{}.json".format(cls.__name__)
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                instance_object = cls.from_json_string(f.read())
                for dict_list in instance_object:
                    list.append(cls.create(**dict_list))
                return list
        else:
            return []
