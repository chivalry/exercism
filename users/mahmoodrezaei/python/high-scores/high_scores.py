def latest(scores):
    return scorses[len(scores)] # return latest added data to scores list  


def personal_best(scores):
    scores.sort()
    return scores[0]#return best personal


def personal_top_three(scores):
    scores.sort()#sort the scores list
    return [scores[0],scores[1],scores[2]] #return 3 best personals
