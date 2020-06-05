def score(word):

    letters = {'aeioulnrst': 1,
               'dg': 2,
               'bcmp': 3,
               'fhvwy': 4,
               'k': 5,
               'jx': 8,
               'qz': 10}
    letter_score = {**dict.fromkeys(list('aeioulnrst'), 1),
                    **dict.fromkeys(list('dg'), 2),
                    **dict.fromkeys(list('bcmp'), 3),
                    **dict.fromkeys(list('fhvwy'), 4),
                    **dict.fromkeys(list('k'), 5),
                    **dict.fromkeys(list('jx'), 8),
                    **dict.fromkeys(list('qz'), 10)}
    letter_score = {char: score for letters, score in letters.items() for char in letters}
    letter_score = {}
    for letters, score in letters.items():
        letter_score = {**letter_score, **dict.fromkeys(list(letters), score)}

    return sum([letter_score[i] for i in word.lower()])
