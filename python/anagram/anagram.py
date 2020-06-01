def normalized(word):
    return sorted(tuple(word.lower()))


def is_anagram(word, candidate):
    return normalized(word) == normalized(candidate) and word.lower() != candidate.lower()


def find_anagrams(word, candidates):
    return [candidate for candidate in candidates if is_anagram(word, candidate)]
