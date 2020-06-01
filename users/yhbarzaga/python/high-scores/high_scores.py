def latest(scores: list) -> int:
    return scores[-1]


def personal_best(scores: list) -> int:
    scores.sort(reverse=True)
    return scores[0]


def personal_top_three(scores: list) -> list:
    scores.sort(reverse=True)
    return scores[:3]
