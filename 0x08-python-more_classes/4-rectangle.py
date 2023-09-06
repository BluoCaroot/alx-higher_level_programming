#!/usr/bin/python3
"""defines rectangle class"""


class Rectangle:
    """rectangle"""

    def __init__(self, width=0, height=0):

        """instance called when object is first created"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """set/get width"""

        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """set/get height"""

        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns perimeter of the rectangle"""
        if self.__height > 0 and self.__width > 0:
            return ((self.__height + self.__width) * 2)
        else:
            return (0)

    def __str__(self):
        """Casts rectnalge to string"""
        if (self.__width == 0) or (self.__height == 0):
            return ('')
        x = '#' * self.__width
        ret = ''
        for i in range(self.__height):
            ret += x
            if i < self.__height - 1:
                ret += '\n'
        return (ret)

    def __repr__(self):
        """Returns string representation of the rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
