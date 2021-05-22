#!/usr/bin/python3
"""Module Defines a locked class."""


class LockedClass:
    """
    Class that defines Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    
    """
    __slots__ = ["first_name"]
