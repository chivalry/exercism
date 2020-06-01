def latest(scores):
    return scores.pop()

def personal_best(scores):
    return sorted(scores).pop()


def personal_top_three(scores):
    return sorted(scores, reverse=True)[:3]
