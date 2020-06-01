def latest(scores):
	return scores[-1]


def personal_best(scores):
  	scores.sort(reverse=True)
  	return scores[0] # sort in reverse "high to low" 



def personal_top_three(scores):
	scores.sort(reverse=True)
	return sorted(scores, reverse=True)[::3]
