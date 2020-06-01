def latest(scores=[]):
    return scores.pop()


def personal_best(scores=[]):
    return (sorted(scores)).pop()


def personal_top_three(scores=[]):
    scores_sorted = sorted(scores)[-3:]
    scores_sorted.reverse()
    return scores_sorted
