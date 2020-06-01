def is_isogram(string):
    chars = {}

    for character in string:
        ch = character.lower()
        if (ch not in ['-', ' ']) and ch in chars and chars[ch] > 0 :
           return False
        else:
           chars[ch] = 1

    return True
