COLORS = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white',
]


def label(colors):
    base = 10 * COLORS.index(colors[0]) + COLORS.index(colors[1])
    exponent = 10 ** COLORS.index(colors[2])
    ohms = base * exponent
    prefix = ''
    for si_pref in ['kilo', 'mega', 'giga']:
        if ohms < 1000:
            break
        ohms /= 1000
        prefix = si_pref
    return f'{int(ohms)} {prefix}ohms'
