def convert(number):
    buf = ''
    if number % 3 == 0:
        buf = 'Pling'
    if number % 5 == 0:
        buf += 'Plang'
    if number % 7 == 0:
        buf += 'Plong'
    return buf if buf else str(number)
