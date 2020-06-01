def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max((score for score in scores))


def personal_top_three(scores):
   return sorted(scores, reverse=True)[:3]
