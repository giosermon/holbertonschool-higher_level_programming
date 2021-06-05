#!/usr/bin/python3
""" function to check if the object is exactly an instance of the specified class """


def is_same_class(obj, a_class):
    """ Returns True if the object is exactly an instance
    of the specified class """
    return (type(obj) == a_class)

