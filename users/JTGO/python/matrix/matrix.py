class Matrix:
    #Constructor: Converts string to int Matrix
    def __init__(self, matrix_string):
        self.m=[[int(col_str) for col_str in row_str.split()] for row_str in matrix_string.split("\n")]
    #Getting a row from the Matrix
    def row(self, index):
        return self.m[index-1]
    #Getting a column from the Matrix
    def column(self, index):
        c=[self.m[i][index-1] for i in range(0,len(self.m))]
        return c