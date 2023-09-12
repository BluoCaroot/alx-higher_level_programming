#!/usr/bin/python3
"""saves to json file"""
import json


def save_to_json_file(my_obj, filename):
    """defines function"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
