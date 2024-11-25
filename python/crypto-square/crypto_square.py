from string import punctuation
from math import ceil, sqrt


def cipher_text(plain_text: str) -> list[str]:
    """Return text using a crypto square
    :param plain_text: str - The text to encode
    :return list[str] - The encoded string
    """
    plain_text = plain_text.translate(
        str.maketrans('', '', punctuation + ' ')
    ).lower()
    length = len(plain_text)
    if length <= 1:
        return plain_text
    cols = ceil(sqrt(length))
    chunked = chunks(plain_text, cols)
    chunked[-1] = chunked[-1].ljust(8)
    transposed = list(map(list, zip(*chunked)))
    return ' '.join([''.join(line) for line in transposed])


def chunks(text: str, length: int) -> list[str]:
    '''Return a list with the string broken into chunks of length specified.

    :param length: int - The length of the chunks to break the string into
    :return list[str] - A list of strings, each one no longer than `length`
    '''
    return [
        text[0 + i:length + i]
        for i in range(0, len(text), length)
    ]
