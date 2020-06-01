
class Matrix:
    def __init__(self, matrix_string):
        matrix_string = matrix_string.strip().split('\n')
        matrix_string = [i.split() for i in matrix_string]
        self.proper_list = [[int(k) for k in i] for i in matrix_string]

    def row(self, index):
        return self.proper_list[index-1]

    def column(self, index):
        columns = [x[index-1] for x in self.proper_list]
        return columns


# text =
# """
# 9 8 7
# 5 3 2
# 6 6 7
# """
#
# lol = Matrix(text)



