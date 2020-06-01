def latest(scores):
   c = len(scores)
   return scores[c-1]

def personal_best(scores):
   scores.sort(reverse = True)
   return scores[0]


def personal_top_three(scores):
    scores.sort(reverse = True)
    return scores[0:3]
