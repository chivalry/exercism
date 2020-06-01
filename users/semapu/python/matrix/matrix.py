class Matrix:
    def __init__(self, matrix_string):

        # Split the matrix_string by rows and convert values to int
        self.rows_ints = [list(map(int, row.split(" "))) for row in matrix_string.split("\n")]

    def row(self, index):

        # Return the requestes row 
        # "-1" because the indexes start from 1 (no from 0)
        print(self.rows_ints[index-1])
        return self.rows_ints[index-1]

    def column(self, index):

        # Initialize the final variable
        column = []

        # For each row, extract the requested colum
        # "-1" because the indexes start from 1 (no from 0)
        for row in self.rows_ints:
            column.append(row[index-1])

        return column