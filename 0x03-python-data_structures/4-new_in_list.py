#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        if idx < 0 or idx >= len(my_list):
            return (my_list)
        new_list = []
        for i in my_list:
            new_list.append(i)
        new_list[idx] = element
        return (new_list)
