def latest(scores):
    return scores[-1]


def personal_best(scores):
    max_value = 0
    for value in scores:
        if value > max_value:
            max_value = value
    return max_value


def personal_top_three(scores):
    top_3 = [0, 0, 0]
    for value in scores:
        if value > top_3[0]:
            top_3.insert(0, value)
        elif value > top_3[1]:
            top_3.insert(1, value)
        elif value > top_3[2]:
            top_3.insert(2, value)
    return top_3[0:-3] if len(top_3) <= 6 else top_3[0:3]

