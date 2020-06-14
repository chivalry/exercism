def is_isogram(string):
    alphabets = set()

    for char in string.lower():
        if char in alphabets:
            return False
        elif char.isalpha():
            alphabets.add(char)

    return True
