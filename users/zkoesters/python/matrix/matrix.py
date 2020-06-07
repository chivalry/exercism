class Matrix:
    def __init__(self, matrix_string):
        self._matrix = []
        for row_string in matrix_string.splitlines():
            self._matrix.append(list(map(int, row_string.split())))

    def row(self, index):
        return self._matrix[index-1]

    def column(self, index):
        return [i[index-1] for i in self._matrix]
