def latest(scores):
    return scores[len(scores)-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    temp = []
    length = len(scores)
    for i in range(length):
        if len(temp) == 3:
            break
        else:
            temp.append(scores.pop(scores.index(max(scores))))
    return sorted(temp,reverse=True)

print(personal_top_three([40]))