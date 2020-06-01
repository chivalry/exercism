class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [(row.split(' ')) for row in matrix_string.split('\n')]

    def row(self, index):
        return [int(item) for item in self.matrix[index-1]]

    def column(self, index):
        return [int(row[index-1]) for row in self.matrix]

