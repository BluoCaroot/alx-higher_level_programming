#!/usr/bin/python3
"""divides a matrix"""

def matrix_divided(matrix, div):
    """ returns the result of dividing matrix by div

    Args:
        matrix(list): A list of lists of ints or floats
        div: number to divide by
    Raises:
        TypeError: if matrix contains non-numbers
        TypeError: if rows of matrix not same size
        TypeError: if div not a number
        ZeroDivisionError: if div is zero
    """
    if (not isinstance(div, int) and not isinstance(div float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if any x in i not isinstance(x, int)
