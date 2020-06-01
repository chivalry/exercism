class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(num) for num in row_string.split(" ")] for row_string in matrix_string.split("\n")]
        self.size = len(self.matrix)
    
    def row(self, index):
        try:
            return self.matrix[index - 1]
        except IndexError as e:
            raise Exception("{} is out of range. Please use index between {} and {}".format(index, 1, self.size))

    def column(self, index):
        try:
            return [self.matrix[i][index - 1] for i in range(self.size)]
        except IndexError as e:
            raise Exception("{} is out of range. Please use index between {} and {}".format(index, 1, self.size))
