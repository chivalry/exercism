def latest(scores):
    return scores[-1]



def personal_best(scores):
    scores.sort()
    return scores[-1]

def personal_top_three(scores):
    if len(scores) == 0:
        return 0
    elif len(scores) <= 3:
        scores.sort(reverse=True)
        return scores
    else:
        scores.sort(reverse=True)
        return scores[0:3]
