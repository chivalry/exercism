def latest(scores):
	return scores[-1]

def personal_best(scores):
	return max(scores)

def personal_top_three(scores):
	top_3 = sorted(scores, reverse=True)

	return top_3 if len(scores) <= 3 else top_3[0:3]
