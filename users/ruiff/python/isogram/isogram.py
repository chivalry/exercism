def is_isogram(string):
    s = set()
    for c in string:
        if not c.isalpha():
            continue
        c = c.lower()
        if c in s:
            return False
        s.add(c)
    return True
