class Matrix:
    def __init__(self, matrix_string):
        self.rows = [[int(num) for num in _.split(' ')] for _ in matrix_string.split('\n')]
        self.columns = []
        for i in range(len(self.rows[0])):
            self.columns.append([num[i] for num in self.rows])

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]