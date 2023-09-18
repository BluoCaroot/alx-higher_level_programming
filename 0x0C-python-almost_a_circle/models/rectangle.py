#!/usr/bin/python3
"""defines rectangle class"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets/sets width"""

        return self.__width

    @width.setter
    def width(self, width):

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """gets/sets height"""

        return self.__height

    @height.setter
    def height(self, height):

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """gets/sets x"""

        return self.__x

    @x.setter
    def x(self, x):

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0)")
        else:
            self.__x = x

    @property
    def y(self):
        """gets/sets y"""

        return self.__y

    @y.setter
    def y(self, y):

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """returns area of rectangle"""

        return self.__width * self.__height
