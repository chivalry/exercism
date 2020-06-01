def latest(scores):
    return scores.pop()

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    scores.sort(key=None, reverse=True)
    return scores[0:3]
