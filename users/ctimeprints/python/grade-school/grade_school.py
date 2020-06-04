class School(object):
    def __init__(self):
        self.l = []

    def add_student(self, name, grade):
        self.l.append((grade, name))

    def roster(self):
        return [n for g, n in sorted(self.l)]

    def grade(self, grade_number):
        return [n for g, n in sorted(self.l) if g==grade_number]
