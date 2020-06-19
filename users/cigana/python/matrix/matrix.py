class Matrix:
    def __init__(self, matrix_string):
        matrix_string = [elem.split(' ') for elem in matrix_string.splitlines()]
        self.matrix_string = [[int(s) for s in matrix_string[i]] for i in range(len(matrix_string))]

    def row(self, index):
        return self.matrix_string[index - 1]

    def column(self, index):
        return [list(elem) for elem in zip(*self.matrix_string)][index - 1]