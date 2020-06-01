def latest(scores):
    return scores[len(scores)-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    
    def get_highest(scorelist):
        highest = max(scorelist)
        scorelist.remove(highest)
        return highest
    
    def number_of(scorelist):
        number = len(scorelist)
        if 3 < number:
            number = 3
        return number

    return [get_highest(scores) for each_x in range(number_of(scores))]
