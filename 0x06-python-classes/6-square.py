#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square

        Args:
            size (int): The size of the new square
            position (int, int): cord of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = size
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = position

    def area(self):
        """return area of square"""
        return (self.size ** 2)

    @property
    def size(self):
        """get/set size of square"""
        return (self.size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = value

    @property
    def position(self):
        """gets/sets position"""
        return (self.position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in vaule)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = value

    def my_print(self):
        """prints square"""
        for i in range(self.size):
            for j in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print("")
        if self.size == 0:
            print("")
