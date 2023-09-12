#!/usr/bin/python3
"""defines Student class"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """constructor method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrives class dictionary"""

        if (type(attrs) == list and
                all(type(x) == str for x in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """replace all attrs"""
        for k, v in json.items():
            setattr(self, k, v)
