def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores_rev = scores
    scores_rev.sort(reverse=True)
    return scores_rev [:3]
