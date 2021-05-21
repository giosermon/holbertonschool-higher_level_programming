#!/usr/bin/python3
"""Documentation for basic Rectangle class"""



class Rectangle:
    """Initializes an empty Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''
            Method that returns the current rectangle area
        '''
        return (self.__height * self.__width)

    def perimeter(self):
        '''
            Method that returns the current rectangle perimeter
        '''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2 + self.__width * 2)

    def __str__(self):
        """Method to be used when use print on Rectangle
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return("")
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string = string + "#"
                if i < self.__height - 1:
                    string = string + '\n'
            return string

    def __repr__(self):
        class_name = self.__class__.__name__
        return "{}({}, {})".format(class_name, self.__width, self.__height)
