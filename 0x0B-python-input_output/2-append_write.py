#!/usr/bin/python3
""" Append to a file """


def append_write(filename="", text=""):
    """Function to append a text in a file
    
    Args:
            filename (str): Name of the file to append to.
            text (str): Text to append to the file.
     Return:
       The numbers of characters written.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return (file.write(text))
