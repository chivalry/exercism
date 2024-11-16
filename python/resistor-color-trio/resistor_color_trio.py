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

PREFIX_DICT = {1_000_000_000: "giga", 1_000_000: "mega", 1_000: "kilo", 0: ""}


def label(colors):
    base = 10 * COLORS.index(colors[0]) + COLORS.index(colors[1])
    exponent = 10 ** COLORS.index(colors[2])
    ohms = base * exponent
    ohms, prefix = si_conversion(ohms)
    return f'{int(ohms)} {prefix}ohms'


def si_conversion(magnitude):
    (new_mag, prefix) = next((new_mag, prefix)
                             for new_mag, prefix in PREFIX_DICT.items() if new_mag <= magnitude)
    magnitude = magnitude / new_mag if new_mag > 0 else magnitude
    return magnitude, prefix
