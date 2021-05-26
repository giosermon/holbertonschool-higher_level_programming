#!/usr/bin/python3
"""Module ro add value int or float
"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix.
    Args:
        matrix (int): list of integers
        div (int): number
    Returns:
        new_matrix2 (int): a new matrix with the division by two
    """

    if type(matrix) != list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    new_matrix2 = []
    for row in matrix:
        if type(row) != list:
            raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats")
        for item in row:
            if type(item) != int and type(item) != float:
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats")
            result = item / div
            new_matrix.append(round(result, 2))
        new_matrix2.append(new_matrix)
        new_matrix = []
    return new_matrix2
