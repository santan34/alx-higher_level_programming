#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for i in matrix:
        newrow = list(map(lambda x: x**2, i))
        newmatrix.append(newrow)
    return newmatrix
