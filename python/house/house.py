LINES = {
    'lay in': 'house that Jack built',
    'ate': 'malt',
    'killed': 'rat',
    'worried': 'cat',
    'tossed': 'dog',
    'milked': 'cow with the crumpled horn',
    'kissed': 'maiden all forlorn',
    'married': 'man all tattered and torn',
    'woke': 'priest all shaven and shorn',
    'kept': 'rooster that crowed in the morn',
    'belonged to': 'farmer sowing his corn',
    '': 'horse and the hound and the horn'
}


def recite(start_verse, end_verse):
    result = []
    for verse in range(start_verse, end_verse + 1):
        result.append(build_verse(verse))
    return result


def build_verse(verse_number):
    clauses = list(reversed(list(LINES.values())[:verse_number]))
    verbs = list(reversed(list(LINES.keys())[:verse_number]))
    result = []
    for i, clause in enumerate(clauses):
        if i == 0:
            result.append('This is the ' + clause)
        else:
            result.append(f'that {verbs[i]} the {clause}')
    return ' '.join(result) + '.'
