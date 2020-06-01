def latest(scores):
    #returns the last item in a list
    return scores[-1]

def personal_best(scores):
    #returns the largest item in a list
    return max(scores)

def personal_top_three(scores):
    #mutates a list by ordering them descendingly(reverse),then returns the first three
    return sorted(scores, reverse = True)[:3]
