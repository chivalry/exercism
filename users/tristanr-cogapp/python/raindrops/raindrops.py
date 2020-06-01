def convert(number):

    if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:

        s = ''

        if number % 3 == 0:
            s += 'Pling'

        if number % 5 == 0:
            s += 'Plang'

        if number % 7 == 0:
            s += 'Plong'

        return s

    return str(number)
