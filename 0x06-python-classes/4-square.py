#!/usr/bin/python3
"""Documentation for a square class"""


class Square:
    """class square."""
    __size = 0

    def __init__(self, size=0):
        """Initialize a new Square."""
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """ define the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Define area of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
