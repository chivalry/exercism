COLORS = [
    'black',  'brown',
    'red',    'orange',
    'yellow', 'green',
    'blue',   'violet',
    'grey',   'white',
]

TOLERANCES = {
    'grey': 0.05, 'violet': 0.1,
    'blue': 0.25, 'green': 0.5,
    'brown': 1,   'red': 2,
    'gold': 5,    'silver': 10
}


def resistor_label(colors):
    if len(colors) == 1:
        return '0 ohms'
    tolerance = TOLERANCES[colors[-1]]
    multiplier = 10 ** COLORS.index(colors[-2])
    base = 10 * COLORS.index(colors[-4]) + COLORS.index(colors[-3])
    if len(colors) == 5:
        base += 100 * COLORS.index(colors[0])
    ohms = base * multiplier
    prefix = ''
    for si_pref in ['kilo', 'mega', 'giga']:
        if ohms < 1000:
            break
        ohms /= 1000
        prefix = si_pref
    ohms = int(ohms) if ohms == int(ohms) else ohms
    return f'{ohms} {prefix}ohms ±{tolerance}%'
