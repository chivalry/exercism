class Matrix:
    def __init__(self, matrix_string):
        self._matrix = [[int(char) for char in row.split()] for row in matrix_string.split('\n')]

    def row(self, index):
        # looks like indexes are 1-based
        # returns a copy, just in case
        return self._matrix[index-1].copy()

    def column(self, index):
        return [row[index-1] for row in self._matrix]
