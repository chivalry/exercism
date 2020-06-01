def latest(scores):
    return scores[-1]
    
def personal_best(scores):
    scores=sorted(scores)
    return scores[-1]

def personal_top_three(scores):
    scores=sorted(scores)
    if(len(scores)>=3):
        return [scores[-1],scores[-2],scores[-3]]
    
    if(len(scores)==2):
        return [scores[-1],scores[-2]]

    if(len(scores)==1):
        return [scores[-1]]