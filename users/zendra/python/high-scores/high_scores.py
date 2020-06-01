def latest(scores):
    return scores[-1]
#returns latest added score in list


def personal_best(scores):
    return max(scores)
#returns max score in list

def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]
#returns top three max scores in list