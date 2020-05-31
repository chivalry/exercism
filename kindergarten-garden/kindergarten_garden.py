class Garden:
    codes = {
        'G': 'Grass',
        'C': 'Clover',
        'R': 'Radishes',
        'V': 'Violets'
    }

    def __init__(self, diagram, students=None):
        self.diagram = diagram.split()
        self.students = students if students else None

    def plants(self, student):
        if not self.students:
            self.students = ['Alice', 'Bob', 'Charlie', 'David',
                             'Eve', 'Fred', 'Ginny', 'Harriet',
                             'Ileana', 'Joseph', 'Kincaid', 'Larry']
        else:
            self.students.sort()
        i = self.students.index(student)
        return [
            self.codes[self.diagram[0][2 * i]],
            self.codes[self.diagram[0][2 * i + 1]],
            self.codes[self.diagram[1][2 * i]],
            self.codes[self.diagram[1][2 * i + 1]]
        ]
