def latest(scores):
    """returns last score added"""
    return scores[-1]


def personal_best(scores):
    """returns highest score"""
    scores.sort()
    return scores[-1]


def personal_top_three(scores):
    """returns top 3 scores"""
    scores.sort(reverse=True)
    return scores[:3]
