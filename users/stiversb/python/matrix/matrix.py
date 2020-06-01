""" This module implements a super simple matrix in support of
    exercism python track exercise 5.  Spec is:
    https://exercism.io/my/solutions/6e45425a6e8c464fb0e1a667a48c7e48

    TODO: Maybe implement floating point.
    TODO: Maybe implement more matrix operations.
"""

class Matrix:
    """Stupid simple matrix class implementation"""

    def __init__(self, matrix_string):
        self.matrix = []
        rows = matrix_string.split("\n")
        for row in rows:
            outline = [int(element) for element in row.split()]
            self.matrix.append(outline)

    def row(self, index):
        """Returns a row of our matrix as a list of integers"""
        return self.matrix[index-1]

    def column(self, index):
        """Returns a column of out matrix as a list of integers"""
        return [line[index-1] for line in self.matrix]
