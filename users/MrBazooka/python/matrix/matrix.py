class Matrix:
    def __init__(self, matrix_string):
    	self.rows = [[int(i) for i in row.split()] for row in matrix_string.split("\n")]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return [i[index - 1] for i in self.rows]
