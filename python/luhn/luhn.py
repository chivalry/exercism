class Luhn:
    def __init__(self, card_num):
        if not all(c.isdigit() or c == ' ' for c in card_num):
            self.card = []
        else:
            self.card = [int(c) for c in card_num if c.isdigit()]

    def valid(self):
        if not self.card or len(self.card) <= 1:
            return False
        doubled = []
        for i, digit in enumerate(reversed(self.card)):
            if i % 2 == 0:
                doubled.append(digit)
            else:
                cand = digit * 2
                cand = cand - 9 if cand > 9 else cand
                doubled.append(cand)
        return sum(doubled) % 10 == 0
