def convert(number):
    raindrop_converter = ''

    if number % 3 == 0:
        raindrop_converter += 'Pling'
    if number % 5 == 0:
        raindrop_converter += 'Plang'
    if number % 7 == 0:
        raindrop_converter += 'Plong'

    if not raindrop_converter:
        return str(number)
    return raindrop_converter
