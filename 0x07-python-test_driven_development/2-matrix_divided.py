#!/usr/bin/python3
"""
Divides a matrix
"""


def matrix_divided(matrix, div):
    length = len(matrix[0])
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    newlist = [[round(num/div, 2) for num in row] for row in matrix]
    return newlist
    """
    a function that divides a list 
    the parameters can be ints or floats
    Args:
        matrix(ist): A list containing a list of integers or floats
        div(int/float): A number to be used as the divisor
    :Returns(list): a list of qoutiants
    """
