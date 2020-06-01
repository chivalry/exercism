def latest(scores):
    ''' conflating int and string return value but don't 
    want to use Errors/Exceptions for expected situations 
    '''
    return scores[-1] if not scores == [] else "list empty"


def personal_best(scores):
    return max(scores) if not scores == [] else "list empty"


def personal_top_three(scores):
    return sorted(scores, reverse=True)[:3]
