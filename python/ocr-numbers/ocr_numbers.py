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


def chunkstring(string: str, length: int):
    return [string[0 + i:length + i] for i in range(0, len(string), length)]
