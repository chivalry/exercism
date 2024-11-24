import string

LOWER = string.ascii_lowercase


def encode(plain_text):
    plain_text = plain_text.lower()
    translation = str.maketrans(LOWER, LOWER[::-1], ' .,')
    return ' '.join(chunkstring(
        plain_text.replace(' ', '').translate(translation), 5)
    )


def decode(ciphered_text):
    return encode(ciphered_text.replace(' ', '')).replace(' ', '')


def chunkstring(string, length):
    return [
        string[0 + i:length + i]
        for i in range(0, len(string), length)
    ]
