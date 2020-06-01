import bisect


class School:
    def __init__(self):
        self.grades = {}

    def add_student(self, name, grade):
        self.grades.setdefault(grade, [])
        bisect.insort(self.grades[grade], name)

    def roster(self):
        buf = []
        for grade in sorted(self.grades.keys()):
            buf.extend(self.grades[grade])
        return buf

    def grade(self, grade):
        return self.grades[grade] if grade in self.grades else []
