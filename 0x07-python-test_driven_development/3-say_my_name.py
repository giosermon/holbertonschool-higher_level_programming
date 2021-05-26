#!/usr/bin/python3
"""Module 3-say_my_name
"""


def say_my_name(first_name, last_name=""):
    """Function that prints My name is <first name> <last name>
    Args:
    first_name (string): must be a string
    last_name (str):  must be a string.
    """
    if type(first_name) != str or first_name is None:
        raise TypeError("first_name must be a string")
    if type(last_name) != str or last_name is None:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
    