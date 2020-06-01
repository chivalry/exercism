class Matrix:
    def __init__(self, matrix_string):
        #Creating two new variables, b as the input without any spaces and an empty list to add values
        self.b = matrix_string.split('\n')
        self.new_matrix = []
    def row(self, index):
        #iterate on each elemnt of the list, current divided vi \n, split the spaces and make a nested list      
        for i in self.b:
            self.new_matrix.append(list(i.split()))
        #Iterate on each element of the nested list, to convert to int, then get the index value required returned as a list
        return [[int(s) for s in xs] for xs in self.new_matrix][index - 1]

    def column(self, index):
        for i in self.b:
            self.new_matrix.append(list(i.split()))

        c = [[int(s) for s in xs] for xs in self.new_matrix]
        #In this case we create a new list with all the values converted to int, then we will iterate again on the list to add each value from the colum selected
        self.colum_liist = []
        for i in c:
            self.colum_liist.append(i[index -1])
        return self.colum_liist
        #how can I improve my code?