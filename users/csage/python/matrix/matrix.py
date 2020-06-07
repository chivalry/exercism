class Matrix:
    def __init__(self, matrix_string):
        self._matrix = [[int(i) for i in row.split(" ")] for row in matrix_string.split("\n")]

    def row(self, index):
        return self._matrix[index-1]

    def column(self, index):
        return [self._matrix[i][index-1] for i in range(len(self._matrix))]
