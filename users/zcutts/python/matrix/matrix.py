class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix_list = [int(x) for x in matrix_string.split()]
        self.matrix_count = matrix_string.count('\n')
        self.length = len(self.matrix_list)
        self.row_length = int(self.length/(self.matrix_count+1))

    def row(self, index):
    	t = index - 1
    	return self.matrix_list[(t)*self.row_length:index*self.row_length]

    def column(self, index):
    	t = index - 1
    	return self.matrix_list[t::self.row_length]



