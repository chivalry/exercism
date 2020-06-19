class Matrix:
	def __init__(self, matrix_string):
		self.matrix =  [[int(i) for i in j.split()] for j in matrix_string.split("\n")]

	def row(self, index):
		return self.matrix[index -1]

	def column(self, index):
		return [self.matrix[i][index-1] for i in range(len(self.matrix))]


