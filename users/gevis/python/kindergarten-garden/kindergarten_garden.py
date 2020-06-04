from typing import List, Optional


class Garden:

    plant_dict = {'G': "Grass", 'C': "Clover", 'R': "Radishes", 'V': "Violets"}
    default_students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                        "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

    def __init__(self, diagram: str, students: Optional[List[str]] = None):
        self.rows = diagram.split("\n")
        self.students = sorted(students) if students else Garden.default_students

    def plants(self, student: str) -> List[str]:
        index = 2 * self.students.index(student)
        plant_lst = []
        for row in self.rows:
            plant_lst.append(Garden.plant_dict[row[index]])
            plant_lst.append(Garden.plant_dict[row[index+1]])
        return plant_lst


