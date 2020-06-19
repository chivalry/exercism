class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [
            [int(num) for num in x.split(' ')] #splits string into spaced numbers
                    for x in matrix_string.split('\n') #splits into rows
                ] 

    def row(self, index):
        return self.matrix[index-1] 

    def column(self, index):
        return [num[index-1] for num in self.matrix]
