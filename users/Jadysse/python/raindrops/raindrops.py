def convert(number):
    PlingPlangPlong = ''

    if number % 3 == 0:
        PlingPlangPlong += 'Pling'
    if number % 5 == 0:
        PlingPlangPlong += 'Plang'
    if number % 7 == 0:
        PlingPlangPlong += 'Plong'
    if PlingPlangPlong:
        return PlingPlangPlong
    else:
        return str(number)

print(convert(5))