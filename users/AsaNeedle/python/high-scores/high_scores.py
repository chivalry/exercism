def latest(scores):
    if not scores:
        raise Exception("No scores to show")
    return scores[-1]

def personal_best(scores):
    if not scores:
        raise Exception("No scores to show")
    return max(scores)

def personal_top_three(scores):
    if not scores:
        raise Exception("No scores to show")
    scores.sort()
    res = []
    for i in range(min(3, len(scores))):
        res.append(scores[len(scores) - (i + 1)])
    return res
