class Matrix:
    
    def __init__(self, matrix_string):
        self.matrix = []
        self.matrix = [[int(x) for x in row.split(' ')] for row in matrix_string.split('\n')]

    def row(self, index):
        return self.matrix[:][index - 1]

    def column(self, index):
        return [i[index - 1] for i in self.matrix]
