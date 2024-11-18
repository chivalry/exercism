LOWER = 'abcdefghijklmnopqrstuvwxyz'
UPPSER = LOWER.upper()


def encode(plain_text):
    plain_text = ''.join(plain_text.split(' '))
    translation = str.maketrans(LOWER + UPPSER, LOWER[::-1] * 2, ' .,')
    cipher = plain_text.translate(translation)
    return ' '.join(chunkstring(cipher, 5))


def decode(ciphered_text):
    cipher_text = ''.join(ciphered_text.split(' '))
    return ''.join(encode(cipher_text).split(' '))


def chunkstring(string, length):
    return [string[0 + i:length + i] for i in range(0, len(string), length)]
