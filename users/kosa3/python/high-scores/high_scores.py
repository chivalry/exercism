def latest(scores):
    return scores[-1]


def personal_best(scores):
    sorted_lists = sorted(scores, reverse=True)
    return sorted_lists[0]


def personal_top_three(scores):
    sorted_lists = sorted(scores, reverse=True)
    return sorted_lists[0:3]
