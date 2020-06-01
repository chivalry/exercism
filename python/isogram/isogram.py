def is_isogram(string: str):
    chars = set()
    for char in string.lower():
        if char.isalpha() and char in chars:
            return False
        chars.add(char)
    return True
