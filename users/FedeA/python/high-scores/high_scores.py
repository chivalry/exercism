""" for returning high scores """


def latest(scores: list) -> int:
    """ latest scores """
    return scores[-1]


def personal_best(scores: list) -> int:
    """ personal best """
    return max(scores)


def personal_top_three(scores: list) -> list:
    """ personal top three """
    return sorted(scores, reverse=True)[:3]
