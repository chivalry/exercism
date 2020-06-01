class Matrix:
    def __init__(self, matrix_string):
        self.matrix = ([[int(n) for n in row.split(" ")]
            for row in matrix_string.split("\n")])
        self.dim = len(matrix_string.split("\n"))

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [self.matrix[d][index - 1] for d in range(self.dim)]
