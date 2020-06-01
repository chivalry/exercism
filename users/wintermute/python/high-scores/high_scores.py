def latest(scores):
    index_of_latest = len(scores) - 1
    latest_score = scores[index_of_latest]
    return latest_score

def personal_best(scores):
    scores.sort(reverse=True)
    best = scores[0]
    return best

def personal_top_three(scores):
    scores.sort(reverse=True)
    top3 = scores[:3]
    return top3
