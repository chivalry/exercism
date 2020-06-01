def convert(number):
    pling = 'Pling' if number % 3 == 0 else ''
    plang = 'Plang' if number % 5 == 0 else ''
    plong = 'Plong' if number % 7 == 0 else ''
    raindrop = f'{pling}{plang}{plong}'
    return raindrop if len(raindrop) > 0 else f'{number}'
