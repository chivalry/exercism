class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.index_list = [self.l.split(' ') for self.l in ''.join(self.matrix_string).split('\n')]

    def row(self, index):
        self.index = index - 1
        return list(map(int, self.index_list[self.index]))

    def column(self, index):
        self.index = index - 1
        return list(map(int, [row[self.index] for row in self.index_list]))