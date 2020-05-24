def score(word):
    scores = {1: 'aeioulnrst',
              2: 'dg',
              3: 'bcmp',
              4: 'fhvwy',
              5: 'k',
              8: 'jx',
              10: 'qz'}
    letters = {c: score for score, chars in scores.items() for c in list(chars)}
    return sum(letters[c] for c in word.lower())
