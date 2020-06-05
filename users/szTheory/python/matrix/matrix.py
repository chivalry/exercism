import logging


class Matrix:
    def __init__(self, matrix_string):
        self.matrix = self.__matrix_from_string(matrix_string)

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        vals = []
        for row in self.matrix:
            vals.append(row[index-1])

        return vals

    def __matrix_from_string(self, string):
        lines = string.split("\n")
        matrix = []
        for line in lines:
            chars = line.split(" ")
            numbers = [int(ch) for ch in chars]
            matrix.append(numbers)

        return matrix
