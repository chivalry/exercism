number=0
school={}
class School(object):
    def __init__(self):
        school={}

    def add_student(self, name, grade):
        school[number]={name:grade}
        number+=1

    def roster(self):
        school=school.sort()
        print(school)

    def grade(self, grade_number):
        print(school[grade_number])