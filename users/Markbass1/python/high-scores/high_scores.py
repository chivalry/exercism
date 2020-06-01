def latest(scores):  # last added score
    return scores[-1]


def personal_best(scores):  # high score
    return max(scores)


def personal_top_three(scores):  # top 3 scores
    sorted_scores = sorted(scores)
    return sorted_scores[::-1][0:3]
