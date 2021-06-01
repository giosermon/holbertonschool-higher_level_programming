#!/usr/bin/python3
""" Create object from a JSON file """
import json


def load_from_json_file(filename):
    """ Function that creates an Object from a “JSON file”
    
    Args:
       filename: Name of the JSON file.
    Return:
       A python object.

    """
    with open(filename, 'r') as f:
        return (json.load(f))
