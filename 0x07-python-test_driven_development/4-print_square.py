#!/usr/bin/python3
"""Module ro add value int or float
"""


def print_square(size):
    """Ffunction that prints a square with the character #.
    Args:
        size (int): is the size length of the square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
