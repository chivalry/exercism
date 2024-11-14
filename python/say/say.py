ONES = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'ninteen',
]

TENS = [
    '', '',
        'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
        'eighty',
    'ninety']

BASES = (
    (1000000000, 'billion'),
    (1000000, 'million'),
    (1000, 'thousand'),
    (100, 'hundred'),
)


def say(num):
    parts = []
    if not 0 <= num < 1000000000000:
        raise ValueError('input out of range')
    if num == 0:
        return ONES[num]
    for base, name in BASES:
        if num >= base:
            parts.append(say(int(num // base)))
            parts.append(name)
            num = int(num % base)
    out = ''
    if num >= 20:
        out += TENS[num // 10]
        num = int(num % 10)
        if num:
            out += '-'
    if num and num < 20:
        out += ONES[num]
    if out:
        parts.append(out)
    return ' '.join(parts)
