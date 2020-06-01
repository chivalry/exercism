def latest(scores):
    if scores:
        return scores[len(scores) - 1]


def personal_best(scores):
    if scores:
        return max(scores)


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[:3]
