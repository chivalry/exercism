class Matrix:
    def __init__(self, matrix_string):
        self.rows = matrix_string.split("\n")
        self.matrix_list = []
        for each in self.rows:
            item_r = each.split(" ")
            self.matrix_list.append(item_r)

    def row(self, index):
        str_list = self.matrix_list[index - 1]
        li = []
        for each in str_list:
            num = int(each)
            li.append(num)
        return  li

    def column(self, index):
        columns = [[col[i] for col in self.matrix_list] for i in range(len(self.matrix_list[0]))]
        str_col = columns[index -1]
        li = []
        for each in str_col:
            num = int(each)
            li.append(num)
        return li
