class Matrix:
    def __init__(self, matrix_string):
        row_strings = self.lines_to_list(matrix_string)
        self.rows = []
        self.c = []
        for values in row_strings:
         self.c = self.row_to_cells(values)
         self.rows.append(self.c)
        
    
    def lines_to_list(self, matrix_string):
        row_string=matrix_string.split('\n')
        return row_string
       
       
    
    def row_to_cells(self, row):
         int_list = []
         cells=row.split()
         for element in cells:
          int_val=int(element)
          int_list.append(int_val)
         return int_list
       
          
           

    def row(self, index):
         return self.rows[index-1]
          

    def column(self, index):
         column = []
         for row_values in self.rows:
          t=row_values[index-1]
          column.append(t)
         return column 
