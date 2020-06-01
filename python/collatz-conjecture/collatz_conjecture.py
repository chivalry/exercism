def steps(number):
    if number < 1:
        raise ValueError('Error: number out of range')
    if number == 1:
        return 0
    if number % 2 == 0:
        return steps(number / 2) + 1
    return steps(number * 3 + 1) + 1


if __name__ == '__main__':
    print(steps(12))
