from typing import List


def latest(scores: List) -> int:
    return scores[len(scores)-1]


def personal_best(scores: List) -> int:
    scores.sort(reverse=True)
    return scores[0]


def personal_top_three(scores: List) -> int:
    scores.sort(reverse=True)
    return scores[:3]
