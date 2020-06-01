def latest(scores):
    """Return latest score"""
    return scores[-1]


def personal_best(scores):
    """Return best score"""
    return max(scores)


def personal_top_three(scores):
    """ Return top 3 scores"""
    return sorted(scores, reverse=True)[:3]
