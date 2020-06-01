def latest(scores):
    #Return the last element from the list
    return scores[-1]


def personal_best(scores):
    #Sort the list in descendent order and get the last item (greatest)
    scores.sort()
    return scores[-1]


def personal_top_three(scores):
    #Sort items and return from last one to the 3 element in reverse
    scores.sort()
    return scores[:-4:-1]