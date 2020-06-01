def is_isogram(string):
    present = set()
    for ch in filter(lambda ch: ch.isalpha(), string.lower()):
        if ch in present:
            return False
        present.add(ch)
    return True
