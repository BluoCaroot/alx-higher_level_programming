#!/usr/bin/python3
"""loads from file"""
import json


def load_from_json_file(filename):
    """defines function"""
    with open(filename, 'r') as f:
        return json.load(f)
