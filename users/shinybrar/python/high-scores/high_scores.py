class HighScores(object):
    """
    Exercism: High Scores
    """

    def __init__(self, scores: list):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def scores(self):
        return self.scores

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        # Instead of reference copy, scores is now copied by value
        # https://docs.python.org/3/faq/programming.html#how-do-i-copy-an-object-in-python
        scores = self.scores[:]
        scores.sort(reverse=True)
        return scores[0:3]
