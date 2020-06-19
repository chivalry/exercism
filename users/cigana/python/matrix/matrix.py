class Matrix:
    def __init__(self, matrix_string):
        matrix_string = [elem.split(' ') for elem in matrix_string.splitlines()]
        
        for elem in matrix_string:
            for s in elem:
                elem[elem.index(s)] = int(s)

        self.matrix_string = matrix_string

    def row(self, index):
        return self.matrix_string[index - 1]

    def column(self, index):
        return list(list(zip(*self.matrix_string))[index - 1])
