def latest(scores):
    return scores[-1]

def personal_best(scores):
    scores.sort()
    return scores[-1]

def personal_top_three(scores):
    aux=[]
    scores.sort()
    if len(scores)<2:
        aux=[scores[-1]]
        return aux
    if len(scores)<3:
        aux=[scores[-1],scores[-2]]
        return aux
    else:
        aux=[scores[-1],scores[-2],scores[-3]]
        return aux
