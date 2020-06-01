# Exercism high_scores.py


def latest(scores):
    """Takes a list and returns the last (latest) item"""
    latest_score = scores[-1]
    return latest_score


def personal_best(scores):
    """Returns the highest item"""
    best_score = max(scores)
    return best_score


def personal_top_three(scores):
    """Sorts and reverses scores and returns the highest three"""
    top_three = sorted(scores, reverse=True)
    return top_three[:3]
