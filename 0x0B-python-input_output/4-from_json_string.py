#!/usr/bin/python3
"""converts json string to python obj"""
import json


def from_json_string(my_str):
    """defines function"""
    return (json.loads(my_str))
