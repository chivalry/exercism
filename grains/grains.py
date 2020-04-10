def square(number):
    if number not in range(1, 65):
        raise ValueError('number out of range')
    return 2 ** (number - 1)


def total():
    return sum(square(number) for number in range(1, 65))
