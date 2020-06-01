class Matrix:
    def __init__(self, matrix_string):
        self.matrix_sting = matrix_string.splitlines()

    def row(self, index):
        row_string = self.matrix_sting[index - 1].split()
        return [int(element) for element in row_string]

    def column(self, index):
        return [int(row.split()[index - 1]) for row in self.matrix_sting]
