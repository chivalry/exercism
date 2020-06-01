class Matrix:
    matrix = []

    def __init__(self, matrix_string):
        rows = matrix_string.split("\n")
        self.matrix = [[int(col) for col in row.split(" ")] for row in rows]
        pass

    def row(self, index):
        return self.matrix[index-1]
        pass

    def column(self, index):
        return [row[index-1] for row in self.matrix]
        pass
