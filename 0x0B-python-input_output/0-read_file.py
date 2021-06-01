#!/usr/bin/python3
"""Module that read a file
"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename (str): text file to read .
    """
    with open(filename, encoding="utf-8") as file:
         for l in file:
                print(l, end="")
