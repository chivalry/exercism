import string

LETTERS = string.ascii_uppercase


def rows(letter):
    if letter == 'A':
        return ['A']
    pos = LETTERS.find(letter) + 1
    len = pos * 2 - 1
    result = ['A'.center(len)]
    result.extend((char + (' ' * ((idx + 1) * 2 - 1)) + char).center(len)
                  for idx, char in enumerate(LETTERS[1:pos]))
    result.extend(result[-2::-1])
    return result
