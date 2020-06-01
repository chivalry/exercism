def convert(number):
    rain_drop = ''
    if number % 3 == 0:
        rain_drop += 'Pling'
    if number % 5 == 0:
        rain_drop += 'Plang'
    if number % 7 == 0:
        rain_drop += 'Plong'
    if rain_drop == '':
        rain_drop = str(number)
    return rain_drop


