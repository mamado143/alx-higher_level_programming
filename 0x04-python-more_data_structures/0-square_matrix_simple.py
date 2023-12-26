#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a given matrix."""
    if not matrix:
        return None

    return list(list(map(lambda x: x*x, new_matrix)) for new_matrix in matrix)
