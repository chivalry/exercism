class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.l=[[int(x) for x in ss.split(' ')] for ss in self.matrix_string.split('\n')]

    def row(self, index):
        return self.l[(index-1)]

    def column(self, index):
        c=[[r[i] for r in self.l] for i in range(index)]
        return c[(index-1)]
