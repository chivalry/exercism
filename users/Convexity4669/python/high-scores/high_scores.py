def latest(scores):
	return scores[-1]
# return the last score in the list


def personal_best(scores):
	return max(scores)
# return the highest score from the list


def personal_top_three(scores):
	scores.sort(reverse=True)
	if len(scores) > 2:
		return scores[:3]
	else:
		return scores
# return the top three scores in the list
