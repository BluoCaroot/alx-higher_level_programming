#!/usr/bin/python3
"""defines rectangle class"""


class Rectangle:
    """rectangle"""

    def __init__(self, width=0, height=0):

        """instance called when object is first created"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """set/get width"""

        return (self.__width)

    def width(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set/get height"""

        return (self.__height)

    def height(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
