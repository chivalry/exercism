LETTERS = [('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'), ('D', 'G'), ('B', 'C', 'M', 'P'), ('F', 'H', 'V', 'W', 'Y'), ('K'), ('J', 'X'), ('Q', 'Z')]
VALUES = {letter: value for le, value in zip(LETTERS, [1,2,3,4,5,8,10]) for letter in le}

def score(word):
    return sum(VALUES[c.upper()] for c in word)
