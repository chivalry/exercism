class Garden:
    def __init__(self, diagram, students=['Alice', 'Bob', 'Charlie', 'David',
                                          'Eve', 'Fred', 'Ginny', 'Harriet',
                                          'Ileana', 'Joseph', 'Kincaid',
                                          'Larry']):
        self.row_1, self.row_2 = diagram.split(sep='\n')
        self.plants_dict = {'G': 'Grass', 'V': 'Violets',
                            'R': 'Radishes', 'C': 'Clover'}
        self.students = sorted(students)

    def plants(self, student):
        i = self.students.index(student)
        letters = self.row_1[2 * i:2 * i + 2] + self.row_2[2 * i:2 * i + 2]
        return [self.plants_dict[letter] for letter in letters]
