score_relation_list = [
    (['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 1),
    (['D', 'G'], 2),
    (['B', 'C', 'M', 'P'], 3),
    (['F', 'H', 'V', 'W', 'Y'], 4),
    (['K'], 5),
    (['J', 'X'], 8),
    (['Q', 'Z'], 10),
]

sc_dict = {}
for ch, value in score_relation_list:
    sc_dict.update(dict.fromkeys(ch, value))


def score(word):
    word = word.upper()
    return sum(sc_dict[ch] for ch in word)