import numpy as np


class Matrix:
    def __init__(self, matrix_string):
        self.matrix = np.matrix(matrix_string.replace("\n", ";"), )

    def row(self, index):
        return np.matrix.tolist(self.matrix[index-1])[0]

    def column(self, index):
        return np.matrix.tolist(self.matrix[:, index-1].transpose())[0]
