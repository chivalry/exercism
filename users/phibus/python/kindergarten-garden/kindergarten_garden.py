
seeds = ("Grass", "Clover", "Radishes", "Violets")
seeds = dict([(seed[0],seed) for seed in seeds])

class Garden:
    def __init__(self, diagram, students = [
    "Alice", "Bob", "Charlie", "David",
    "Eve", "Fred", "Ginny", "Harriet",
    "Ileana", "Joseph", "Kincaid", "Larry"
    ]):
        self.diagram = diagram.split("\n")
        self.students = students
        self.rank = dict([(name, rank) for rank, name in enumerate(sorted(self.students))])

    def plants(self, student):
        plants = []
        plants.append(seeds[self.diagram[0][self.rank[student]*2]])
        plants.append(seeds[self.diagram[0][self.rank[student]*2+1]])
        plants.append(seeds[self.diagram[1][self.rank[student]*2]])
        plants.append(seeds[self.diagram[1][self.rank[student]*2+1]])
        return plants
