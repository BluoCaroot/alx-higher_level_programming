#!/usr/bin/python3
"""reads file"""


def read_file(filename=""):
    """defines function that reads from file"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
