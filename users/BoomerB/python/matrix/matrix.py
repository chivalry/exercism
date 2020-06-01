class Matrix:
    def __init__(self, matrix_string):
        self._matrix = [
            [int(x) for x in line.split()] for line in matrix_string.splitlines()
        ]

    def row(self, index):
        """return row index, with index 1 based"""
        return self._matrix[index - 1]

    def column(self, index):
        """return column index, with index 1 based"""
        return [row[index - 1] for row in self._matrix]
