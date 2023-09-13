#!/usr/bin/python3
"""tech interview"""


def pascal_triangle(n):
    """pascal triangle"""

    x = []
    ret = []
    if n <= 0:
        return x
    
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                x += [1]
            else:
                x += [last[j - 1] + last[j]]
        last = x
        ret += [x]
        x = []
    return ret
