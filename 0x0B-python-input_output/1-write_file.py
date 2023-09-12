#!/usr/bin/python3
"""writes to file"""


def write_file(filename="", text=""):
    """defines function to write to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
