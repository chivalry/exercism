from string import ascii_uppercase
from random import randint, seed


class Robot:
    def __init__(self):
        self._generate_name()

    def reset(self):
        self._generate_name()

    def _generate_name(self):
        seed()
        self.name = self._random_letter() + self._random_letter() + str(randint(100, 999))

    def _random_letter(self):
        return ascii_uppercase[randint(0, 25)]
