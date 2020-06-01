class Matrix:
    def __init__(self, matrix_string):
        self.matrix = self._parse_matrix(matrix_string)

    def _parse_matrix(self, string):
        return [
            [int(cell) for cell in row.split(" ")]
            for row in string.split("\n")]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [list(col) for col in zip(*self.matrix)][index - 1]
