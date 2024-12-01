DIGIT_MAP = {
    ' _ | ||_|': '0',
    '     |  |': '1',
    ' _  _||_ ': '2',
    ' _  _| _|': '3',
    '   |_|  |': '4',
    ' _ |_  _|': '5',
    ' _ |_ |_|': '6',
    ' _   |  |': '7',
    ' _ |_||_|': '8',
    ' _ |_| _|': '9'
}


def convert(grid: list[str]) -> str:
    """Given a textual representation of LCD numerals, convert the text into a string of
    numerals with each "line" of numerals representing comma-separated powers of 10^3.
    :param grid: list[str] - The textual represenation of the numerals
    :return str - The converted string of numerals

    :note - The textual representation format:
         _  _
      | _| _|
      ||_  _|

        _  _
    |_||_ |_
      | _||_|

     _  _  _
      ||_||_|
      ||_| _|
    """
    if len(grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if len(grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")
    if len(grid) > 4:
        grids = [grid[0 + i:4 + i] for i in range(0, len(grid), 4)]
        return ','.join([convert(grid) for grid in grids])
    zipped = list(zip(
        chunkstring(grid[0], 3),
        chunkstring(grid[1], 3),
        chunkstring(grid[2], 3)))
    return ''.join(DIGIT_MAP[key] if key in DIGIT_MAP else '?'
                   for key in [''.join(elem) for elem in zipped])


def chunkstring(string: str, length: int) -> list[str]:
    """Break the given string into an array of strings of maximum length given by the
    parameter.
    :param string: str - The string to break into chunks
    :param length: int - The maximum length for each of the chunks
    :return list[str] - A list of strings, each one of which is the maximum given length
    """
    return [string[0 + i:length + i] for i in range(0, len(string), length)]
