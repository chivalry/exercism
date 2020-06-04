class Garden:
    seeds = (('G', 'Grass'), ('C', 'Clover'), ('R', 'Radishes'), ('V', 'Violets'))

    students = ('Alice','Bob', 'Charlie', 'David', 'Eve', 'Fred',
                'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry')

    def __init__(self, diagram, students=students):
        self.diagram = diagram.split()
        self.students = sorted(students)

    def decode(self, seed_codes):
        seed_names = []
        for code in seed_codes:
            for letter, name in self.seeds:
                if code == letter:
                    seed_names.append(name)
        return seed_names

    def plants(self, student):
        seed_codes = []
        for n in range(len(self.students)):
            if self.students[n] == student:
                for row in self.diagram:
                    for letter in row[n*2:n*2+2]:
                        seed_codes.append(letter)
        return self.decode(seed_codes)
        