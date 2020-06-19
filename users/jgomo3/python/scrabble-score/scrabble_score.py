import string

LETTER_SCORES = {
    l:s
    for s, lts in {
        1 : 'A, E, I, O, U, L, N, R, S, T',
        2 : 'D, G',
        3 : 'B, C, M, P',
        4 : 'F, H, V, W, Y',
        5 : 'K',
        8 : 'J, X',
        10: 'Q, Z',
    }.items()
    for l in lts.split(', ')
}

def score(text):
    if text.isalpha():
        return sum(LETTER_SCORES[l] for l in text.upper())
    else:
        return 0