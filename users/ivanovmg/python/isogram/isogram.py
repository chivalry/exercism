def is_isogram(string):
    clean_string = _clean(string)
    return len(clean_string) == len(set(clean_string))


def _clean(string):
    bad_chars = ['-', ' ']
    lower = string.lower()
    for char in bad_chars:
        lower = lower.replace(char, '')
    return lower
