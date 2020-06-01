def convert(number):
    a = ''
    if number % 3 == 0:
        a += "Pling"

    if number % 5 == 0:
        a += "Plang"

    if number % 7 == 0:
        a += "Plong"

    if a == '':
        return str(number)
    else:
        return a