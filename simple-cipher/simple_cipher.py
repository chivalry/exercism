from string import ascii_lowercase
from random import choice


class Cipher:
    chars = ascii_lowercase

    def __init__(self, key=None):
        self.key = key or ''.join([choice(self.chars) for _ in range(100)])

    def encode(self, text):
        return self.code(text, 'encode')

    def decode(self, text):
        return self.code(text, 'decode')

    def code(self, text, action):
        sign = 1 if action == 'encode' else -1
        buf = ''
        for i, char in enumerate(text):
            shift = self.chars.find(self.key[i % len(self.key)]) * sign
            pos = self.chars.find(char)
            buf += self.chars[(pos + shift) % len(self.chars)]
        return buf
