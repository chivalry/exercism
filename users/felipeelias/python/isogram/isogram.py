import string


def is_isogram(words):
    letters = set()

    for char in words.lower():
        if char in letters and char in string.ascii_lowercase:
            return False
        else:
            letters.add(char)

    return True
