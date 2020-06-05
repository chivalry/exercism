class Matrix:
    def __init__(self, matrix_string):

        matrix_list = []
        if len(matrix_string.split("\n")) == 1:
            matrix_list.append(matrix_string.splitlines()[0].split())

        else:
            i = 0
            while i < len(matrix_string.split("\n")):
                matrix_list.append(matrix_string.splitlines()[i].split())
                i += 1

        self.matrix = [list(map(int, x)) for x in matrix_list]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [[row[i] for row in self.matrix] for i in range(len(self.matrix[0]))][
            index - 1]
