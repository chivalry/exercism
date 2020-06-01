def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    reverse_sorted = sorted(scores, reverse=True)
    return reverse_sorted[0:3]
