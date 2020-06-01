def is_isogram(string):
    letters = [letter.lower() for letter in string if letter != "-" and letter != " "]
    return len(letters) == len(set(letters))
