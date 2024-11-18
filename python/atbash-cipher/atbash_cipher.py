LOWER = 'abcdefghijklmnopqrstuvwxyz'
UPPSER = LOWER.upper()


def encode(plain_text):
    translation = str.maketrans(LOWER + UPPSER, LOWER[::-1] * 2, ' .,')
    return ' '.join(chunkstring(plain_text.replace(' ', '').translate(translation), 5))


def decode(ciphered_text):
    return encode(ciphered_text.replace(' ', '')).replace(' ', '')


def chunkstring(string, length):
    return [string[0 + i:length + i] for i in range(0, len(string), length)]
