def updated_data(data, result):
    data = data.copy()
    data['matches'] += 1
    if result == 'win':
        data['wins'] += 1
        data['points'] += 3
    if result == 'draw':
        data['draws'] += 1
        data['points'] += 1
    if result == 'loss':
        data['losses'] += 1
    return data


def format_results(results):
    header = [['Team', 'MP', 'W', 'D', 'L', 'P']]
    results = [[key, value['matches'], value['wins'], value['draws'], value['losses'], value['points']]
               for key, value in results.items()]
    results.sort(key=lambda elem: (elem[5] * -1, elem[0]))
    return [f'{result[0]:<31}| {result[1]:>2} | {result[2]:>2} | ' +
            f'{result[3]:>2} | {result[4]:>2} | {result[5]:>2}'
            for result in header + results]


def tally(matches):
    results = {}
    default = {
        'matches': 0,
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'points': 0
    }
    for match in matches:
        home, visitor, result = match.split(';')
        results[home] = updated_data(results.get(home, default), result)
        result = {'win': 'loss', 'loss': 'win', 'draw': 'draw'}[result]
        results[visitor] = updated_data(results.get(visitor, default), result)
    return format_results(results)