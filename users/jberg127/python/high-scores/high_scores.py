def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    # sort list in descending order
    scores = sorted(scores, reverse=True)
    # print the top 3 (first) scores in the list, or the whole list if < 3
    return scores[:min(len(scores), 3)]
