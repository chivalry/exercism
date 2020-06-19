import string

def is_isogram(word):
    letters = [_ for _ in word.lower() if _ in string.ascii_letters]
    return len(set(letters)) == len(letters)