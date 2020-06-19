result = 0

def latest(scores):
    result = scores[- 1]
    return result


def personal_best(scores):
    scores.sort(reverse=True)
    result = scores[0]
    return result


def personal_top_three(scores):
    scores.sort(reverse=True)
    top_three_scores = []

    i=0

    for idx in range(len(scores)):
        if i == 3:
            return top_three_scores
        i+= 1
        top_three_scores.append(scores[idx])
    
    return top_three_scores
