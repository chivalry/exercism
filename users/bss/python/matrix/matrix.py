class Matrix:
    def __init__(self, matrix_string):
        self.rows = matrix_string.split("\n")

    def row(self, index):
        return [int(x) for x in self.rows[index - 1].split(" ")]

    def column(self, index):
        return [int(x.split(" ")[index - 1]) for x in self.rows]
