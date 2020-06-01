STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.word = word
        self.mask = '_' * len(word)
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING

    def guess(self, char):
        if self.status in [STATUS_WIN, STATUS_LOSE]:
            raise ValueError('The game is over.')
        if (char in self.word) and (char not in self.mask):
            for i in range(len(self.word)):
                if self.word[i] == char:
                    self.mask = self.mask[:i] + char + self.mask[i+1:]
        else:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE
        if self.mask == self.word:
            self.status = STATUS_WIN

    def get_masked_word(self):
        return self.mask

    def get_status(self):
        return self.status
