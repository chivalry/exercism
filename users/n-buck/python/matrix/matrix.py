import numpy as np

class Matrix:
    def __init__(self, matrix_string):
        m = []
        for column_string in matrix_string.split('\n'):
            m.append([int(i) for i in column_string.split(' ')])
        self._matrix = m
        pass

    def row(self, index):
        return self._matrix[index - 1]

    def column(self, index):
        return [i[index - 1] for i in self._matrix]
