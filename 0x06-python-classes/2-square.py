#!/usr/bin/python3
"""Class Square defines a square"""


class Square:
    """ A class that defines a square.

    by its size.

    """
    def __init__(self, size=0):
        """ Method to initialize the square object.

        Args: 
            size(int) this defines the size of the square.
                The size is validated with try/except.

        """
        try:
            self.__size = size
            if size < 0:
                raise ValueError
            if type(size) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
