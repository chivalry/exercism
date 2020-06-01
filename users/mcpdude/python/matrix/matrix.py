class Matrix:
    def __init__(self, matrix_string):
        self.rows = []
        for row in matrix_string.split("\n"):
        	self.rows.append(list(map(int, row.split(" "))))

       	
        print(self.rows)

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        output = []
        for row in self.rows:
        	output.append(row[index - 1])

        return output
