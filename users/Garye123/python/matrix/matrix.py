class Matrix:
    def __init__(self, matrix_string):
        self.rows= matrix_string.split("\n")
        self.numbers= matrix_string.split()

    def row(self, index):
        return [int(i) for i in self.rows[index-1].split()]


    def column(self, index):
        column= []
        for i in self.rows:
            column.append(self.rows[index-1])
        return column


        # for row in self.numbers:
        #     column.append(int(row.split()[index-1]))
        # return column
