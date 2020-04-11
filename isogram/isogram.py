from string import ascii_lowercase

def is_isogram(string: str):
    filtered = [s for s in string.lower() if s in ascii_lowercase]
    return len(set(filtered)) == len(filtered)