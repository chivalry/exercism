def latest(scores):
    last = scores.pop()
    return last


def personal_best(scores):
    scores.sort(reverse=True)
    return scores[0]


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]
