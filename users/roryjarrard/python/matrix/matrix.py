class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        for s in matrix_string.split('\n'):
            self.matrix.append([int(x) for x in s.split(' ')])

    def row(self, index):
        return [self.matrix[index - 1][x] for x in range(len(self.matrix[index - 1]))]

    def column(self, index):
        return [self.matrix[y][index - 1] for y in range(len(self.matrix))]
