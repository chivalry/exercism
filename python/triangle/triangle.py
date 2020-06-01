def equilateral(sides):
    sides_set = set(sides)
    return len(sides_set) == 1 and sides_set != set([0])


def isosceles(sides):
    sides_set = set(sides)
    if len(sides_set) in [1, 2]:
        if max(sides_set) > 2 * min(sides_set):
            return False
        return True
    return False


def scalene(sides):
    sides_set = set(sides)
    if len(sides_set) == 3:
        if max(sides_set) > sum([side for side in sides_set if side != max(sides_set)]):
            return False
        return True
    return False
