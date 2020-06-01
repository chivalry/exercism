def latest(scores: list) -> int:
    """
        :param scores: contains player scores
        :return: latest score
    """
    return scores[-1]


def personal_best(scores: list) -> int:
    """
        :param scores: contains player scores
        :return: personal best score
    """
    return max(scores)


def personal_top_three(scores: list) -> list:
    """
        :param scores: contains player scores
        :return: personal 3 best scores
    """
    return sorted(scores, reverse=True)[:3]
