#!/usr/bin/python3
"""Documentation for a Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):

    """Square class that inherits from the Rectangle class
       which in turn inherited from the Base class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of a Square object
        Args:
            size (int): the size of the square
            x (int): the x coordinate
            y (int): the y coordinate
            id (int): the id of the object
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloading the __str__ method to return certain string"""

        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Getter for size attribute
        Returns:
            the size of the Square instance
        """

        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute
        Args:
            value (int): the size of the Square attribute
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the square instance
        Args:
            args (list): list of updated values
            kwargs (dict): dictionary of updated values
        """

        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]

        else:
            if len(kwargs) > 0:
                keys = kwargs.keys()
                for i in keys:
                    if i == 'id':
                        self.id = kwargs['id']
                    if i == 'size':
                        self.width = kwargs['size']
                        self.height = kwargs['size']
                    if i == 'x':
                        self.x = kwargs['x']
                    if i == 'y':
                        self.y = kwargs['y']

    def to_dictionary(self):
        """Returns the dictionary representation of the object
        Returns:
            the dictionary representation of the square object
        """

        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
