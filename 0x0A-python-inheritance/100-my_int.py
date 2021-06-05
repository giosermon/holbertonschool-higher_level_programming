#!/usr/bin/python3
""" New class """


class MyInt(int):
    """ A class MyInt that inherits from int """
    def __eq__(self, num):
        """ Function for equals """
        return(int(self) != int(num))

    def __ne__(self, num):
        """ Function for not equals """
        return (int(self) == int(num))
