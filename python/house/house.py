LINES = {
    'lay in': 'the house that Jack built',
    'ate': 'the malt',
    'killed': 'the rat',
    'worried': 'the cat',
    'tossed': 'the dog',
    'milked': 'the cow with the crumpled horn',
    'kissed': 'the maiden all forlorn',
    'married': 'the man all tattered and torn',
    'woke': 'the priest all shaven and shorn',
    'kept': 'the rooster that crowed in the morn',
    'belonged to': 'the famer sowing his corn',
    '': 'the horse and the hound and the horn'
}


def recite(start_verse, end_verse):
    return list(LINES.values())[start_verse - 1]


print(recite(12, 12))
