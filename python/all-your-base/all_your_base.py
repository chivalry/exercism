from math import log


def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Convert the digits from the input base to the output base.
    :param input_base: int - The base the digits are originally represented in
    :param digits: list[int] - A list of the "digits" representing the number in the input base
    :param output_base: int - The base the digits should represent once converted
    :return list[int] - The converted digits in the output base
    :note - Uses base-10 as an interim base, taking advantage when it's either the input or the
            output base
    """
    if (in_err := input_base < 2) or output_base < 2:
        raise ValueError(f'{"input" if in_err else "output"} base must be >= 2')
    if any([digit < 0 or digit >= input_base for digit in digits]):
        raise ValueError('all digits must satisfy 0 <= d < input base')
    number = int(''.join([str(digit) for digit in digits])
                 ) if input_base == 10 else to_base_10(input_base, digits)
    if output_base == 10:
        return [int(digit) for digit in str(number)]
    return from_base_10(number, output_base)


def to_base_10(input_base: int, digits: list[int]) -> int:
    """Convert the digits, representing a number in the input base, to a number in base-10.
    :param input_base: int - The base the digits are originally represented in
    :param digits: int - An integer representing the number in base 10.
    """
    result = 0
    for idx, digit in enumerate(reversed(digits)):
        result += digit * input_base ** idx
    return result


def from_base_10(number: int, output_base: int) -> list[int]:
    """Convert the number to a list of digits in the output base.
    :param number: int - The number to convert
    :param output_base: int - The base the digits should represent once converted
    :return list[int] - The converted digits in the output base
    """
    if number == 0:
        return [0]
    max_pow = int(log(number, output_base))
    result = []
    for pow in range(max_pow, -1, -1):
        place = output_base ** pow
        divved = number // place
        result += [divved]
        number -= divved * place
    return result
