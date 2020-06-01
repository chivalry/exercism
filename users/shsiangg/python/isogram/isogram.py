def is_isogram(string):
    hash = {}

    for c in string.lower():
        if c in hash.keys():
            if c == ' ' or c == '-':
                continue
            return False
        else:
            hash[c] = 1
    return True
