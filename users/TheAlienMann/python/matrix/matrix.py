class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = [[int(item) for item in items.split()] for items in matrix_string.split("\n")]

    def row(self, index):
        return self.matrix_string[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix_string]

    def number_of_row(self):
        return len(self.matrix_string)

    def number_of_columns(self):
        return len(self.matrix_string[0])

    def size(self):
        return self.number_of_row(), self.number_of_columns()


print(Matrix("1 2 3 4\n5 6 7 8\n9 8 7 6").size())
