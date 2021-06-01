#!/usr/bin/python3
"""print that write into a file"""


def write_file(filename="", text=""):
    """ Function to write on a file.
        Args:
            filename (str): Name of the file to write in.
            text (str) Text to write into the file.
        Return:
       The numbers of characters written.
    """
    with open(filename, "w", encoding='utf-8') as file:
        return(file.write(text))
