class Matrix:
    def __init__(self, matrix_string):
        string_rows = matrix_string.split('\n')
        self.rows = [self.split_string_into_integer_list(sr) for sr in string_rows]

    def split_string_into_integer_list(self, string_of_numbers):
        return list(map(lambda x: int(x), string_of_numbers.split(' '))) 

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return [r[index-1] for r in self.rows]
