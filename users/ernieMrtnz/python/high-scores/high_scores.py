def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    s = sorted(scores, reverse=True)
    ln = len(s)

    if ln >= 3:
        return s[:3]
    if ln == 2:
        return s[:2]
    return s[:1]
