def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores = sorted(scores)
    top_three = scores[-3:]
    top_three.reverse()
    return top_three
