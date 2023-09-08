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
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(error)
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(error)
        if len(i) == 0:
            raise TypeError(error)
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(error)
    for i in range(len(matrix) - 1):
        if (len(matrix[i]) != len(matrix[i + 1])):
            raise TypeError("Each row of the matrix must have the same size")
    ret = []
    for i in matrix:
        temp = []
        for j in i:
            temp += [round(j / div, 2)]
        ret += [temp]
    return (ret)
