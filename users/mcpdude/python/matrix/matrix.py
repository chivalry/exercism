class Matrix:
    def __init__(self, matrix_string):
        self.rows = [list(map(int, row.split(' '))) for row in matrix_string.split('\n')]
        # for row in matrix_string.split("\n"):
        # 	self.rows.append(list(map(int, row.split(" ")))
       	
        print(self.rows)

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        output = [row[index - 1] for row in self.rows]

        return output
