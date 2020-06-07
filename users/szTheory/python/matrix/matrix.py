import logging


class Matrix:
    def __init__(self, matrix_string):
        self.matrix = self.__matrix_from_string(matrix_string)

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]

    def __matrix_from_string(self, string):
        lines = string.split("\n")
        matrix = [self.__row_from_line(line) for line in lines]

        return matrix

    def __row_from_line(self, line):
        chars = line.split(" ")
        row = [int(ch) for ch in chars]

        return row
