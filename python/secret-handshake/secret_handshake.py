ACTIONS = [
    'wink',
    'double blink',
    'close your eyes',
    'jump'
]


def commands(binary_str):
    code = int(binary_str, 2)
    ''' original code
    shake = []
    for i in range(4):
        if bit_is_set(code, i):
            shake.append(ACTIONS[i])
    if bit_is_set(code, 4):
        shake.reverse()
    return shake
    '''
    shake = [ACTIONS[i] for i in range(4) if bit_is_set(code, i)]
    return shake[::-1] if bit_is_set(code, 4) else shake


def bit_is_set(num, pos):
    '''Return `True` if the bit at the given position is on, position moving from left to
    right starting at 0.

    Works by shifting the bits until the target position is in the 0th spot and bit-wise anding
    with 1.
    '''
    return (num >> pos) & 1
