def latest(scores):
    return scores[-1]


def personal_best(scores):
    scores.sort()
    return scores[-1]


def personal_top_three(scores):
    scores.sort()
    final_result = scores[-3::]
    return final_result[::-1]