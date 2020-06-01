def convert(number):
    msj = ''
    sw = 0
    if(number % 3 == 0):
        msj += 'Pling'
        sw = 1

    if(number % 5 == 0):
        msj += 'Plang'
        sw = 1

    if(number % 7 == 0):
        msj += 'Plong'
        sw = 1

    if(sw == 0):
        msj += str(number)

    return msj
