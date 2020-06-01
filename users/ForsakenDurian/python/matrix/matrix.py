class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(num) for num in row.split()] for row in
                       matrix_string.splitlines()]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [matrix_row[index-1] for matrix_row in self.matrix]
