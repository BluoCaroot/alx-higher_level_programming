#!/usr/bin/python3
"""locked class"""

class LockedClass:
    """locked class"""
    __slots__ = ['first_name']

    def __init__(self):
        """creates new instance"""
        self.first_name = 'first_name'
