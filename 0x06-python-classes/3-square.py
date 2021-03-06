#!/usr/bin/python3
"""Documentation for a square class"""


class Square():
    '''class Square.
    '''
    def __init__(self, size=0):
        '''"""Initialize a new Square.
                Args:
                size (int): The size of the square
        '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size*self.__size
