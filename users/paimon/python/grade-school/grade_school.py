import bisect
class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade in self.students:
            bisect.insort(self.students[grade], name)
        else:
            self.students[grade] = [name]

    def roster(self):
        roster = []
        for grade in sorted(self.students.keys()):
            roster += self.students[grade]
        return roster

    def grade(self, grade_number):
        if grade_number in self.students:
            return self.students[grade_number]
        return []
