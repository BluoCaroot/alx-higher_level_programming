#!/usr/bin/python3
"""writes to file"""


def append_write(filename="", text=""):
    """defines function to append to file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
