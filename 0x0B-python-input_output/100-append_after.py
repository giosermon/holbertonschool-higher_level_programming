#!/usr/bin/python3
""" function  Module that executes a function that appends a line  """


def append_after(filename="", search_string="", new_string=""):
    """ function """
    with open(filename, mode='r+', encoding='utf-8') as file:
        for line in file:
            if search_string in line:
                return(file.write(new_string))
