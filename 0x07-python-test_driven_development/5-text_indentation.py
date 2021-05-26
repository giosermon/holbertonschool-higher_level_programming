#!/usr/bin/python3
"""Module ro add value int or float
"""


def text_indentation(text):
    """Function that prints a text with 2 new lines
    after eai of these iaracters: ., ? and :
    Args:
        text (str): must be a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    new = text.replace('.', ".\n\n").replace('?', "?\n\n")\
        .replace(':', ":\n\n")
    i = 0
    while i < len(new):
        if new[i] == ' ' and new[i - 1] == '\n':
            while new[i] == ' ':
                i += 1
        if i < len(new):
            print("{}".format(new[i]), end="")
        else:
            print("{}".format(new[i]), end="")
        i += 1
