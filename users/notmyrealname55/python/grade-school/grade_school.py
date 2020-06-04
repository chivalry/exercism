class School:
    def __init__(self):
        # list of lists with grade number in index 0, list of names in index 1
        self._roster = []

    def add_student(self, name, grade):
        # making a new grade by appending to end of _roster
        if grade not in [grade[0] for grade in self._roster]:
            self._roster.append([grade, [name]])
        # adding name to existing grade by appending to end of list of names
        else:
            index = [grade[0] for grade in self._roster].index(grade)
            self._roster[index][1].append(name)

    def roster(self):
        all_grades = []
        # flattening list of lists by grade order using grade function
        for grade_number in sorted([grade[0] for grade in self._roster]):
            all_grades.extend(self.grade(grade_number))
        return all_grades


    def grade(self, grade_number):
        # if grade number doesn't exist, appends it with an empty list of names
        if grade_number not in [grade[0] for grade in self._roster]:
            self._roster.append([grade_number, []])

        # find where in the list of lists the grade is
        index = [grade[0] for grade in self._roster].index(grade_number)

        # return the sorted list of names
        return sorted(self._roster[index][1])


if __name__ == "__main__":
    school = School()
    school.add_student(name="Peter", grade=2)
    school.add_student(name="Anna", grade=1)
    school.add_student(name="Barb", grade=1)
    school.add_student(name="Zoe", grade=2)
    school.add_student(name="Alex", grade=2)
    school.add_student(name="Jim", grade=3)
    school.add_student(name="Charlie", grade=1)

    print(school.roster())
    print(school.grade(1))
    print(school.grade(2))
    print(school.grade(3))