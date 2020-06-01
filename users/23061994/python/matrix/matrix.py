class Matrix:
    def __init__(self, matrix_string):
        raw = matrix_string.split("\n")
        self.row_mat = [
            [int(item) for item in raw[i].split(" ")] for i in range(len(raw))
        ]

    def row(self, index):
        return self.row_mat[index - 1]

    def column(self, index):
        column = [self.row_mat[item][index - 1] for item in range(len(self.row_mat))]
        return column
