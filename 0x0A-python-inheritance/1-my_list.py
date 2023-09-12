#!/usr/bin/python3
"""defines list MyList"""


class MyList(list):
    """defines list that has function print_sorted"""
    pass

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(list(self)))
