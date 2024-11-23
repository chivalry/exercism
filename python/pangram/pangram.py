import string


def is_pangram(sentence):
    sentence = sentence.lower()
    for char in string.ascii_lowercase:
        if char not in sentence:
            return False
    return True
