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

PREFIX_DICT = {1_000_000_000: "giga", 1_000_000: "mega", 1_000: "kilo", 0: ""}


def resistor_label(colors):
    if len(colors) == 1:
        return '0 ohms'
    tolerance = TOLERANCES[colors[-1]]
    multiplier = 10 ** COLORS.index(colors[-2])
    base = 10 * COLORS.index(colors[-4]) + COLORS.index(colors[-3])
    if len(colors) == 5:
        base += 100 * COLORS.index(colors[0])
    ohms = base * multiplier
    ohms, prefix = si_conversion(ohms)
    ohms = int(ohms) if ohms == int(ohms) else ohms
    return f'{ohms} {prefix}ohms ±{tolerance}%'


def si_conversion(magnitude):
    (new_mag, prefix) = next((new_mag, prefix)
                             for new_mag, prefix in PREFIX_DICT.items() if new_mag <= magnitude)
    magnitude = magnitude / new_mag if new_mag > 0 else magnitude
    return magnitude, prefix
