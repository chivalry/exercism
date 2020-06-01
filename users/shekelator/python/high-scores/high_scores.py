def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    copy = (scores[:])
    copy.sort(reverse=True)
    return copy[:3]

