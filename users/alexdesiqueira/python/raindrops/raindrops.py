def convert(number: int) -> str:
    """Convert a number into a string containing raindrop sounds.

    Parameters
    ----------
    number : int
        An integer.

    Returns
    -------
    raindrops : str
        If `number` is divisible by 3, 5, or 7, returns specific raindrops;
        if not, returns the input number in a string.

    Notes
    -----
    `raindrops` contains the following raindrops if number is divisible by
    3, 5, or 7: Pling, Plang, or Plong, respectively.
    """
    raindrops = ''
    for (factor, char) in ((3, 'i'), (5, 'a'), (7, 'o')):
        if not (number % factor):
            raindrops += f'Pl{char}ng'
    if not raindrops:
        raindrops = str(number)

    return raindrops
