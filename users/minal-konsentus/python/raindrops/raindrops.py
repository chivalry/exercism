def convert(number):
    raindrops = ''
    if (number % 3) == 0:
        raindrops = raindrops + 'Pling'
    if (number % 5) == 0:
        raindrops = raindrops + 'Plang'
    if (number % 7) == 0:
        raindrops = raindrops + 'Plong'
    if raindrops == '':
        return str(number)
    return raindrops
