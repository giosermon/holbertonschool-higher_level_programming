#!/usr/bin/python3
"""Documentation for a square class"""


class Square():
    '''class Square.
    '''

    # creating the instance
    def __init__(self, size=0):
        '''Initialization of instance attributes
            Args:
            size (int): The size of the square
        '''
        self.size = size
    # propeerty. Private instnace atributte size

    @property
    def size(self):
        '''
            property  to retrieve it
        '''
        return self.__size

    # setter
    @size.setter
    def size(self, value):
        '''
            property  setter to set it
            Args:
            value(int)
        '''
        if type(value) != int:
                raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    # public instance. Returns the area
    def area(self):
        '''
            Method that returns the current square area
        '''
        return self.__size * self.__size

    # public instance. prints the cuadrado
    def my_print(self):
        '''
            Method that prints in stdout the square with
            the character #
        '''
        if self.size is 0:
            print(' ')
        for i in range(self.size):
            for j in range(self.size):
                print("#", end='')
            print()
