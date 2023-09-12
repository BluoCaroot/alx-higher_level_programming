#!/usr/bin/python3
"""defines Student class"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """constructor method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrives class dictionary"""

        return self.__dict__()
