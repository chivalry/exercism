def latest(scores):
    '''return last element in list'''
    return scores[-1]

def personal_best(scores):
    '''return highest number in list'''
    return sorted(scores)[-1]

def personal_top_three(scores):
    '''return list with up to 3 elements from highest to lowest value'''
    return sorted(scores, reverse=True)[:3]
