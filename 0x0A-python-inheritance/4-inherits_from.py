#!/usr/bin/python3
"""def inherits_from"""


def inherits_from(obj, a_class):
    """defines function that checks inheritance"""

    return (False if type(obj) is a_class else isinstance(obj, a_clas))
