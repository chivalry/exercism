OUTER = 10
MIDDLE = 5
INNER = 1


def score(x, y):
    mag = (x ** 2 + y ** 2) ** (1/2)
    if mag > OUTER:
        return 0
    if mag > MIDDLE:
        return 1
    if mag > INNER:
        return 5
    return 10
