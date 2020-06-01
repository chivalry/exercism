class Garden:
    CODES = {
        'G': 'Grass',
        'C': 'Clover',
        'R': 'Radishes',
        'V': 'Violets'
    }

    DEFAULT = ['Alice', 'Bob', 'Charlie', 'David',
               'Eve', 'Fred', 'Ginny', 'Harriet',
               'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def __init__(self, diagram, students=DEFAULT):
        self.diagram = diagram.split()
        self.students = sorted(students)[:len(self.diagram[0]) // 2]
        self.shelves = {student: [
            self.CODES[self.diagram[0][2 * i]],
            self.CODES[self.diagram[0][2 * i + 1]],
            self.CODES[self.diagram[1][2 * i]],
            self.CODES[self.diagram[1][2 * i + 1]]
        ] for i, student in enumerate(self.students)}

    def plants(self, student):
        return self.shelves[student]
