class Matrix():
    """
    >>> A = "1 2 3 4\\n5 6 7 8\\n9 10 11 12"
    >>> A
    '1 2 3 4\\n5 6 7 8\\n9 10 11 12'
    >>> instance_of_class = Matrix(A)
    >>> instance_of_class.matrix
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    >>> transposed = [instance_of_class.column(_+1) for _ in range(0,len(instance_of_class.matrix)+1)]
    >>> print(f"Below is the transpose of instance_of_class.matrix:\\n{transposed}")
    Below is the transpose of instance_of_class.matrix:
    [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    """
    def __init__(self, matrix_string):
        self.matrix = [(lambda x: [int(j) for j in x])( i.split() ) for i in matrix_string.split('\n')]
    def row(self, index):
        return self.matrix[index - 1]
    def column(self, index):
        return [row[index - 1] for row in self.matrix]
