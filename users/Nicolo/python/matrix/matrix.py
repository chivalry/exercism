class Matrix:
    def __init__(self, matrix_string):
        self.mat = [list(map(int, x.split(' '))) for x in matrix_string.split('\n')]

    def row(self, index):
        return self.mat[index - 1]

    def column(self, index):
        return [x[index - 1] for x in self.mat]
