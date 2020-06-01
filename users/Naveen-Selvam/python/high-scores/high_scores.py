def latest(scores):
    for x in scores:
      return scores[-1]


def personal_best(scores):
    for x in scores:
      return max(scores)


def personal_top_three(scores):
    for x in scores:
        return sorted(scores , reverse=True)[ :3]
