#!/usr/bin/python3
"""Documentation for a square class"""


class Square:
    """Class square"""
    __size = 0

    def __init__(self, size=0):
        """Initialize a new Square."""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
