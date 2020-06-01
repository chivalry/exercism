def latest(scores: [int]):
    return scores[-1]


def personal_best(scores: [int]):
    scores.sort(reverse=True)
    return scores[0]


def personal_top_three(scores: [int]):
    scores.sort(reverse=True)
    return scores[0:3]
