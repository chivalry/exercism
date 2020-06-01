class Matrix:
    def __init__(self, matrix_string):
        self.matrix = list(x.split() for x in matrix_string.split("\n"))

    def row(self, index):
        return list(map(int, self.matrix[index - 1]))

    def column(self, index):
        return list(int(y[index - 1]) for y in self.matrix)
