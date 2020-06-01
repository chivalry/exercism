scores = [100,200,400,300,400,50,300,99,999]


def latest(scores):
    return scores[-1]



def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    return sorted(scores, reverse=True)[0:3]
