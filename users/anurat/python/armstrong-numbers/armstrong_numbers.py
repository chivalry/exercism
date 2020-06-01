def is_armstrong_number(number):
    digits = list(str(number))
    length = len(digits)
    armstrong = sum([int(digit) ** length for digit in digits])
    return armstrong == number
